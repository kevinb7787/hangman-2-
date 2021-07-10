import random


def ChemicalElement():

    list_of_words = ['Tennessine', 'Flerovium', 'Roentgenium', 'Roentgenium',
                     'Thulium', 'Cadmium', 'Rubidium', 'Nitrogen', 'Ytterbium', 'Chromine ']
    word = random.choice(list_of_words)
    turns = 10
    guessmade = ''
    valid_enter = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890')

    while len(word) > 0:
        main_word = ''
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word = main_word+letter
            else:
                main_word = main_word+"_ "

        if main_word == word:
            print("the word is", main_word, "!")
            print("you won!!!!")
            break

        print("guess the word ", main_word)
        guess = input()

        if guess in valid_enter:
            guessmade = guessmade+guess
        else:
            print("enter valid character")
            guess = input()

        if guess not in word:
            turns = turns-1
        if turns == 9:
            print("9 turns left.....")
            print(" ---------  ")

        if turns == 8:
            print("8 turns left.....")
            print(" ---------  ")
            print("     O      ")

        if turns == 7:
            print("7 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")

        if turns == 6:
            print("6 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")
            print("    /       ")
        if turns == 5:
            print("5 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")
            print("    / \     ")

        if turns == 4:
            print("4 turns left.....")
            print(" ---------  ")
            print("   \ O      ")
            print("     |      ")
            print("    / \     ")
        if turns == 3:
            print("3 turns left.....")
            print(" ---------  ")
            print("   \ O /    ")
            print("     |      ")
            print("    / \     ")

        if turns == 2:
            print("2 turns left.....")
            print(" ---------  ")
            print("        |   ")
            print("   \ O /|   ")
            print("     |      ")
            print("    / \     ")
        if turns == 1:
            print("1 turns left.....")
            print("Last breaths counting, Take care :-|")
            print(" ---------  ")
            print("       |    ")
            print("   \ O_|/   ")
            print("     |      ")
            print("    / \     ")
        if turns == 0:
            print(" ---------  ")
            print("       |    ")
            print("     O_|   ")
            print("    /|\      ")
            print("    / \     ")
            print("You Loose")
            print("You let a good man die")
            print("the word was", word, "!")
            break

#  car name code start for hear
#               || 
#               ||
#               ||
#               ||
#               ||                  
#              \  /
#               \/ 

def Carname():

    list_of_words = ['Lamborghini-Diablo', 'Lamborghini-Diablo', 'Ferrari-Testarossa', 'Porsche-911-Carrera', 'Jensen-Interceptor',
                     'Lamborghini-Huracán', 'Ferrari-812-Superfast', 'Jeep-Gladiator', 'Land-Rover-Defender', 'Rolls-Royce-Wraith']
    word = random.choice(list_of_words)
    turns = 10
    guessmade = ''
    valid_enter = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890')

    while len(word) > 0:
        main_word = ''
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word = main_word+letter
            else:
                main_word = main_word+"_ "

        if main_word == word:
            print("the word is", main_word, "!")
            print("you won!!!!")
            break

        print("guess the word ", main_word)
        guess = input()

        if guess in valid_enter:
            guessmade = guessmade+guess
        else:
            print("enter valid character")
            guess = input()

        if guess not in word:
            turns = turns-1
        if turns == 9:
            print("9 turns left.....")
            print(" ---------  ")

        if turns == 8:
            print("8 turns left.....")
            print(" ---------  ")
            print("     O      ")

        if turns == 7:
            print("7 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")

        if turns == 6:
            print("6 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")
            print("    /       ")
        if turns == 5:
            print("5 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")
            print("    / \     ")

        if turns == 4:
            print("4 turns left.....")
            print(" ---------  ")
            print("   \ O      ")
            print("     |      ")
            print("    / \     ")
        if turns == 3:
            print("3 turns left.....")
            print(" ---------  ")
            print("   \ O /    ")
            print("     |      ")
            print("    / \     ")

        if turns == 2:
            print("2 turns left.....")
            print(" ---------  ")
            print("        |   ")
            print("   \ O /|   ")
            print("     |      ")
            print("    / \     ")
        if turns == 1:
            print("1 turns left.....")
            print("Last breaths counting, Take care :-|")
            print(" ---------  ")
            print("       |    ")
            print("   \ O_|/   ")
            print("     |      ")
            print("    / \     ")
        if turns == 0:
            print(" ---------  ")
            print("       |    ")
            print("     O_|   ")
            print("    /|\      ")
            print("    / \     ")
            print("You Loose")
            print("You let a good man die")
            print("the word was", word, "!")
            break

