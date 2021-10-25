import random

name = "Joe"
question = "Is this real life?"
answer = ""
random_number = random.randint(1,15)

#print(random_number)

if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "How about another question?"
elif random_number == 11:
  answer = "This very well is."
elif random_number == 12:
  answer = "Yes, yes, yes."
elif random_number == 13:
  answer = "No, no no."
elif random_number == 14:
  answer = "I am not sure if I can help you."
elif random_number == 15:
  answer = "Alas!"
else:
  answer = "Error"
#condition for if the name is empty
if name == "":
    print("Question: " + question)
else:
  print(name, 'asks: ' + question)
print("Magic 8-Ball's answer:", answer)

#Condition for if the question is empty
if question == "":
  print("The Magic 8-ball cannot provide a fortune unless you as it something.")
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)
