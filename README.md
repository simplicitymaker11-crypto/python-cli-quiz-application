🧠 CLI Quiz Application (Python)

A professional Command Line Interface (CLI) Quiz Application built using Python.
This project demonstrates object-oriented programming, modular structure, input validation, category management, scoring system, and JSON-based question storage.

📌 Features

✅ Multiple Categories
✅ JSON-based question storage
✅ Difficulty-based scoring system
✅ Input validation (no crashes)
✅ Clean CLI interaction
✅ Category selection menu
✅ Exit anytime option
✅ Repeat quiz option
✅ Error handling (file + JSON errors)

🗂 Project Structure
quiz-app/
│
├── main.py
├── quiz_maintenance.py
├── question.py
├── utils.py
│
├── general_knowledge.json
├── math.json
├── physics.json
├── chemistry.json
├── biology.json
├── computer.json
├── islamic.json
├── politics.json
│
└── README.md
🧩 How It Works
1️⃣ Category Selection (main.py)

Displays available categories.

User selects category by number.

Validates user input.

Loads selected JSON file.

Creates Question objects.

Passes them to Quiz class.

2️⃣ Question Model (question.py)

The Question class handles:

Storing question text

Storing options

Storing correct answer

Assigning points based on difficulty

Checking correctness

Difficulty → Points Mapping
Difficulty	Points
Easy	1
Medium	3
Hard	5
3️⃣ Quiz Logic (quiz_maintenance.py)

The Quiz class manages:

Looping through questions

Displaying questions

Input validation

Exit during quiz (press 0)

Score calculation

Final result display

Repeat or Exit option

4️⃣ JSON Question Format

Each category file must follow this structure:

{
  "questions": [
    {
      "question": "What is 2 + 2?",
      "options": ["3", "4", "5", "6"],
      "answer": 2,
      "difficulty": "easy"
    }
  ]
}
Important:

answer must match option number (starting from 1)

difficulty must be: "easy", "medium", or "hard"

▶️ How to Run

Make sure Python is installed.

Navigate to project directory.

Run:

python main.py
🛡 Error Handling Included

The app safely handles:

Invalid input (letters instead of numbers)

Empty input

Out-of-range selection

Missing JSON file

Invalid JSON format

Empty question file

No crashes. Clean CLI experience.

🎯 Learning Concepts Covered

Object-Oriented Programming (OOP)

Classes & Methods

Exception Handling

JSON File Handling

Modular Programming

Input Validation

Control Flow

Loops & Conditionals

Clean CLI Design

🚀 Future Improvements (Optional Ideas)

Randomize question order

Add timer per question

Add leaderboard system

Add user profiles

Add difficulty filter

Store high scores in file

Convert to GUI (Tkinter / PyQt)

Convert to Web App (Flask / Django)

👨‍💻 Author

Built as a structured learning project to practice Python fundamentals and application design.

📜 License

Free to use and modify for learning purposes.