from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()
client = genai.Client()

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/notes', methods=['GET'])
def get_notes():
    conn = get_db_connection()
    notes = conn.execute('''
        SELECT notes.id, notes.title, notes.content,   notes.summary, categories.name AS category
        FROM notes
        LEFT JOIN categories ON notes.category_id = categories.id
        ''').fetchall()
    conn.close()
    return jsonify([dict(note) for note in notes])

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')
    category_id = data.get('category_id')

    if not title:
        return jsonify({"error": "Title is required"}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO notes (title, content, category_id) VALUES (?, ?, ?)',
                 (title, content, category_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Note created"}), 201

@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if not title:
        return jsonify({"error": "Title is required"}), 400

    conn = get_db_connection()
    conn.execute('UPDATE notes SET title = ?, content = ? WHERE id = ?', (title, content, note_id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Note updated"})

@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Note deleted"})

@app.route('/categories', methods=['GET'])
def get_categories():
    conn = get_db_connection()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    conn.close()
    return jsonify([dict(c) for c in categories])

@app.route('/hello')
def hello():
    name = request.args.get('name', 'stranger')
    return jsonify({"message": f"Hello, {name}!"})

@app.route('/')
def home():
    return "Hello, Flask!"

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/api/greeting')
def greeting():
    return jsonify({"message": "Hello from the API!"})

@app.route('/add-numbers', methods=['POST'])
def add_numbers():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')

    if a is None or b is None:
        return jsonify({"error": "Both 'a' and 'b' are required"}), 400
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "'a' and 'b' must be numbers"}), 400

    result = a + b
    return jsonify({"result": result})
@app.route('/notes/<int:note_id>/summarize', methods=['POST'])
def summarize_note(note_id):
    conn = get_db_connection()
    note = conn.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()

    if note is None:
        conn.close()
        return jsonify({"error": "Note not found"}), 404

    if note['summary']:
        conn.close()
        return jsonify({"summary": note['summary']})

    if not note['content'] or len(note['content'].strip()) < 20:
        conn.close()
        return jsonify({"error": "This note is too short to summarize"}), 400
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=note['content'],
            config=types.GenerateContentConfig(
                system_instruction="Summarize the student's note in 2-3 short sentences. " \
                "Use only information from the note. Do not add anything that isn't in it.",
                temperature=0.3,
            ),
        )
        summary = response.text
        if not summary:
            raise ValueError("Empty response")
    except Exception:
        conn.close()
        return jsonify({"error": "Could not summarize right now. Try again later."}), 502

    conn.execute('UPDATE notes SET summary = ? WHERE id = ?', (summary, note_id))
    conn.commit()
    conn.close()
    return jsonify({"summary": summary})

@app.route('/notes/<int:note_id>/study-questions', methods=['POST'])
def study_questions(note_id):
    conn = get_db_connection()
    note = conn.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()
    conn.close()

    if note is None:
        return jsonify({"error": "Note not found"}), 404

    if note ['study_questions']:
        return jsonify({"study_questions": note['study_questions']})

    if not note['content'] or len(note['content'].strip()) < 20:
        return jsonify({"error": "This note is too short to make questions from"}), 400

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=note['content'],
            config=types.GenerateContentConfig(
                system_instruction="TODO: write the instruction here, in quotes",
                temperature=0.3,
            ),
        )
        questions = response.text
        if not questions:
            raise ValueError("Empty response")
    except Exception:
        return jsonify({"error": "Could not make questions right now. Try again later."}), 502

    conn = get_db_connection()
    conn.execute('UPDATE notes SET study_questions = ? WHERE id = ?', (questions, note_id))
    conn.commit()
    conn.close()
    return jsonify({"study_questions": questions})
if __name__ == '__main__':
    app.run(debug=True)