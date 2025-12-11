# Notes Sharing Web App

A simple and elegant web application for creating, editing, and sharing notes with a 300-character limit.

## Features

- **Create Notes**: Add new notes with up to 300 characters
- **Edit Notes**: Modify existing notes
- **Delete Notes**: Remove notes you no longer need
- **RESTful API**: Full API support for integration with other applications

## Design Patterns

This project implements two software design patterns:

1. **Singleton Pattern**: Ensures only one instance of the NotesManager exists throughout the application lifecycle
2. **Facade Pattern**: Provides a simplified interface to the complex note management system through the NotesService class

## Project Structure

```
notes-webapp/
├── app.py                 # Main Flask application
├── models/
│   └── notes_manager.py   # Singleton pattern - Notes storage manager
├── services/
│   └── notes_service.py   # Facade pattern - Simplified service interface
├── static/
│   ├── style.css         # Frontend styling
│   └── script.js         # Frontend JavaScript
├── templates/
│   └── index.html        # Main HTML page
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── API.md                # API documentation
```

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd notes-webapp
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## API Usage

See [API.md](API.md) for complete API documentation.

## Quick API Examples

### Create a Note
```bash
curl -X POST http://localhost:5000/api/notes \
  -H "Content-Type: application/json" \
  -d '{"content": "My first note"}'
```

### Get All Notes
```bash
curl http://localhost:5000/api/notes
```

### Update a Note
```bash
curl -X PUT http://localhost:5000/api/notes/1 \
  -H "Content-Type: application/json" \
  -d '{"content": "Updated note content"}'
```

### Delete a Note
```bash
curl -X DELETE http://localhost:5000/api/notes/1
```

## Configuration

- **Maximum Note Length**: 300 characters (configurable in `services/notes_service.py`)
- **Port**: 5000 (configurable in `app.py`)

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **API**: RESTful architecture with JSON responses

## License

MIT License - feel free to use this project for learning and development.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.
