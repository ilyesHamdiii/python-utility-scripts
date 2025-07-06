import random

quiz = {
    "question1": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What is the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What is the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7": {
        "question": "What is the capital of Austria?",
        "answer": "Vienna"
    },
}

score = 0

questions = list(quiz.values())
random.shuffle(questions)

for q in questions:
    print(q['question'])
    answer = input("Answer? ").strip()

    if answer.lower() == q['answer'].lower():
        print(" Correct!")
        score += 1
    else:
        print(f" Wrong! The correct answer is: {q['answer']}")

    print(f"Current score: {score}")