# Water animal name code start for hear
#               |
#               |
#               |
#              \ /


def Wateranimalname():

    list_of_words = ['Suropean-Sea-Sturgeon', 'Smalltooth-Sawfish', 'Kissing-loach', 'Giant-Sea-Bass', 'Tequila-Splitfin',
                     'Adriatic-Sturgeon', 'Devils-Hole-Pupfish', 'Red-handfish', 'Sakhalin-Sturgeon', 'Ornate-Sleeper-Ray']
    word = random.choice(list_of_words)
    turns = 10
    guessmade = ''
    valid_enter = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890')

    while len(word) > 0:
        main_word = ''
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word = main_word+letter
            else:
                main_word = main_word+"_ "

        if main_word == word:
            print("the word is", main_word, "!")
            print("you won!!!!")
            break

        print("guess the word ", main_word)
        guess = input()

        if guess in valid_enter:
            guessmade = guessmade+guess
        else:
            print("enter valid character")
            guess = input()

        if guess not in word:
            turns = turns-1
        if turns == 9:
            print("9 turns left.....")
            print(" ---------  ")

        if turns == 8:
            print("8 turns left.....")
            print(" ---------  ")
            print("     O      ")

        if turns == 7:
            print("7 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")

        if turns == 6:
            print("6 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")
            print("    /       ")
        if turns == 5:
            print("5 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")
            print("    / \     ")

        if turns == 4:
            print("4 turns left.....")
            print(" ---------  ")
            print("   \ O      ")
            print("     |      ")
            print("    / \     ")
        if turns == 3:
            print("3 turns left.....")
            print(" ---------  ")
            print("   \ O /    ")
            print("     |      ")
            print("    / \     ")

        if turns == 2:
            print("2 turns left.....")
            print(" ---------  ")
            print("        |   ")
            print("   \ O /|   ")
            print("     |      ")
            print("    / \     ")
        if turns == 1:
            print("1 turns left.....")
            print("Last breaths counting, Take care :-|")
            print(" ---------  ")
            print("       |    ")
            print("   \ O_|/   ")
            print("     |      ")
            print("    / \     ")
        if turns == 0:
            print(" ---------  ")
            print("       |    ")
            print("     O_|   ")
            print("    /|\      ")
            print("    / \     ")
            print("You Loose")
            print("You let a good man die")
            print("the word was", word, "!")
            break

#  Dinosaur name name code start for hear
#               || 
#               ||
#               ||
#               ||
#               ||                  
#              \  /
#               \/ 

def Dinosaurname():

    list_of_words = ['Tyrannosaurus Rex', 'Stegosaurus', 'Triceratops', 'Velociraptor',
                     'Spinosaurus', 'Allosaurus', 'Archaeopteryx', 'Megalosaurus', 'Diplodocus', 'Ankylosaurus']
    word = random.choice(list_of_words)
    turns = 10
    guessmade = ''
    valid_enter = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890')

    while len(word) > 0:
        main_word = ''
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word = main_word+letter
            else:
                main_word = main_word+"_ "

        if main_word == word:
            print("the word is", main_word, "!")
            print("you won!!!!")
            break

        print("guess the word ", main_word)
        guess = input()

        if guess in valid_enter:
            guessmade = guessmade+guess
        else:
            print("enter valid character")
            guess = input()

        if guess not in word:
            turns = turns-1
        if turns == 9:
            print("9 turns left.....")
            print(" ---------  ")

        if turns == 8:
            print("8 turns left.....")
            print(" ---------  ")
            print("     O      ")

        if turns == 7:
            print("7 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")

        if turns == 6:
            print("6 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")
            print("    /       ")
        if turns == 5:
            print("5 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")
            print("    / \     ")

        if turns == 4:
            print("4 turns left.....")
            print(" ---------  ")
            print("   \ O      ")
            print("     |      ")
            print("    / \     ")
        if turns == 3:
            print("3 turns left.....")
            print(" ---------  ")
            print("   \ O /    ")
            print("     |      ")
            print("    / \     ")

        if turns == 2:
            print("2 turns left.....")
            print(" ---------  ")
            print("        |   ")
            print("   \ O /|   ")
            print("     |      ")
            print("    / \     ")
        if turns == 1:
            print("1 turns left.....")
            print("Last breaths counting, Take care :-|")
            print(" ---------  ")
            print("       |    ")
            print("   \ O_|/   ")
            print("     |      ")
            print("    / \     ")
        if turns == 0:
            print(" ---------  ")
            print("       |    ")
            print("     O_|   ")
            print("    /|\      ")
            print("    / \     ")
            print("You Loose")
            print("You let a good man die")
            print("the word was", word, "!")
            break

