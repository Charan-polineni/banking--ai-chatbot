# Banking AI Chatbot

A small Python chatbot prototype that matches banking keywords and returns preset responses. It uses only Python's standard library and runs without additional packages, API keys, or a bank connection.

## Run locally

Install Python 3, then run this command in the project folder:

```powershell
python agent.py
```

The script prints each example question below followed by the chatbot's response.

## Supported questions

| Example question | Response |
| --- | --- |
| Where is my payment? | Please authenticate to check your payment status. |
| What is my account balance? | Please authenticate to check your account balance. |
| Can I see my transactions? | Please authenticate to view your transaction history. |
| Hello | Welcome to the Banking AI Assistant. |

Keyword matching is case-insensitive. Authentication prompts are sample responses. The prototype does not authenticate users or access account data.
