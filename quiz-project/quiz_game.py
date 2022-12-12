print("Welcome to the Quiz Game!")

playing = input("Would you like to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play :)" )
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")




answer = input("What does ESC stand for on your keyboard? ")
if answer.lower() == "escape":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")




answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")




answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")




answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")




answer = input("What button do you hold to capitalize on your keyboard? ")
if answer.lower() == "shift":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")




answer = input("What is the snack that smiles back? ")
if answer.lower() == "goldfish":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")




answer = input("What does USD stand for? ")
if answer.lower() == "united states dollar":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")




answer = input("Who owns Twitter? ")
if answer.lower() == "elon musk":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")




answer = input("What coding language created this quiz? ")
if answer.lower() == "python":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
