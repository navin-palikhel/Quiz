print("Welcome to the Quiz Game!")

playing = input("Do you want to play? (yes/no)? ")

if playing.lower() != "yes":
    print("Maybe next time. Goodbye!")
    exit()
print("Great! Let's get started.")


# Quiz Questions

correct_answers = 0
wrong_answers = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    correct_answers += 1
else:
    print("Wrong! The correct answer is Central Processing Unit.")
    wrong_answers += 1

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    correct_answers += 1
else:
    print("Wrong! The correct answer is Random Access Memory.")
    wrong_answers += 1

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    correct_answers += 1
else:
    print("Wrong! The correct answer is Graphics Processing Unit.")
    wrong_answers += 1

answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print("Correct!")
    correct_answers += 1
else:
    print("Wrong! The correct answer is Solid State Drive.")
    wrong_answers += 1


print(f"You got {correct_answers} correct and {wrong_answers} wrong.")


if correct_answers > wrong_answers:
    print("Congratulations! You won the quiz!")
elif correct_answers < wrong_answers:
    print("Better luck next time! You lost the quiz.")
else:
    print("It's a tie! You did well!")
