import random
import hangman_words
import hangman_art

word_list = hangman_words.get_word_list()
word = random.choice(word_list)
chosen_word = word["word"]
word_hint = word["hint"]
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    if lives == 3:
        print(f'Pssst, here\'s a hint: {word_hint}.')

    guess = input("Guess a letter: ").lower()
    already_guessed = False

    if guess in display:
        print(f"You've already guessed {guess}")
        already_guessed = True

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word and already_guessed is False:
        print(f'The letter {guess} was not in the word, you lose a life')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'Pssst, the solution was {chosen_word}.')
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
