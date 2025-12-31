#project config
import google.generativeai as genai
genai.configure(api_key="AIzaSyDJ5Jz9Ik6lmfPMYigdBRxB1XGhKLj-hZk")
apple = genai.GenerativeModel("gemini-2.5-flash")
chat = apple.start_chat(history=[])
print("Hi I'm Apple the chatbot")
while True:
    user_input = input("User : ")

    if user_input.lower() == "bye":
        break

    response = chat.send_message(user_input)
    print("Apple : ",response.text)
