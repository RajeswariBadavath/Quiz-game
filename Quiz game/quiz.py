import random
import time

# Data for geography capitals (static list, used in generator)
capitals = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brasília",
    "Canada": "Ottawa",
    "Australia": "Canberra"
}

# Question generators by topic
def math_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(['+', '-', '*'])
    if op == '+':
        correct = num1 + num2
    elif op == '-':
        correct = num1 - num2
    else:
        correct = num1 * num2

    question = f"What is {num1} {op} {num2}?"
    wrong_answers = set()
    while len(wrong_answers) < 3:
        fake = correct + random.randint(-10, 10)
        if fake != correct and fake >= 0:
            wrong_answers.add(fake)

    options = list(wrong_answers) + [correct]
    random.shuffle(options)

    lettered_options = [f"{chr(65+i)}) {opt}" for i, opt in enumerate(options)]
    correct_letter = chr(65 + options.index(correct))

    return question, lettered_options, correct_letter

def geography_question():
    country = random.choice(list(capitals.keys()))
    correct = capitals[country]

    # Get wrong options (capitals from other countries)
    wrong_options = set(capitals.values()) - {correct}
    wrong_answers = random.sample(wrong_options, 3)

    options = wrong_answers + [correct]
    random.shuffle(options)

    question = f"What is the capital of {country}?"
    lettered_options = [f"{chr(65+i)}) {opt}" for i, opt in enumerate(options)]
    correct_letter = chr(65 + options.index(correct))

    return question, lettered_options, correct_letter

def cs_question():
    # Simple CS fact questions with variations
    facts = [
        ("Which language is known as the backbone of web development?", ["Python", "C++", "Java", "JavaScript"], "D"),
        ("What does 'CPU' stand for?", ["Central Processing Unit", "Computer Personal Unit", "Central Programming Unit", "Control Processing Unit"], "A"),
        ("Which data structure uses LIFO?", ["Queue", "Linked List", "Stack", "Array"], "C"),
        ("What does HTML stand for?", ["HyperText Markup Language", "Hyper Tool Makeup Language", "Hyperlink Text Makeup Language", "Home Tool Markup Language"], "A")
    ]
    question, options, answer = random.choice(facts)
    lettered_options = [f"{chr(65+i)}) {opt}" for i, opt in enumerate(options)]
    return question, lettered_options, answer

def general_knowledge_question():
    # True/False or multiple choice general facts
    facts = [
        ("The Earth is flat.", ["True", "False"], "B"),
        ("The Great Wall of China is visible from space.", ["True", "False"], "B"),
        ("Light travels faster than sound.", ["True", "False"], "A"),
        ("The chemical symbol for water is H2O.", ["True", "False"], "A")
    ]
    question, options, answer = random.choice(facts)
    lettered_options = [f"{chr(65+i)}) {opt}" for i, opt in enumerate(options)]
    return question, lettered_options, answer

# List of all generators
all_generators = [
    math_question,
    geography_question,
    cs_question,
    general_knowledge_question
]

def generate_random_question():
    gen = random.choice(all_generators)
    return gen()

def start_quiz(total_questions):
    print(f"\nStarting Quiz: {total_questions} questions from mixed topics!\n")
    score = 0
    start_time = time.time()

    for i in range(1, total_questions + 1):
        question, options, correct_answer = generate_random_question()
        print(f"Q{i}: {question}")
        for opt in options:
            print(opt)

        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer == correct_answer:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer was {correct_answer}\n")

    total_time = int(time.time() - start_time)
    print(f"Quiz Finished! Your score: {score} / {total_questions}")
    print(f"Time taken: {total_time} seconds\n")

def main():
    print("Welcome to the Auto-Generated Multi-Topic Quiz Game!")
    name = input("Enter your name: ")
    while True:
        try:
            total_questions = int(input("How many questions do you want? (e.g., 5): "))
            if total_questions <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    start_quiz(total_questions)

if __name__ == "__main__":
    main()
