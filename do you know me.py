import random

# the question/answer dictionary.
my_dict = {
    "What is my first name:": "Gift",
    "Where do I live(county):": "Mombasa",
    "Which HighSchool do I go to": "Makueni Boys",
    "How old am I:": "18",
    "Which form am I": "4",
    "What do I love the most in this world": "Computers",
    "Do you think I love you": "Yes",
    "Which primary school did I go to": "Brights Academy",
    "Am I tall": "Yes",
    "Am I dark or light skinned": "Dark",
    "Do you love my game": "Yes",
    "What is my favorite colour": "Black"
}
# the questions
name = input("What is your name?\n")
print("Do you think you know me well? " + name + "!\n")
print("Lets see! Answer all these questions about me correctly. \n"
      "=============================================================")
print("0 = You're a stranger.\n"
      "1 = Really!!!\n"
      "2 = And you claim to know me..\n"
      "3 = We need to hang out more\n"
      "4 = You know me alright.\n"
      "5 = Meet me for pizza.. " + name + "\n")
print("Note: There are 12 questions in total \n     "
      "HAVE FUN!\n    "
      "***********\n")
playing = True
# the quiz will end when this variable becomes 'False'
while playing:
    # set score to 0 initially
    score = 0

    # gets the number of questions the player wants to answer
    num = int(input("\nHow many questions would you like: \n"))

    # loop the correct number of times
    for i in range(num):
        # the question is one of the dictionary keys, picked at random
        question = (random.choice(list(my_dict.keys())))
        # the answer is the string mapped to the question key
        answer = my_dict[question]
        # print the question, along with the question number
        print("\nQuestion " + str(i + 1))
        print(question + "? ")
        # get the user's answer attempt
        guess = input("> ")

        # if their guess is the same as the answer
        if guess.lower() == answer.lower():
            # add 1 to the score and print a message
            print("Correct! ")
            score += 1
        else:
            print(" Nope! " + "Answer is " + answer)

    # after the quiz, print their final score
    print("\nYour final score was " + str(score))
    "\n"

    if score == 0:
        print("You're a stranger")
    elif score == 1:
        print("Really!")
    elif score == 2:
        print("And you claim to know me")
    elif score == 3:
        print("We should hang out more " + name)
    elif score == 4:
        print("You know me alright")
    elif score > 5:
        print("Meet me for pizza.. " + name)

    "\n"

    # store the user's input...
    again = input("Enter any key to play again, or 'q' to quit.")

    # ...and quit if they types 'q'
    if again.lower() == 'q':
        playing = False
