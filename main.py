from datetime import datetime

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

    elif user == "bye":
        print("Chintu: Goodbye! Have a nice day.")
        break

    else:
        print("Chintu: Sorry, I don't understand that yet.")
