score = 0

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["a) Mumbai", "b) Delhi", "c) Pune"],
        "answer": "b"
    },
    {
        "question": "Which language is used for Python files?",
        "options": ["a) .py", "b) .java", "c) .html"],
        "answer": "a"
    },
    {
        "question": "Who is known as Father of Computer?",
        "options": ["a) Charles Babbage", "b) Newton", "c) Einstein"],
        "answer": "a"
    }
]

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (a/b/c): ")

    if user_answer.lower() == q["answer"]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")

print("\nQuiz Completed!")
print("Your Final Score is:", score, "/", len(questions))