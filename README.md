# YourGPT – Personal AI Chatbot

YourGPT is a beginner-friendly, rule-based chatbot built using Python. It provides simple conversational responses and remembers basic user details even after the application is restarted.

## Features

- Responds to greetings and basic conversations.
- Recognizes user questions and provides predefined responses.
- Remembers the user's name and favourite colour.
- Stores user information using JSON.
- Provides a simple web-based chat interface.
- Uses Flask to connect the frontend with the Python chatbot.

## Technologies Used

- **Python** – Chatbot logic and response handling.
- **Flask** – Backend and API.
- **HTML** – Webpage structure.
- **CSS** – Styling and layout.
- **JavaScript** – Frontend interaction.
- **JSON** – Persistent memory storage.

## Project Structure

YourGPT/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── app.py
├── yourgpt.py
├── memory.json
└── README.md

## How to Run

1. Clone or download this repository.
2. Install Flask:
   python -m pip install flask

3. Open the project folder in VS Code.
4. Run the application:
   python app.py

5. Open `http://127.0.0.1:5000` in your browser.

## Future Improvements

- Improve chatbot response handling.
- Expand conversational capabilities.
- Enhance the user interface.

## Author

Developed as a beginner Python and web development project.