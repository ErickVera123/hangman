from words import words
import random


def get_valid_word(word):
    word = random.choice(word)
    while '-' in word or ' ' in word:
        word = random.choice(word)
    return word.upper()


def printWord(displayWord):
    word = ""
    for i in range(len(displayWord)):
        word += displayWord[i]
    print()
    print("Current Progress: ", word)


def print_man(lives):
    hangman_pics = ['''
        +---+
            |
            |
            |
          ===''', '''
        +---+
        O   |
            |
            |
           ===''', '''
        +---+
        O   |
        |   |
            |
           ===''', '''
        +---+
        O   |
       /|   |
            |
           ===''', '''
        +---+
        O   |
       /|\  |
            |
           ===''', '''
        +---+
        O   |
       /|\  |
       /    |
           ===''', '''
        +---+
        O   |
       /|\  |
       / \  |
           ===''']
    hangman_pics.reverse()
    print(hangman_pics[lives])


def hangman():
    lives = 7
    game_over = False
    word = get_valid_word(words)  # word
    display_word = ("_" * len(word))
    display_word = list(display_word)
    word = list(word)
    print("_" * len(word)) 
    print(f"You have {lives} lives") 
    
    while not game_over:
        letter = input("Choose a letter: ").upper()
        if letter in word:
            print("Your guess is correct!")
            for i in range(len(word)):
                if word[i] == letter:
                    display_word[i] = letter
            printWord(display_word)
            if "_" not in display_word:
                print("Player wins!")
                game_over = True
        else:
            lives -= 1
            print("Your guess is incorrect! Please try again.")
            print("Hangman Status: ", end="")
            print_man(lives)
            if lives == 0:
                game_over = True
                print("† You kill a man, you loser †")
            print(f"You have {lives} lives")
            printWord(display_word)
            
            
def imprimePalabra(mostrarPalabra):
    word = ""
    for i in range(len(mostrarPalabra)):
        word += mostrarPalabra[i]
    print()
    print("Progreso de la palabra: ", word)
            
def ahorcado():
    lives = 7
    game_over = False
    word = get_valid_word(words)  # word
    mostrar_palabra = ("_" * len(word))
    mostrar_palabra = list(mostrar_palabra)
    word = list(word)
    print("_" * len(word)) 
    print(f"Tienes {lives} vidas.") 
    
    while not game_over:
        letter = input("Ingresa una letra: ").upper()
        if letter in word:
            print("La letra es correcta!")
            for i in range(len(word)):
                if word[i] == letter:
                    mostrar_palabra[i] = letter
            imprimePalabra(mostrar_palabra)
            if "_" not in mostrar_palabra:
                print("Ganaste!")
                game_over = True
        else:
            lives -= 1
            print("La letra es incorrecta! Intentalo de nuevo.")
            print("Estado de ahorcado: ", end="")
            print_man(lives)
            if lives == 0:
                game_over = True
                print("Te ahorcaste!, Perdiste!")
            print(f"Tines {lives} vidas.")
            imprimePalabra(mostrar_palabra)
            
def lenguaje():
    print("Idiomas: \n1.Ingles \n2.Español") 
    opc = int(input("Seleccione idioma: "))
    
    if opc == 1:
       hangman()
    elif opc == 2:
       ahorcado()
    else:
        print("Idioma no encontrado")
     
lenguaje()