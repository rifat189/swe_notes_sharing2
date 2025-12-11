"""
NotesManager - Singleton Pattern Implementation

This class ensures only one instance of the notes storage manager exists
throughout the application lifecycle.
"""

from datetime import datetime
from threading import Lock


class NotesManager:
    """
    Singleton class for managing notes storage.
    Ensures only one instance exists across the application.
    """

    _instance = None
    _lock = Lock()

    def __new__(cls):
        """
        Override __new__ to implement Singleton pattern.
        Thread-safe implementation using double-checked locking.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(NotesManager, cls).__new__(cls)
                    cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """Initialize the notes manager only once."""
        if self._initialized:
            return

        self._notes = {}
        self._next_id = 1
        self._initialized = True

    def add_note(self, content):
        """
        Add a new note to storage.

        Args:
            content (str): The note content

        Returns:
            dict: The created note with id, content, and timestamps
        """
        note_id = self._next_id
        self._next_id += 1

        note = {
            'id': note_id,
            'content': content,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat()
        }

        self._notes[note_id] = note
        return note

    def get_note(self, note_id):
        """
        Retrieve a note by ID.

        Args:
            note_id (int): The note ID

        Returns:
            dict or None: The note if found, None otherwise
        """
        return self._notes.get(note_id)

    def get_all_notes(self):
        """
        Retrieve all notes.

        Returns:
            list: List of all notes
        """
        return list(self._notes.values())

    def update_note(self, note_id, content):
        """
        Update an existing note.

        Args:
            note_id (int): The note ID
            content (str): The new content

        Returns:
            dict or None: The updated note if found, None otherwise
        """
        if note_id not in self._notes:
            return None

        self._notes[note_id]['content'] = content
        self._notes[note_id]['updated_at'] = datetime.now().isoformat()

        return self._notes[note_id]

    def delete_note(self, note_id):
        """
        Delete a note by ID.

        Args:
            note_id (int): The note ID

        Returns:
            bool: True if deleted, False if not found
        """
        if note_id in self._notes:
            del self._notes[note_id]
            return True
        return False

    def get_notes_count(self):
        """
        Get the total count of notes.

        Returns:
            int: Number of notes
        """
        return len(self._notes)
