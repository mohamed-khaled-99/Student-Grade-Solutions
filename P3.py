import random
# create the list of word
words = ["arish","sinai","rafah"]
print("Welcome to the Word Scramble Game!\n")
# the program choice any word
word = random.choice(words)
# lists the word to shuffle
word_list = list(word)
# shuffle the list of word
random.shuffle(word_list)
# join a word again
scarmble_word = ''.join(word_list)
# print scramble word
print(f"Try to guess the original word from the scrambled word: {scarmble_word}\n")
print("You have 5 attempts.\n")
attempts = 5 
#  play
while attempts > 0 :
    guess = input("Enter your guess: ")
    # if guess is true print congratular 
    if guess == word :
        print("Congratulations! You guessed the correct word!")
        break
    # attempt again
    else:
        attempts -= 1 
        # show the attempts avvilable
        print(f"Incorrect! Try again. You have {attempts} attempts left.")
    # if out of attempts
    if attempts == 0 :
        print(f"You’re out of attempts! The correct word was: {word}")