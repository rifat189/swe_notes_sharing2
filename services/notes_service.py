"""
NotesService - Facade Pattern Implementation

This class provides a simplified interface to the complex note management system,
hiding the underlying complexity and providing validation.
"""

from models.notes_manager import NotesManager


class NotesService:
    """
    Facade class that provides a simplified interface for note operations.
    Handles validation and error handling.
    """

    MAX_NOTE_LENGTH = 300

    def __init__(self):
        """Initialize the service with the singleton NotesManager."""
        self.notes_manager = NotesManager()

    def create_note(self, content):
        """
        Create a new note with validation.

        Args:
            content (str): The note content

        Returns:
            tuple: (success: bool, result: dict or error message: str)
        """
        # Validate content
        if not content or not content.strip():
            return False, "Note content cannot be empty"

        if len(content) > self.MAX_NOTE_LENGTH:
            return False, f"Note content cannot exceed {self.MAX_NOTE_LENGTH} characters"

        # Create note
        note = self.notes_manager.add_note(content.strip())
        return True, note

    def get_note(self, note_id):
        """
        Get a specific note by ID.

        Args:
            note_id (int): The note ID

        Returns:
            tuple: (success: bool, result: dict or error message: str)
        """
        try:
            note_id = int(note_id)
        except (ValueError, TypeError):
            return False, "Invalid note ID"

        note = self.notes_manager.get_note(note_id)

        if note is None:
            return False, "Note not found"

        return True, note

    def get_all_notes(self):
        """
        Get all notes.

        Returns:
            tuple: (success: bool, result: list)
        """
        notes = self.notes_manager.get_all_notes()
        return True, notes

    def update_note(self, note_id, content):
        """
        Update an existing note with validation.

        Args:
            note_id (int): The note ID
            content (str): The new content

        Returns:
            tuple: (success: bool, result: dict or error message: str)
        """
        # Validate note ID
        try:
            note_id = int(note_id)
        except (ValueError, TypeError):
            return False, "Invalid note ID"

        # Validate content
        if not content or not content.strip():
            return False, "Note content cannot be empty"

        if len(content) > self.MAX_NOTE_LENGTH:
            return False, f"Note content cannot exceed {self.MAX_NOTE_LENGTH} characters"

        # Update note
        note = self.notes_manager.update_note(note_id, content.strip())

        if note is None:
            return False, "Note not found"

        return True, note

    def delete_note(self, note_id):
        """
        Delete a note by ID.

        Args:
            note_id (int): The note ID

        Returns:
            tuple: (success: bool, result: str)
        """
        try:
            note_id = int(note_id)
        except (ValueError, TypeError):
            return False, "Invalid note ID"

        deleted = self.notes_manager.delete_note(note_id)

        if not deleted:
            return False, "Note not found"

        return True, "Note deleted successfully"

    def get_statistics(self):
        """
        Get statistics about notes.

        Returns:
            dict: Statistics including total count
        """
        return {
            'total_notes': self.notes_manager.get_notes_count(),
            'max_length': self.MAX_NOTE_LENGTH
        }
