

import random
import hangman_words
import hangman_art

word_list= hangman_words.word_list1
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6




print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')


display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    already_guessed = False
    if guess in display:
      print(f"You've already guessed {guess}")
      already_guessed = True

    
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    
    if guess not in chosen_word and already_guessed==False:
        print(f'The letter {guess} was not in the word, you lose a life')
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'Pssst, the solution is {chosen_word}.')
   
    print(f"{' '.join(display)}")

   
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
