import random


def generate_math_problem():
    """Generates a random math problem and returns the correct answer."""
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*', '/'])

    if operator == '/':
        # Only generate numbers that divide into whole numbers
        factors = [i for i in range(1, num1 + 1) if num1 % i == 0]
        num2 = random.choice(factors)
        num1 = num1 // num2

    problem = f"{num1} {operator} {num2}"
    answer = eval(problem)
    return problem, answer


def ask_for_answer(problem):
    """Asks the user for an answer and compares it to the correct answer."""
    user_answer = input(f"What is {problem}? ")
    try:
        user_answer = int(user_answer)
    except ValueError:
        return None  # Return None if user input is not an integer

    return user_answer


def generate_and_check_problems():
    """Generates and checks math problems until user types 'done'."""
    num_questions = 0
    num_correct = 0
    num_incorrect = 0

    while True:
        problem, answer = generate_math_problem()
        user_answer = ask_for_answer(problem)

        if user_answer is None:
            print("Invalid input. Please enter an integer or type 'done'.")
            continue  # Ask for input again

        num_questions += 1

        if user_answer == answer:
            print("Congratulations! That's the correct answer.")
            num_correct += 1
        else:
            print(f"Sorry, the correct answer is {answer}.")
            num_incorrect += 1

        done = input("Type 'done' to quit or press Enter to continue: ")
        if done.lower() == 'done':
            break

    print(f"Number of questions answered: {num_questions}")
    print(f"Number of correct answers: {num_correct}")
    print(f"Number of incorrect answers: {num_incorrect}")
    print(f"Grade: {num_correct}/{num_questions}")


generate_and_check_problems()
