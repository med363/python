import random
name = input("Enter your name: ")
words = ["hangman","programming","python","binod","codesnail",]
word = random.choice(words) //il pc hya ili ta5tar mort a partir les morts ili mawjoudin
print("Guess the characters")
guesses = ""
turns = 12 //12 fois

while turns > 0: //maazal 3andy chnce nzid na5tar guesses o5ra
    failed= 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed +=1
    if failed == 0:
        print("you win")
        print("the word is: ",word) 
        break
    guess = input ("guess the character: ")
    guesses += guess

    if guess not in word:
        turns-= 1
        print("wrong")
        print("u have", +turns,"more guesses")

        if turns == 0:
            print("u lose")  