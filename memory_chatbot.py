from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

chat_history = []

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    chat_history.append(
        f"User: {user_input}"
    )

    prompt = "\n".join(chat_history)

    response = llm.invoke(prompt)

    print("AI:", response.content)

    chat_history.append(
        f"AI: {response.content}"
    )