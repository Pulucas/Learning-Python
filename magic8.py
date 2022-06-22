import random

name = input("What is your name? ")
question = input("What is your question? (Preferably make it a yes no question) ")
rng = random.randint(1, 9)
if rng == 1:
    answer = "Yes - definitely."
elif rng == 2:
    answer = "It is decidedly so."
elif rng == 3:
    answer = "Without a doubt."
elif rng == 4:
    answer = "Reply hazy, try again."
elif rng == 5:
    answer = "Ask again later."
elif rng == 6:
    answer = "Better not tell you now."
elif rng == 7:
    answer = "My sources say no."
elif rng == 8:
    answer = "Outlook not so good."
elif rng == 9:
    answer = "Very doubtful."
else:
    answer = "Error: Number is not within the range specified or is a float"

#print(question == None)

# If no question is put in, it will ask for a question
if question == "":
    print("You Need To Ask A Question!")
elif name == "":
    print("Question: " + question)
    print("Magic 8-Ball's answer: " + answer)
else:
    print(name + " asks: " + question)
    print("Magic 8-Ball's answer: " + answer)