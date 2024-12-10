


def check_if_correct(answer, user_answer):
    global score
    if user_answer.lower() == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect")

def question(question_text, correct_answer):
    user_answer = input(question_text)
    check_if_correct(correct_answer, user_answer)


playing = input("Do you wanna play?\n").lower()
score = 0
if playing!= "yes":
    quit()
print("Let's play)")

question("What does CPU stand for?\n", "central processing unit")
question("What does GPU stand for?\n", "graphics processing unit")
question("What does RAM stand for?\n", "random access memory")
question("What does PSU stand for?\n", "power supply")
print(f"You got score: {score}")
print(f"You got score: {(score / 4) * 100}%")




