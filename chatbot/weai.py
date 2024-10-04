def get_response(user_message):
    # Simple response logic for demonstration
    responses = {
        "hello": "Hi there! How can I assist you today?",
        "bye": "Goodbye! Have a great day!",
        "how are you": "I'm just a bot, but I'm here to help you!"
    }
    return responses.get(user_message.lower(), "I'm sorry, I don't understand that.")
