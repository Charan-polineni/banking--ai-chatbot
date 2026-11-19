def chatbot(question):
    question = question.lower()

    if "payment" in question:
        return "Please authenticate to check your payment status."

    if "balance" in question:
        return "Please authenticate to check your account balance."

    if "transaction" in question:
        return "Please authenticate to view your transaction history."

    return "Welcome to the Banking AI Assistant."


print(chatbot("Where is my payment?"))
