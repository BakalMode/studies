import random
questions = open("C:\\Users\\turht\\Desktop\\myfile.txt", "w")
answers = open("C:\\Users\\turht\\Desktop\\myanswers.txt", "w")
actions = ["*", "/", "-", "+"]

for question in range(0,10):
    random1 = (random.randint(1, 10))
    random2 = (random.randint(1, 10))
    rnd_action = actions[(random.randint(0,3))]

    questions.write(f"{question+1}. {str(random1)} {rnd_action} {str(random2)} =\n")
    if rnd_action == "+":
        answer = random1+random2
    elif rnd_action == "-":
        answer = random1-random2
    elif rnd_action == "*":
        answer = random1*random2
    elif rnd_action == "/":
        answer = random1/random2
    answers.write(f"{question+1}. {str(random1)} {rnd_action} {str(random2)} = {answer} \n")







