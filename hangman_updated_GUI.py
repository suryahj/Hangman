import tkinter as tk
from tkinter import messagebox, font
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Hangman Game")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        self.root.resizable(False, False)
        
        # Game variables
        self.word_list = [
            "apple", "brave", "cloud", "dragon", "elephant", "forest", "guitar", "horizon", 
            "island", "jungle", "kitchen", "lemon", "mountain", "ocean", "purple", "quiet", 
            "river", "sunset", "thunder", "umbrella", "village", "window", "yellow", "zebra",
            "adventure", "bicycle", "candle", "dolphin", "energy", "feather", "garden", "harmony",
            "imagination", "journey", "kindness", "lighthouse", "melody", "notebook", "opportunity", "peaceful",
            "question", "rainbow", "strawberry", "telescope", "universe", "vacation", "wisdom", "xylophone",
            "yesterday", "zephyr", "ancient", "butterfly", "crystal", "detective", "emerald", "fountain",
            "galaxy", "happiness", "invisible", "jewel", "knowledge", "language", "mystery", "nightfall",
            "orchestra", "painting", "quicksand", "reflection", "sculpture", "tornado", "underwater", "volcano",
            "waterfall", "xerosis", "yearning", "zenith", "balloon", "cemetery", "diamond", "eclipse",
            "festival", "glacier", "hurricane", "iceberg", "jackpot", "kaleidoscope", "labyrinth", "monument",
            "nebula", "oasis", "pyramid", "quasar", "raccoon", "sandstorm", "treasure", "ultraviolet",
            "vineyard", "wilderness", "xenophobia", "yonder", "zigzag", "asteroid", "blizzard", "constellation",
            "dragonfly", "earthquake", "firefly", "grasshopper", "hedgehog", "icicle", "jellyfish"
        ]
        
        self.hangman_stages = [
            "",  # 0 wrong guesses
            "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",  # 1
            "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",  # 2
            "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",  # 3
            "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",  # 4
            "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",  # 5
            "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",  # 6
            "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="   # 7 (game over)
        ]
        
        self.reset_game()
        self.create_widgets()
        self.new_game()
    
    def reset_game(self):
        """Reset game variables"""
        self.word = ""
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong_guesses = 6
        self.game_over = False
        self.won = False
    
    def create_widgets(self):
        """Create and arrange GUI widgets"""
        # Title
        title_font = font.Font(family="Arial", size=24, weight="bold")
        title_label = tk.Label(self.root, text="🎮 HANGMAN GAME 🎮", 
                              font=title_font, fg='#e74c3c', bg='#2c3e50')
        title_label.pack(pady=20)
        
        # Main game frame
        main_frame = tk.Frame(self.root, bg='#2c3e50')
        main_frame.pack(expand=True, fill='both', padx=20, pady=10)
        
        # Left side - Hangman drawing
        left_frame = tk.Frame(main_frame, bg='#34495e', relief='raised', bd=2)
        left_frame.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        hangman_title = tk.Label(left_frame, text="Hangman", 
                                font=('Arial', 16, 'bold'), fg='#ecf0f1', bg='#34495e')
        hangman_title.pack(pady=10)
        
        self.hangman_canvas = tk.Text(left_frame, height=10, width=25, 
                                     font=('Courier', 12), bg='#2c3e50', fg='#e74c3c',
                                     state='disabled', relief='sunken', bd=2)
        self.hangman_canvas.pack(pady=10, padx=10)
        
        # Right side - Game info
        right_frame = tk.Frame(main_frame, bg='#34495e', relief='raised', bd=2)
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        # Game stats
        stats_frame = tk.Frame(right_frame, bg='#34495e')
        stats_frame.pack(pady=10, padx=10, fill='x')
        
        self.lives_label = tk.Label(stats_frame, text="Lives: 6", 
                                   font=('Arial', 14, 'bold'), fg='#27ae60', bg='#34495e')
        self.lives_label.pack(anchor='w')
        
        self.word_length_label = tk.Label(stats_frame, text="Word Length: 0", 
                                         font=('Arial', 12), fg='#3498db', bg='#34495e')
        self.word_length_label.pack(anchor='w')
        
        # Word display
        word_frame = tk.Frame(right_frame, bg='#34495e')
        word_frame.pack(pady=20, padx=10, fill='x')
        
        tk.Label(word_frame, text="Word:", font=('Arial', 14, 'bold'), 
                fg='#ecf0f1', bg='#34495e').pack(anchor='w')
        
        self.word_display = tk.Label(word_frame, text="", font=('Arial', 20, 'bold'), 
                                    fg='#f39c12', bg='#34495e', wraplength=300)
        self.word_display.pack(pady=10)
        
        # Wrong letters
        wrong_frame = tk.Frame(right_frame, bg='#34495e')
        wrong_frame.pack(pady=10, padx=10, fill='x')
        
        tk.Label(wrong_frame, text="Wrong Letters:", font=('Arial', 12, 'bold'), 
                fg='#ecf0f1', bg='#34495e').pack(anchor='w')
        
        self.wrong_letters_display = tk.Label(wrong_frame, text="None", 
                                             font=('Arial', 12), fg='#e74c3c', bg='#34495e')
        self.wrong_letters_display.pack(anchor='w')
        
        # Input section
        input_frame = tk.Frame(self.root, bg='#2c3e50')
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Enter a letter:", font=('Arial', 14), 
                fg='#ecf0f1', bg='#2c3e50').pack()
        
        self.entry_var = tk.StringVar()
        self.entry_var.trace('w', self.on_entry_change)
        
        self.letter_entry = tk.Entry(input_frame, textvariable=self.entry_var, 
                                    font=('Arial', 16), width=5, justify='center')
        self.letter_entry.pack(pady=10)
        self.letter_entry.bind('<Return>', self.guess_letter)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg='#2c3e50')
        button_frame.pack(pady=10)
        
        self.guess_button = tk.Button(button_frame, text="Guess Letter", 
                                     command=self.guess_letter, font=('Arial', 12, 'bold'),
                                     bg='#3498db', fg='white', padx=20, pady=5)
        self.guess_button.pack(side='left', padx=10)
        
        self.new_game_button = tk.Button(button_frame, text="New Game", 
                                        command=self.new_game, font=('Arial', 12, 'bold'),
                                        bg='#27ae60', fg='white', padx=20, pady=5)
        self.new_game_button.pack(side='left', padx=10)
        
        self.quit_button = tk.Button(button_frame, text="Quit", 
                                    command=self.root.quit, font=('Arial', 12, 'bold'),
                                    bg='#e74c3c', fg='white', padx=20, pady=5)
        self.quit_button.pack(side='left', padx=10)
        
        # Status bar
        self.status_label = tk.Label(self.root, text="Welcome to Hangman! Guess a letter to start.", 
                                    font=('Arial', 12), fg='#ecf0f1', bg='#34495e', relief='sunken')
        self.status_label.pack(side='bottom', fill='x', pady=5)
    
    def on_entry_change(self, *args):
        """Limit entry to single letter and convert to uppercase"""
        value = self.entry_var.get().upper()
        if len(value) > 1:
            self.entry_var.set(value[0])
        elif len(value) == 1 and not value.isalpha():
            self.entry_var.set("")
    
    def new_game(self):
        """Start a new game"""
        self.reset_game()
        self.word = random.choice(self.word_list).upper()
        self.update_display()
        self.letter_entry.focus_set()
        self.status_label.config(text="New game started! Guess a letter.", fg='#27ae60')
    
    def update_display(self):
        """Update all display elements"""
        # Update hangman drawing
        self.hangman_canvas.config(state='normal')
        self.hangman_canvas.delete(1.0, tk.END)
        self.hangman_canvas.insert(tk.END, self.hangman_stages[self.wrong_guesses])
        self.hangman_canvas.config(state='disabled')
        
        # Update lives
        lives_left = self.max_wrong_guesses - self.wrong_guesses
        color = '#27ae60' if lives_left > 2 else '#e74c3c'
        self.lives_label.config(text=f"Lives: {lives_left}", fg=color)
        
        # Update word length
        self.word_length_label.config(text=f"Word Length: {len(self.word)}")
        
        # Update word display
        display_word = ""
        for i, letter in enumerate(self.word):
            if i == 0 or i == len(self.word) - 1 or letter in self.guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        self.word_display.config(text=display_word.strip())
        
        # Update wrong letters
        wrong_letters = sorted([letter for letter in self.guessed_letters if letter not in self.word])
        if wrong_letters:
            self.wrong_letters_display.config(text=" ".join(wrong_letters))
        else:
            self.wrong_letters_display.config(text="None")
    
    def guess_letter(self, event=None):
        """Process a letter guess"""
        if self.game_over:
            return
        
        letter = self.entry_var.get().upper()
        
        if not letter:
            self.status_label.config(text="Please enter a letter!", fg='#e74c3c')
            return
        
        if letter in self.guessed_letters:
            self.status_label.config(text=f"You already guessed '{letter}'!", fg='#f39c12')
            return
        
        self.guessed_letters.add(letter)
        self.entry_var.set("")
        
        if letter in self.word:
            self.status_label.config(text=f"Good guess! '{letter}' is in the word.", fg='#27ae60')
        else:
            self.wrong_guesses += 1
            self.status_label.config(text=f"Sorry, '{letter}' is not in the word.", fg='#e74c3c')
        
        self.update_display()
        self.check_game_over()
    
    def check_game_over(self):
        """Check if the game is over"""
        # Check if word is complete (excluding first and last letters which are always shown)
        word_complete = all(letter in self.guessed_letters for letter in self.word[1:-1])
        
        if word_complete:
            self.game_over = True
            self.won = True
            messagebox.showinfo("Congratulations!", f"🎉 You won! 🎉\nThe word was: {self.word}")
            self.status_label.config(text="You won! Click 'New Game' to play again.", fg='#27ae60')
        
        elif self.wrong_guesses >= self.max_wrong_guesses:
            self.game_over = True
            self.won = False
            messagebox.showinfo("Game Over", f"💀 Game Over! 💀\nThe word was: {self.word}")
            self.status_label.config(text="Game over! Click 'New Game' to try again.", fg='#e74c3c')

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()