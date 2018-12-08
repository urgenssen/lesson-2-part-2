answers = {"Hi":"Hello!", "How are you?":
"Excellent, and you?", "Bye":"See you soon!"}

def get_answer(question, amswer):
    return answers.get(question)

def ask_user(answers):
    try:
        while True:
            user_input = input("Скажи что-нибудь: ")
            
            if user_input == 'пока':
                print("\n", "Пока")
                break
            answer = get_answer(user_input, answers)
            print(answer)

    except KeyboardInterrupt:

        print("\n", "Пока")

if __name__ == "__main__":
    ask_user(answers)