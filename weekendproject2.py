import random

def choose_random_word(words):
    return random.choice(words).upper()

def display_initial_word(word):
    return '_' * len(word)

def display_current_word(correct_word, display_word):
    return '',(correct_word, display_word)

def play_hangman():
    words = ['funny', 'absurd', 'buffalo', 'jackpot', 'uptown', 'scratch']
    correct_word = choose_random_word(words)
    display_word = display_initial_word(correct_word)
    turns = 6
    guess_letters = set()

    while turns > 0:
        guess = input('Guess a letter: ').upper()

        if guess in guess_letters:
            print('Oops! You have already guessed that letter.')
            

        guess_letters.add(guess)

        if guess in correct_word:
            print('Correct! The letter is part of the word.')
            display_word = display_current_word(correct_word, display_word)
        else:
            turns -= 1
            print(f'Incorrect. {turns} turns remaining.')

        print(f'Word: {display_word}')

        if '_' not in display_word:
            print('Congratulations! You won.')
            return

    print(f'Sorry, you lost. The correct word was: {correct_word}')

# Call the main function to play the game
play_hangman()