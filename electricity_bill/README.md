# ⚡ Electricity Bill Generator (Python)

A simple **console-based Electricity Bill Generator** built using Python.  
This program calculates the electricity bill based on the number of units consumed using slab-wise pricing.

---

## 🚀 Features

- Takes **electricity units** as user input
- Calculates bill using **slab-based tariff**
- Displays total electricity bill
- Simple and beginner-friendly logic

---

## 🧮 Billing Slabs

| Units Consumed | Rate per Unit |
|---------------|---------------|
| 0 – 100       | ₹5            |
| 101 – 200     | ₹7            |
| 201 – 300     | ₹10           |
| 301+          | ₹15           |

---

## 🛠️ Technologies Used

- **Language:** Python  
- **Concepts Used:**
  - Functions
  - Conditional Statements (`if-elif-else`)
  - User Input
  - Arithmetic Operations

---

## 📂 Project Structure

Electricity_Bill_Generator/
│
├── electricity_bill_generator.py
└── README.md

yaml
Copy code

---

## ▶️ How to Run the Program

### Prerequisites
- Python **3.x** installed on your system

### Steps
1. Clone or download the repository
2. Open terminal / command prompt
3. Navigate to the project folder
4. Run the program:

```bash
python electricity_bill_generator.py
📝 Example Calculation
Input:
nginx
Copy code
Enter no of units: 105
Calculation:
First 100 units → 100 × 5 = 500

Remaining 5 units → 5 × 7 = 35

Output:
bash
Copy code
Your total bill is 105 - 535 /-
🧠 How It Works
The program uses a function billGenerator(units)

It applies tariff rates based on the slab the units fall into

Returns the total calculated bill

Final bill is displayed to the user

⚠️ Limitations
No input validation for negative values

No file or database storage

Console-based only

🔮 Future Enhancements
Add input validation

Add monthly bill history

Export bill as a file

Add GUI using Tkinter

Support dynamic tariff rates

👨‍💻 Author
Name: Jahid

Course: BTech CSE (AI Specialization)

Purpose: Python mini project for practicing functions and conditionals

⭐ Support
If you found this project useful, give it a ⭐ on GitHub!
