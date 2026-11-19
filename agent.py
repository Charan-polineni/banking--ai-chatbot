def chatbot(question):
    question = question.lower()

    if "payment" in question:
        return "Please authenticate to check your payment status."

    if "balance" in question:
        return "Please authenticate to check your account balance."

    if "transaction" in question:
        return "Please authenticate to view your transaction history."

    return "Welcome to the Banking AI Assistant."


if __name__ == "__main__":
    examples = (
        "Where is my payment?",
        "What is my account balance?",
        "Can I see my transactions?",
        "Hello",
    )

    for question in examples:
        print(f"Q: {question}")
        print(f"A: {chatbot(question)}")
