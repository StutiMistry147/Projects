import random
word_bank = ['banana', 'apple', 'kiwi', 'mango', 'strawberry', 'blueberry', 'orange', 'grape', 'peach', 'pear']
word = random.choice(word_bank)
guessedWord = ['_'] * len(word)
attempts = 10
while attempts > 0:
   
    print('\nCurrent word: ' + ' '.join(guessedWord))

    guess = input('Guess a letter: ').lower()
   
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessedWord:
        print('\nCongratulations!! You guessed the word: ' + word)
        break
    elif attempts == 0:
        print('\nGame Over! The word was: ' + word)
        break
