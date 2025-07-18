# 🧩 Hangman Game in Python – CLI & GUI Versions

A classic word-guessing game implemented in Python with two variants:
- `hangman.py`: A command-line version with smart use of data structures and logic.
- `updated_hangman_gui.py`: A GUI version developed with the help of **Claude AI** using Tkinter.

---

## 📚 Index

1. [🎮 Game Objective](#-game-objective)  
2. [🧠 Core Game Mechanics](#-core-game-mechanics)  
3. [📂 Project Files Overview](#-project-files-overview)  
4. [🔢 Data Structures Used](#-data-structures-used)  
5. [🔁 Looping & Game Flow](#-looping--game-flow)  
6. [🧑‍💻 Detailed Code Walkthrough](#-detailed-code-walkthrough)  
7. [🪟 GUI Version with Tkinter](#-gui-version-with-tkinter)  
8. [🖼️ Screenshots](#️-screenshots)  
9. [📈 Future Enhancements](#-future-enhancements)  
10. [🤝 AI Collaboration Acknowledgment](#-ai-collaboration-acknowledgment)  
11. [📝 License](#-license)  
12. [🙋‍♂️ Author](#-author)  

---

## 🎮 Game Objective

The goal is to guess a randomly selected word, one letter at a time. You lose a life with each incorrect guess. The game ends when:
- You guess all letters correctly ✅  
- You run out of lives ❌

---

## 🧠 Core Game Mechanics

- Word is randomly chosen from a list.
- First and last characters are revealed by default.
- Guessed letters are tracked and matched to reveal positions.
- A dictionary maps each character to its positions for efficient access.
- User gets limited lives to guess the word.

---

## 📂 Project Files Overview

| File Name               | Description                                       |
|-------------------------|---------------------------------------------------|
| `hangman.py`            | Command-line version of the game                  |
| `updated_hangman.py`| GUI version on Terminal (with help from Claude AI) |
| `updated_hangman_gui.py`| GUI version using Tkinter (with help from Claude AI) |

---

## 🔢 Data Structures Used

| Data Structure   | Purpose                                                  |
|------------------|----------------------------------------------------------|
| `list`           | `guessed_letters` to store indices of revealed letters  |
| `dict`           | `word_dict` maps character → list of its positions       |
| `int`            | `lives` to keep count of remaining chances               |
| `str`            | The word to be guessed                                   |

---

## 🔁 Looping & Game Flow

Main game loop in `hangman.py`:

```python
while lives > 0 and len(guessed_letters) < len(word):
```

- **Runs Until**:
  - All letter indices are guessed, or
  - Lives reach 0

### Guess Evaluation:

```python
if word_dict.get(user_guess):
    guessed_letters.append(word_dict[user_guess].pop(0))
    if not word_dict[user_guess]:
        del word_dict[user_guess]
```

- **Correct Guess**:
  - Position is added to `guessed_letters`
  - Index removed from `word_dict`
- **Incorrect Guess**:
  - `lives -= 1`

---

## 🧑‍💻 Detailed Code Walkthrough

### 1. **Word Selection**
```python
word = random.choice(word_list)
```

### 2. **Building the Word Dictionary**
```python
word_dict = {}
for i in range(len(word)):
    word_dict.setdefault(word[i], []).append(i)
```

### 3. **User Guess Checking**
```python
if word_dict.get(user_guess):
    guessed_letters.append(word_dict[user_guess].pop(0))
    if not word_dict[user_guess]:
        del word_dict[user_guess]
```

### 4. **Display Function**
```python
for i in range(len(word)):
    print(word[i] if i in guessed_letters else "_", end="")
```

> ✅ Efficient: avoids full string rebuilds and uses simple index checks.

---

## 🪟 GUI Version with Tkinter

After completing the CLI version, I extended this into a **Tkinter GUI** version with the help of **Claude AI**.

### GUI Features:
Create a fully interactive graphical Hangman game where:
- A random word is selected.
- The user guesses one letter at a time.
- The UI displays a hangman drawing that progresses with each wrong guess.
- The player wins or loses based on the number of incorrect attempts.

### 🧠 Core Game Mechanics (GUI Version):
Object-Oriented Programming (OOP): The game is structured as a class HangmanGame.

Encapsulation: Game state is wrapped inside methods and instance variables.

GUI programming: Built using tkinter with event-driven callbacks.

String processing: Used for word display logic (_ vs letter reveal).

Control Flow: Managed using if-else conditions and set logic.

Modularity: Methods like update_display, guess_letter, check_game_over.

### 🧱 GUI Components Breakdown

| Component   | Description                                                 |
|------------------|----------------------------------------------------------|
| `tk.Label`           | Used for title, word hints, status messages  |
| `tk.Entry`           | For letter input       |
| `tk.Text`            | For ASCII-style hangman drawing               |
| `tk.Button`            | Guess, New Game, Quit controls                                  |
| `tk.Frame`            | Used to organize layout sections (left, right, bottom)                               |
| `tk.StringVar`            | Dynamically trace the letter input                                   |




> 💡 The GUI maintains the same core logic as the CLI version but integrates it into a visual interface using Tkinter's widgets and event handlers.

---

## 🖼️ Screenshots

 ### 🖥️ CLI Version  
<img width="910" height="533" alt="image" src="https://github.com/user-attachments/assets/12ecf61c-a406-4f36-882e-3f9b1fa7895c" />
<img width="879" height="554" alt="image" src="https://github.com/user-attachments/assets/67d299a7-c8db-4760-bd16-83e6982b8092" />

### 🔥 GUI Version  
<img width="799" height="628" alt="image" src="https://github.com/user-attachments/assets/29c42517-83a4-4466-8c47-3b9d0a831885" />
<img width="798" height="624" alt="image" src="https://github.com/user-attachments/assets/f018de2c-ac13-404b-89e5-8f9c7cd850f3" />
<img width="800" height="623" alt="image" src="https://github.com/user-attachments/assets/45b93c2e-744a-4994-b011-9ff545513d2e" />

---

## 📈 Future Enhancements

- Add difficulty levels (Easy / Medium / Hard)
- Include hints or word definitions
- Add audio cues on win/loss
- GUI theming options
- Scoreboard or leaderboard support

---

## 🤝 AI Collaboration Acknowledgment

The **command-line version** (`hangman.py`) was written by me from scratch, focusing on clean, modular code and optimal data handling.

For the **GUI version** (`updated_hangman_gui.py`), I collaborated with **Claude AI**, who assisted in building the Tkinter interface and binding UI logic with the game backend.

---

## 📝 License

This project is licensed under the [MIT License](LICENSE)

---

## 🙋‍♂️ Author

Made with ❤️ by **SURYANATH TRIPATHY** 🤞 
Feel free to connect, fork, or build upon this!

---

Happy Coding & Game On! 🎮🐍
