def chatbot(question):
    if "payment" in question.lower():
        return "Please authenticate to check your payment status."

    return "Welcome to the Banking AI Assistant."


print(chatbot("Where is my payment?"))