# 🧠 QuizzMaster – Python Quiz Application

**QuizzMaster** is a simple **console-based quiz application** built using Python.  
It presents multiple-choice questions, evaluates user answers, calculates the score, and provides performance feedback.

---

## 🚀 Features

The application includes the following features:

1. 🎉 Welcome screen with app name and instructions  
2. ❓ Predefined set of multiple-choice questions  
3. ⌨️ User input using **A, B, C, or D**  
4. ✅ Correct and ❌ wrong answer validation  
5. 📊 Score calculation  
6. 📈 Display total score and percentage  
7. 🏆 Performance feedback:
   - Excellent  
   - Good Job  
   - Keep Practicing  
8. 🔁 Replay option (play again feature)

---

## 🛠️ Technologies Used

- **Language:** Python  
- **Concepts Applied:**
  - Functions
  - Lists and Dictionaries
  - Loops
  - Conditional Statements
  - User Input Handling
  - Recursion (replay feature)

---

## 📂 Project Structure

QuizzMaster/
│
├── quizzmaster.py
└── README.md

yaml
Copy code

---

## ▶️ How to Run the Project

### Prerequisites
- Python **3.x** installed

### Steps
1. Clone or download the repository
2. Open terminal / command prompt
3. Navigate to the project directory
4. Run the program:

```bash
python quizzmaster.py
📋 How the Quiz Works
The quiz displays one question at a time.

Each question has four options (A–D).

User enters the correct option letter.

Score increases for each correct answer.

At the end, total score and percentage are displayed.

The user receives performance feedback.

Option to replay the quiz is provided.

📝 Sample Question Format
python
Copy code
{
  "question": "Which keyword is used to define a function in Python?",
  "options": ["A. function", "B. def", "C. fun", "D. define"],
  "answer": "B"
}
🧠 Sample Output
yaml
Copy code
Quiz over! You Scored: 4/6
Your Percentage is: 66.67%
Good Job
⚠️ Limitations
Questions are hardcoded

No file or database storage

Console-based (no GUI)

🔮 Future Enhancements
Load questions from a file or database

Add timer for each question

Randomize question order

Add difficulty levels

Add GUI using Tkinter

👨‍💻 Author
Name: Jahid

Course: BTech CSE (AI Specialization)

Purpose: Python practice project for logic building and fundamentals

⭐ Support
If you like this project, don’t forget to give it a ⭐ on GitHub!