#  animals name code start for hear
#               || 
#               ||
#               ||
#               ||
#               ||                  
#              \  /
#               \/ 

def animalsname():

    list_of_words = ['Amur-leopard', 'Sumatran-rhino', 'Hainan-gibbon', 'Gorilla', 'Black-eyed-leaf-frog', 'Cuban-greater-funnel-eared-bat', 'Spoon-billed-sandpiper', 'Vaquita', 'Greater-bamboo-lemur', 'Northern-Hairy-Nosed-Wombat']
    word = random.choice(list_of_words)
    turns = 10
    guessmade = ''
    valid_enter = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-1234567890')

    while len(word) > 0:
        main_word = ''
        missed = 0

        for letter in word:
            if letter in guessmade:
                main_word = main_word+letter
            else:
                main_word = main_word+"_ "

        if main_word == word:
            print("the word is", main_word, "!")
            print("you won!!!!")
            break

        print("guess the word ", main_word)
        guess = input()

        if guess in valid_enter:
            guessmade = guessmade+guess
        else:
            print("enter valid character")
            guess = input()

        if guess not in word:
            turns = turns-1
        if turns == 9:
            print("9 turns left.....")
            print(" ---------  ")

        if turns == 8:
            print("8 turns left.....")
            print(" ---------  ")
            print("     O      ")

        if turns == 7:
            print("7 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")

        if turns == 6:
            print("6 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")
            print("    /       ")
        if turns == 5:
            print("5 turns left.....")
            print(" ---------  ")
            print("     O      ")
            print("     |      ")
            print("    / \     ")

        if turns == 4:
            print("4 turns left.....")
            print(" ---------  ")
            print("   \ O      ")
            print("     |      ")
            print("    / \     ")
        if turns == 3:
            print("3 turns left.....")
            print(" ---------  ")
            print("   \ O /    ")
            print("     |      ")
            print("    / \     ")

        if turns == 2:
            print("2 turns left.....")
            print(" ---------  ")
            print("        |   ")
            print("   \ O /|   ")
            print("     |      ")
            print("    / \     ")
        if turns == 1:
            print("1 turns left.....")
            print("Last breaths counting, Take care :-|")
            print(" ---------  ")
            print("       |    ")
            print("   \ O_|/   ")
            print("     |      ")
            print("    / \     ")
        if turns == 0:
            print(" ---------  ")
            print("       |    ")
            print("     O_|   ")
            print("    /|\      ")
            print("    / \     ")
            print("You Loose")
            print("You let a good man die")
            print("the word was", word, "!")
            break



name = input("ENTER YOUR NAME ->")
print("Welcome", name, "!")
print("1. Water animal name")
print("2. Car name")
print("3. Dinosaur name")
print("4. Element")
print("5. Animal name")
print("Enter your number ")

a = int(input("                  "))
print("__________________")
if a == 1:
    Wateranimalname()
if a == 2:
    Carname()
if a == 3:
    Dinosaurname()
if a == 4:
    ChemicalElement()
if a == 5:
    animalsname()

print('----------------------')
print("for using space you can use '-'")

print("try to guess theword in less that 10 attempts")
