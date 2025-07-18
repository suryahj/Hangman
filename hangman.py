import random

word_list=[
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

def choose_word(word_list):
    word=random.choice(word_list)
    return (word,len(word))

def display_word(word,len_word,lives,guesed_letters):
    print("############################################################################################################")
    print(f"number of lives left {lives}")
    for i in range(0,len_word):
        if i in guesed_letters:
            print(word[i],end="")
        else:
            print("_",end="")
    print("\n############################################################################################################")

def check_guess(word_dict,guesed_letters):
    user_guess=input("\n\nenter your guessed letter - ")
    if word_dict.get(user_guess,None)!=None:
        guesed_letters.append(word_dict[user_guess].pop(0))
        if len(word_dict[user_guess])==0:
            del word_dict[user_guess]
        return True
    else:
        return False
        


if __name__=="__main__":
    word,len_word=choose_word(word_list)
    print(word,len_word)
    lives=len_word-2
    guesed_letters=[0,len_word-1]

    word_dict={}
    for i in range(0,len_word):
        if word_dict.get(word[i],None)!=None:
            word_dict[word[i]].append(i)
        else:
            word_dict[word[i]]=[i]

    display_word(word,len_word,lives,guesed_letters)
    while lives>0 and len(guesed_letters)<len_word:
        if check_guess(word_dict,guesed_letters):
            print("Its a correct choice keep it up")
            display_word(word,len_word,lives,guesed_letters)
        else:
            print("woring guess lives decreased by 1")
            print (f"total lives left {lives-1}")
            lives=lives-1
            display_word(word,len_word,lives,guesed_letters)

    if len(guesed_letters)==len_word:
        print("\n\n ****************************YOU ARE THE WINNER CONGRATS **************************************")
    else:
        print("\n\n !!!!!!!!!!!!!!!!!!!!!!!!!!!!GAME OVER YOU LOOSE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")