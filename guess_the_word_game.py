import random
WORD=('rajkumar','veena','kishori','vandana','komal','prince','nisha','vineet','garv','aman','shubham','janhavi')
word=random.choice(WORD)
correct=word
clue=word[0]+word[(len(word)-1):(len(word))]
letter_guess=' '
word_guess=' '
store_letter=' '
count=0
limit=5
print('Welcome to "Guess the Word Game!"')
print('You have 5 attempts at guessing letters in a word')
print('Let\'s begin!')
print('\n')

while count<limit:
    letter_guess=input('Guess the letter:')

    if letter_guess in word:
        print('yes!')
        store_letter+=letter_guess
        count+=1

    if letter_guess not in word:
        print('no!')
        count+=1

    if count==2:
        print('\n')
        clue_request=input('Would you like a clue?')
        if clue_request== 'yes':
            print('\n')
            print('CLUE: The first and last letter of the word is:',clue)
        if clue_request=='no':
            print('You\'re very brave!')

print('\n')
print('Now its time to guess.You have guessed',len(store_letter),'letters correctly.')
print('These letters are:',store_letter)
word_guess=input('Guess the whole word: ')
while word_guess:
    if word_guess.lower()==correct:
        print('\n')
        print('Congrats!')
        print('Woww! You correctly guessed the word')
        break
    elif word_guess.lower()!=correct:
        print('\n')
        print('Unlucky! The answer was,',word)
        print('You lose....... Better luck next time.')
        break

print('\n')
input('Press Enter to leave the program')
