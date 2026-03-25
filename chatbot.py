import datetime


def normalize_input(user_input):
    """Clean and normalize user input."""
    return user_input.strip().lower()


def generate_response(message):
    """Return chatbot response based on user message."""

    if message in ["hello", "hi", "hey"]:
        return "Hi there!"

    elif message in ["how are you", "how are you doing"]:
        return "I'm doing well, thanks for asking! How about you?"

    elif message in ["what is your name", "who are you"]:
        return "I'm your simple Python chatbot."

    elif message in ["time", "current time"]:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}"

    elif message == "bye":
        return "Goodbye! Have a great day!"

    else:
        return "Hmm... I didn't quite understand that. Try saying 'hello' or 'help'."


def start_chat():
    """Main chatbot loop."""

    print("=" * 40)
    print("Welcome to Python Chatbot")
    print("Type 'bye' to exit the conversation")
    print("=" * 40)

    conversation_count = 0

    while True:
        user_input = input("\nYou: ")
        message = normalize_input(user_input)

        response = generate_response(message)
        print("Bot:", response)

        conversation_count += 1

        if message == "bye":
            print(f"\nSession ended. Messages exchanged: {conversation_count}")
            break


if __name__ == "__main__":
    start_chat()