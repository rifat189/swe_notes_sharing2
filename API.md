# Notes Sharing API Documentation

This document describes the RESTful API endpoints for the Notes Sharing Web App.

## Base URL

```
http://localhost:5000/api
```

## Endpoints

### 1. Get All Notes

Retrieve all notes in the system.

**Endpoint**: `GET /api/notes`

**Response**: 
```json
{
  "success": true,
  "data": [
    {
      "id": 1,
      "content": "Sample note content",
      "created_at": "2025-12-06T11:57:00",
      "updated_at": "2025-12-06T11:57:00"
    }
  ],
  "count": 1
}
```

**Status Codes**:
- `200 OK`: Success

---

### 2. Get Single Note

Retrieve a specific note by ID.

**Endpoint**: `GET /api/notes/<note_id>`

**Parameters**:
- `note_id` (path parameter): Integer ID of the note

**Response**:
```json
{
  "success": true,
  "data": {
    "id": 1,
    "content": "Sample note content",
    "created_at": "2025-12-06T11:57:00",
    "updated_at": "2025-12-06T11:57:00"
  }
}
```

**Status Codes**:
- `200 OK`: Note found
- `404 Not Found`: Note doesn't exist

---

### 3. Create Note

Create a new note.

**Endpoint**: `POST /api/notes`

**Request Body**:
```json
{
  "content": "Your note content here (max 300 characters)"
}
```

**Response**:
```json
{
  "success": true,
  "message": "Note created successfully",
  "data": {
    "id": 2,
    "content": "Your note content here",
    "created_at": "2025-12-06T11:58:00",
    "updated_at": "2025-12-06T11:58:00"
  }
}
```

**Status Codes**:
- `201 Created`: Note created successfully
- `400 Bad Request`: Invalid content or exceeds 300 characters

**Validation Rules**:
- Content is required
- Maximum length: 300 characters
- Content cannot be empty or whitespace only

---

### 4. Update Note

Update an existing note.

**Endpoint**: `PUT /api/notes/<note_id>`

**Parameters**:
- `note_id` (path parameter): Integer ID of the note

**Request Body**:
```json
{
  "content": "Updated note content (max 300 characters)"
}
```

**Response**:
```json
{
  "success": true,
  "message": "Note updated successfully",
  "data": {
    "id": 2,
    "content": "Updated note content",
    "created_at": "2025-12-06T11:58:00",
    "updated_at": "2025-12-06T12:00:00"
  }
}
```

**Status Codes**:
- `200 OK`: Note updated successfully
- `400 Bad Request`: Invalid content or exceeds 300 characters
- `404 Not Found`: Note doesn't exist

---

### 5. Delete Note

Delete a note by ID.

**Endpoint**: `DELETE /api/notes/<note_id>`

**Parameters**:
- `note_id` (path parameter): Integer ID of the note

**Response**:
```json
{
  "success": true,
  "message": "Note deleted successfully"
}
```

**Status Codes**:
- `200 OK`: Note deleted successfully
- `404 Not Found`: Note doesn't exist

---

## Error Response Format

All error responses follow this format:

```json
{
  "success": false,
  "error": "Error message describing what went wrong"
}
```

## Example Usage

### Using cURL

**Create a note**:
```bash
curl -X POST http://localhost:5000/api/notes \
  -H "Content-Type: application/json" \
  -d '{"content": "Meeting notes: Discuss project timeline"}'
```

**Get all notes**:
```bash
curl http://localhost:5000/api/notes
```

**Update a note**:
```bash
curl -X PUT http://localhost:5000/api/notes/1 \
  -H "Content-Type: application/json" \
  -d '{"content": "Updated: Meeting rescheduled to next week"}'
```

**Delete a note**:
```bash
curl -X DELETE http://localhost:5000/api/notes/1
```

### Using Python Requests

```python
import requests

# Base URL
base_url = "http://localhost:5000/api"

# Create a note
response = requests.post(f"{base_url}/notes", 
                        json={"content": "My new note"})
print(response.json())

# Get all notes
response = requests.get(f"{base_url}/notes")
print(response.json())

# Update a note
response = requests.put(f"{base_url}/notes/1", 
                       json={"content": "Updated content"})
print(response.json())

# Delete a note
response = requests.delete(f"{base_url}/notes/1")
print(response.json())
```

### Using JavaScript Fetch

```javascript
// Create a note
fetch('http://localhost:5000/api/notes', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({content: 'My new note'})
})
.then(response => response.json())
.then(data => console.log(data));

// Get all notes
fetch('http://localhost:5000/api/notes')
  .then(response => response.json())
  .then(data => console.log(data));
```

## Rate Limiting

Currently, there are no rate limits. For production use, consider implementing rate limiting.

## CORS

CORS is enabled for all origins in development. For production, configure specific allowed origins in `app.py`.

## Notes

- All timestamps are in ISO 8601 format
- Note IDs are auto-incrementing integers
- The API uses JSON for both requests and responses
- Content-Type header must be `application/json` for POST/PUT requests
