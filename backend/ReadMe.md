Chatbot with Conversational Memory

This FastAPI app implements a chatbot with Conversational Memory capabilities. It allows users to interact with the chatbot by asking questions, saving answers to memory, asking follow-up questions, clearing memory, and viewing the memory content.
Functions:


• Answer Question:

• Endpoint: /answer_question
• Description: Accepts a question as input, provides an answer using the chatbot, and saves the answer to memory.
• Method: POST
• Request Body: {"question": "Your question here"}
• Response: {"answer": "Chatbot's answer"}


• Follow-up Question:

• Endpoint: /follow_up_question
• Description: Allows users to ask a follow-up question based on the previous interaction.
• Method: POST
• Request Body: {"question": "Your follow-up question here"}
• Response: {"answer": "Chatbot's response to the follow-up question"}


• Clear Memory:

• Endpoint: /clear_memory
• Description: Clears the memory content stored in the chatbot.
• Method: POST
• Response: {"message": "Memory cleared"}


• Memory Content:

• Endpoint: /memory_content
• Description: Retrieves and displays the content of the memory stored in the chatbot.
• Method: GET
• Response: {"memory_content": "Content of the memory"}



How to Run:


• Install the required dependencies:
pip install fastapi uvicorn langchain

• Run the FastAPI app:
uvicorn chatbot_app:app --reload

• Interact with the API using tools like cURL, Postman, or send HTTP requests programmatically to the defined endpoints.

download llama-2-7b-chat.Q5_K_M.gguf file and save it in models directory.