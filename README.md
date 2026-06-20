# Task Management Kanban Board

A comprehensive full-stack application featuring an HTML/CSS column layout, the JavaScript Drag-and-Drop API for fluid task movement, and a Python-based Flask backend to store and persist task states. Move a card across columns and the entire board state is saved server-side automatically — no manual saving required.

---

## How It Works

Tasks are rendered server-side via Jinja2 from a Python dictionary storing the three-column state. When a card is dragged and dropped into a new column, the JavaScript Drag-and-Drop API handles the DOM move, then immediately fires a `POST` request to the Flask backend with the updated board state. Python stores it in memory, ready to restore on the next page load.

---

## Built With

| Technology | Role |
|------------|------|
| Python | Backend state management and task storage |
| Flask | Server-side rendering and `/atualizar` REST endpoint |
| Jinja2 | Dynamic board and task rendering from Python data |
| JavaScript | Drag-and-Drop API, DOM manipulation, and async state sync |
| HTML/CSS | Kanban column layout, task card styling, and drag states |

---

## Project Structure

```
/
├── app.py                # Flask app with board state and /atualizar POST endpoint
└── templates/
    └── index.html        # Kanban board layout with Jinja2 loop and inline JS
```

---

## Getting Started

**1. Install dependencies**

```bash
pip install flask
```

**2. Start the server**

```bash
python app.py
```

**3. Open the board**

Navigate to `http://127.0.0.1:5000` in your browser.

---

## Board Columns

| Column | Default Tasks |
|--------|--------------|
| `TODO` | Estudar Python, Fazer café |
| `DOING` | Projeto Kanban |
| `DONE` | Blog Markdown |

---

## API Reference

**`POST /atualizar`**

Fired automatically after every drag-and-drop. Sends the full updated board state.

Request body:
```json
{
  "todo": ["Estudar Python"],
  "doing": ["Projeto Kanban"],
  "done": ["Blog Markdown", "Fazer café"]
}
```

Success response:
```json
{ "status": "sucesso" }
```

---

## Features

- Native HTML5 Drag-and-Drop API — no external libraries required
- Auto-save on every drop via async `fetch` to the Flask backend
- Full board rendered server-side with Jinja2 on every page load
- Visual drag feedback via `.dragging` opacity class during card movement
- Graceful drop targeting — accepts drops on both the task list and sibling cards
- Zero frontend dependencies — pure HTML, CSS, and vanilla JavaScript

Thank you for your attention!
