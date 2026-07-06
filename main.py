from datetime import datetime
import random
import csv

user_name = ""

print("===================================")
print("        AI Chatbot in Python")
print("===================================")

print("Hello! I am Chintu 🤖")
print("Type 'bye' to exit.")

while True:
    user = input("\nYou: ").lower()

    if user == "hi" or user == "hello":
        print("Chintu: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Chintu: I am doing great! How about you?")

    elif user == "what is your name":
        print("Chintu: My name is Chintu. I am your AI chatbot.")

    elif user == "time":
        print("Chintu: Current time is", datetime.now().strftime("%I:%M %p"))

    elif user == "date":
        print("Chintu: Today's date is", datetime.now().strftime("%d %B %Y"))

    elif user == "calculator":
        print("Chintu: Calculator Mode")

        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Result:", num1 + num2)

        elif operator == "-":
            print("Result:", num1 - num2)

        elif operator == "*":
            print("Result:", num1 * num2)

        elif operator == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Cannot divide by zero.")

        else:
            print("Invalid operator.")

    elif user == "joke":
        jokes = [
            "Why did the programmer quit his job? Because he didn't get arrays.",
            "Why do Python programmers wear glasses? Because they can't C.",
            "Why was the computer cold? It left its Windows open.",
            "Why did the keyboard go to the doctor? It had too many bugs.",
            "Why was the math book sad? Because it had too many problems."
        ]

        print("Chintu:", random.choice(jokes))

    elif user.startswith("my name is "):
        user_name = user[11:].title()

        with open("user.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([user_name])

        print(f"Chintu: Nice to meet you, {user_name}!")

    elif user == "what is my name":
        try:
            with open("user.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    print(f"Chintu: Your name is {row[0]}.")
                    break

        except FileNotFoundError:
            print("Chintu: I don't know your name yet. Tell me by typing 'my name is ...'")

   elif user == "motivate":
        quotes = [
            "Success is the sum of small efforts repeated every day.",
            "Believe in yourself. You can achieve great things.",
            "Every expert was once a beginner.",
            "Never stop learning because life never stops teaching.",
            "Dream big, work hard, and stay consistent."
        ]

        print("Chintu:", random.choice(quotes))

  elif user == "help":
        print("\n===== Commands =====")
        print("hi / hello")
        print("how are you")
        print("what is your name")
        print("my name is <your name>")
        print("what is my name")
        print("date")
        print("time")
        print("calculator")
        print("joke")
        print("motivate")
        print("help")
        print("bye")
    elif user == "bye":
        print("Chintu: Goodbye! Have a nice day.")
        break

    else:
        print("Chintu: Sorry, I don't understand that yet.")
