# 🎲 Number Guessing Game

A fun, interactive command-line interface (CLI) game developed to practice fundamental Python concepts such as loops, conditionals, and error handling.

## 🎯 Objective
The computer selects a random number between **1 and 100**. Your goal is to guess the correct number within **5 attempts**. The game will guide you with "Higher" or "Lower" hints after each guess.

## 🚀 Features
* **Random Number Generation:** Uses Python's `random` module to ensure a unique number every game.
* **Lives System:** Adds difficulty by limiting the player to 5 attempts.
* **Smart Hints:** Provides feedback (Go Higher / Go Lower) to help the player narrow down the logic.
* **Input Validation:** Robust `try-except` blocks prevent the game from crashing if non-numeric values are entered.
* **Replayability:** Includes a game loop allowing the user to play again without restarting the program.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Key Concepts:** `while` Loops, Conditional Logic (`if-elif-else`), Error Handling (`try-except`)

## 💻 How to Run
1. Ensure Python 3 is installed on your machine.
2. Navigate to the project directory in your terminal.
3. Run the following command:

```bash
python GuessTheNumber.py