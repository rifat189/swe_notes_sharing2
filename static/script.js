// API Base URL
const API_BASE = '/api';

// State
let currentEditingNoteId = null;

// DOM Elements
const noteContent = document.getElementById('noteContent');
const charCount = document.getElementById('charCount');
const createBtn = document.getElementById('createBtn');
const notesList = document.getElementById('notesList');
const emptyState = document.getElementById('emptyState');
const notesCount = document.getElementById('notesCount');
const editModal = document.getElementById('editModal');
const editContent = document.getElementById('editContent');
const editCharCount = document.getElementById('editCharCount');
const saveEditBtn = document.getElementById('saveEditBtn');

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    loadNotes();
    setupEventListeners();
});

// Event Listeners
function setupEventListeners() {
    // Character counter for create
    noteContent.addEventListener('input', () => {
        charCount.textContent = noteContent.value.length;
    });

    // Character counter for edit
    editContent.addEventListener('input', () => {
        editCharCount.textContent = editContent.value.length;
    });

    // Create note
    createBtn.addEventListener('click', createNote);

    // Save edit
    saveEditBtn.addEventListener('click', saveEdit);

    // Enter to create (Ctrl+Enter in textarea)
    noteContent.addEventListener('keydown', (e) => {
        if (e.ctrlKey && e.key === 'Enter') {
            createNote();
        }
    });
}

// Load all notes
async function loadNotes() {
    try {
        const response = await fetch(`${API_BASE}/notes`);
        const data = await response.json();

        if (data.success) {
            displayNotes(data.data);
            notesCount.textContent = data.count;
        }
    } catch (error) {
        console.error('Error loading notes:', error);
        showError('Failed to load notes');
    }
}

// Display notes
function displayNotes(notes) {
    if (notes.length === 0) {
        notesList.style.display = 'none';
        emptyState.style.display = 'block';
        return;
    }

    notesList.style.display = 'grid';
    emptyState.style.display = 'none';

    // Sort by ID descending (newest first)
    notes.sort((a, b) => b.id - a.id);

    notesList.innerHTML = notes.map(note => createNoteCard(note)).join('');
}

// Create note card HTML
function createNoteCard(note) {
    const createdDate = new Date(note.created_at).toLocaleString();
    const updatedDate = new Date(note.updated_at).toLocaleString();
    const isUpdated = note.created_at !== note.updated_at;

    return `
        <div class="note-card" data-note-id="${note.id}">
            <div class="note-header">
                <span class="note-id">#${note.id}</span>
                <div class="note-actions">
                    <button class="btn btn-edit" onclick="openEditModal(${note.id})">
                        Edit
                    </button>
                    <button class="btn btn-danger" onclick="deleteNote(${note.id})">
                        Delete
                    </button>
                </div>
            </div>
            <div class="note-content">${escapeHtml(note.content)}</div>
            <div class="note-meta">
                <span>Created: ${createdDate}</span>
                ${isUpdated ? `<span>Updated: ${updatedDate}</span>` : ''}
            </div>
        </div>
    `;
}

// Create new note
async function createNote() {
    const content = noteContent.value.trim();

    if (!content) {
        showError('Please enter note content');
        return;
    }

    if (content.length > 300) {
        showError('Note exceeds 300 characters');
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/notes`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ content })
        });

        const data = await response.json();

        if (data.success) {
            noteContent.value = '';
            charCount.textContent = '0';
            loadNotes();
            showSuccess('Note created successfully!');
        } else {
            showError(data.error || 'Failed to create note');
        }
    } catch (error) {
        console.error('Error creating note:', error);
        showError('Failed to create note');
    }
}

// Open edit modal
async function openEditModal(noteId) {
    try {
        const response = await fetch(`${API_BASE}/notes/${noteId}`);
        const data = await response.json();

        if (data.success) {
            currentEditingNoteId = noteId;
            editContent.value = data.data.content;
            editCharCount.textContent = data.data.content.length;
            editModal.classList.add('active');
        } else {
            showError('Failed to load note');
        }
    } catch (error) {
        console.error('Error loading note:', error);
        showError('Failed to load note');
    }
}

// Close edit modal
function closeEditModal() {
    editModal.classList.remove('active');
    currentEditingNoteId = null;
    editContent.value = '';
    editCharCount.textContent = '0';
}

// Save edited note
async function saveEdit() {
    if (!currentEditingNoteId) return;

    const content = editContent.value.trim();

    if (!content) {
        showError('Note content cannot be empty');
        return;
    }

    if (content.length > 300) {
        showError('Note exceeds 300 characters');
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/notes/${currentEditingNoteId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ content })
        });

        const data = await response.json();

        if (data.success) {
            closeEditModal();
            loadNotes();
            // showSuccess('Note updated successfully!');
        } else {
            showError(data.error || 'Failed to update note');
        }
    } catch (error) {
        console.error('Error updating note:', error);
        showError('Failed to update note');
    }
}

// Delete note
async function deleteNote(noteId) {
    if (!confirm('Are you sure you want to delete this note?')) {
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/notes/${noteId}`, {
            method: 'DELETE'
        });

        const data = await response.json();

        if (data.success) {
            loadNotes();
            showSuccess('Note deleted successfully!');
        } else {
            showError(data.error || 'Failed to delete note');
        }
    } catch (error) {
        console.error('Error deleting note:', error);
        showError('Failed to delete note');
    }
}

// Utility functions
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function showError(message) {
    alert('Error: ' + message);
}

function showSuccess(message) {
    alert(message);
}

// Close modal on outside click
editModal.addEventListener('click', (e) => {
    if (e.target === editModal) {
        closeEditModal();
    }
});
