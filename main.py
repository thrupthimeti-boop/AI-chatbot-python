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

    elif user == "bye":
        print("Chintu: Goodbye! Have a nice day.")
        break

    else:
        print("Chintu: Sorry, I don't understand that yet.")
