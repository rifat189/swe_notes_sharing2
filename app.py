"""
Notes Sharing Web Application
Main Flask application with RESTful API
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from services.notes_service import NotesService

app = Flask(__name__)
CORS(app)  # Enable CORS for API access

# Initialize the notes service (Facade pattern)
notes_service = NotesService()


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


# API Routes

@app.route('/api/notes', methods=['GET'])
def get_notes():
    """Get all notes."""
    success, notes = notes_service.get_all_notes()
    return jsonify({
        'success': success,
        'data': notes,
        'count': len(notes)
    }), 200


@app.route('/api/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    """Get a specific note by ID."""
    success, result = notes_service.get_note(note_id)

    if not success:
        return jsonify({
            'success': False,
            'error': result
        }), 404

    return jsonify({
        'success': True,
        'data': result
    }), 200


@app.route('/api/notes', methods=['POST'])
def create_note():
    """Create a new note."""
    data = request.get_json()

    if not data or 'content' not in data:
        return jsonify({
            'success': False,
            'error': 'Content is required'
        }), 400

    success, result = notes_service.create_note(data['content'])

    if not success:
        return jsonify({
            'success': False,
            'error': result
        }), 400

    return jsonify({
        'success': True,
        'message': 'Note created successfully',
        'data': result
    }), 201


@app.route('/api/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    """Update an existing note."""
    data = request.get_json()

    if not data or 'content' not in data:
        return jsonify({
            'success': False,
            'error': 'Content is required'
        }), 400

    success, result = notes_service.update_note(note_id, data['content'])

    if not success:
        status_code = 404 if result == "Note not found" else 400
        return jsonify({
            'success': False,
            'error': result
        }), status_code

    return jsonify({
        'success': True,
        'message': 'Note updated successfully',
        'data': result
    }), 200


@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    """Delete a note."""
    success, result = notes_service.delete_note(note_id)

    if not success:
        return jsonify({
            'success': False,
            'error': result
        }), 404

    return jsonify({
        'success': True,
        'message': result
    }), 200


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get application statistics."""
    stats = notes_service.get_statistics()
    return jsonify({
        'success': True,
        'data': stats
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'success': False,
        'error': 'Resource not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500


if __name__ == '__main__':
    print("=" * 50)
    print("Notes Sharing Web App")
    print("=" * 50)
    print("Server starting on http://localhost:5000")
    print("API documentation: See API.md")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
