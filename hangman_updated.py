import random
import os
import time

# ANSI color codes for better visual appeal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

word_list = [
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

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_hangman(wrong_guesses):
    """Draw the hangman based on number of wrong guesses"""
    stages = [
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |     
           -
        """
    ]
    
    if wrong_guesses < len(stages):
        return Colors.RED + stages[wrong_guesses] + Colors.END
    else:
        return Colors.RED + stages[-1] + Colors.END

def print_title():
    """Print an attractive title"""
    title = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║        🎮 WELCOME TO THE ENHANCED HANGMAN GAME! 🎮            ║
    ║                                                               ║
    ║        Guess the word letter by letter to save the man!       ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """
    print(Colors.CYAN + Colors.BOLD + title + Colors.END)

def choose_word(word_list):
    word = random.choice(word_list)
    return (word.upper(), len(word))

def display_game_state(word, len_word, lives, guessed_letters, wrong_letters, wrong_guesses):
    clear_screen()
    print_title()
    
    # Draw hangman
    print(draw_hangman(wrong_guesses))
    
    # Game stats
    print(f"\n{Colors.YELLOW}═══════════════════════════════════════════════════════════════{Colors.END}")
    print(f"{Colors.BOLD}Lives remaining: {Colors.GREEN if lives > 3 else Colors.RED}{lives}{Colors.END}")
    print(f"{Colors.BOLD}Word length: {Colors.BLUE}{len_word}{Colors.END}")
    print(f"{Colors.YELLOW}═══════════════════════════════════════════════════════════════{Colors.END}")
    
    # Display word with guessed letters
    print(f"\n{Colors.BOLD}Word: {Colors.END}", end="")
    for i in range(len_word):
        if i in guessed_letters:
            print(f"{Colors.GREEN}{Colors.BOLD}{word[i]}{Colors.END}", end=" ")
        else:
            print(f"{Colors.WHITE}_{Colors.END}", end=" ")
    print()
    
    # Display wrong letters
    if wrong_letters:
        print(f"\n{Colors.RED}Wrong letters: {' '.join(wrong_letters)}{Colors.END}")
    else:
        print(f"\n{Colors.MAGENTA}No wrong letters yet!{Colors.END}")
    
    print(f"\n{Colors.YELLOW}═══════════════════════════════════════════════════════════════{Colors.END}")

def get_user_guess(guessed_all_letters):
    """Get user input with validation"""
    while True:
        user_guess = input(f"\n{Colors.CYAN}Enter your guess (letter): {Colors.END}").upper().strip()
        
        if len(user_guess) != 1:
            print(f"{Colors.RED}Please enter only one letter!{Colors.END}")
            continue
        
        if not user_guess.isalpha():
            print(f"{Colors.RED}Please enter only letters!{Colors.END}")
            continue
        
        if user_guess in guessed_all_letters:
            print(f"{Colors.YELLOW}You already guessed '{user_guess}'! Try a different letter.{Colors.END}")
            continue
        
        return user_guess

def check_guess(word_dict, guessed_letters, letter, wrong_letters):
    """Check if the guessed letter is in the word"""
    if letter in word_dict:
        # Add all positions of this letter to guessed_letters
        while word_dict[letter]:
            guessed_letters.append(word_dict[letter].pop(0))
        del word_dict[letter]
        return True
    else:
        wrong_letters.append(letter)
        return False

def play_again():
    """Ask if player wants to play again"""
    while True:
        choice = input(f"\n{Colors.CYAN}Do you want to play again? (y/n): {Colors.END}").lower().strip()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print(f"{Colors.RED}Please enter 'y' for yes or 'n' for no{Colors.END}")

def main():
    """Main game loop"""
    print(f"{Colors.MAGENTA}Loading game...{Colors.END}")
    time.sleep(1)
    
    while True:
        # Initialize game
        word, len_word = choose_word(word_list)
        max_wrong_guesses = 6
        lives = max_wrong_guesses
        guessed_letters = [0, len_word - 1]  # Show first and last letters
        wrong_letters = []
        guessed_all_letters = set()
        wrong_guesses = 0
        
        # Create word dictionary
        word_dict = {}
        for i in range(len_word):
            if word[i] in word_dict:
                word_dict[word[i]].append(i)
            else:
                word_dict[word[i]] = [i]
        
        # Remove first and last letters from word_dict since they're already revealed
        if word[0] in word_dict:
            word_dict[word[0]].remove(0)
            if not word_dict[word[0]]:
                del word_dict[word[0]]
        
        if word[-1] in word_dict:
            word_dict[word[-1]].remove(len_word - 1)
            if not word_dict[word[-1]]:
                del word_dict[word[-1]]
        
        # Game loop
        while lives > 0 and len(guessed_letters) < len_word:
            display_game_state(word, len_word, lives, guessed_letters, wrong_letters, wrong_guesses)
            
            user_guess = get_user_guess(guessed_all_letters)
            guessed_all_letters.add(user_guess)
            
            if check_guess(word_dict, guessed_letters, user_guess, wrong_letters):
                print(f"{Colors.GREEN}✓ Correct! Great job!{Colors.END}")
                time.sleep(1)
            else:
                print(f"{Colors.RED}✗ Wrong guess! Be careful!{Colors.END}")
                lives -= 1
                wrong_guesses += 1
                time.sleep(1)
        
        # Final display
        display_game_state(word, len_word, lives, guessed_letters, wrong_letters, wrong_guesses)
        
        # Game over messages
        if len(guessed_letters) == len_word:
            print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 CONGRATULATIONS! YOU WON! 🎉{Colors.END}")
            print(f"{Colors.GREEN}You successfully guessed the word: {Colors.BOLD}{word}{Colors.END}")
        else:
            print(f"\n{Colors.RED}{Colors.BOLD}💀 GAME OVER! YOU LOST! 💀{Colors.END}")
            print(f"{Colors.RED}The word was: {Colors.BOLD}{word}{Colors.END}")
        
        if not play_again():
            break
    
    print(f"\n{Colors.CYAN}Thanks for playing! Goodbye! 👋{Colors.END}")

if __name__ == "__main__":
    main()