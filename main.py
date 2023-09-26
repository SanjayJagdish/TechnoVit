# Sustainable development Quiz

questions = ("What does SDG stand for in the context of sustainable development?: ",
             "Which is a renewable energy source?: ",
             "What is the primary aim of sustainable development?: ",
             "What is the primary focus of biodiversity conservation?: ",
             "Which is considered more sustainable?: ")

options = (("A. Sustainable Development Goals", "B. Social Development Goals", "C. Sustainable Design Guidelines",),
           ("A. Coal", "B. Natural Gas", "C. Solar"),
           ("A. Economic growth", "B. Environmental conservation", "C. Both of them"),
           ("A. Protect endangered species", "B. Increase industrial production", "C. Expand urban development"),
           ("A. Throwing away used products", "B. Reusing or recycling products", "C. Buying new products frequently"))

answers = ("A", "C", "C", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
