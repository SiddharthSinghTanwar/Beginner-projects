"""
Similar to "What's the Number?", this name focuses on the user having to guess the randomly generated word. 
You can create a list from which the word would have to be guessed and also set a cap on the number of guesses allowed.
After this, you can create the rules yourself! 
When the user inputs the word, you can indicate whether the alphabet written appears in this particular position or not.
You will need a function to check if the user is inputting alphabets or numbers and to display error messages appropriately. 
"""
import random

wordList = ["embarrassment", "psychology", "money", "spiritual", "processing", "endeavour", "macroeconomics", "introduction", "algorithm", "watermelon"]

word = random.choice(wordList)

print("Guess the word!")

vowel = "aeiou"

holder = []

for letter in word:
    if letter not in vowel:
        holder.append('_')
    else:
        holder.append(letter)
        

def progress():
    print(" ".join(holder))

progress()

while True:
    guess = input("Guess letter: ").lower()[0]
    for i in range(len(word)):
        if guess == word[i]:
            holder[i] = guess

        
    progress()
    
    if "".join(holder) == word:
        print("You Guessed it!")
        quit()








