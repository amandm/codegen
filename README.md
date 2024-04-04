# Chatbot with Conversational Memory

FastAPI project is in backend folder where there are different API's that you can call for the chat bot. 

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

# Model Details

- **Model Choice:** Chosen `llama-2-7b-chat.Q5_K_M.gguf` for a balanced approach to computational efficiency and complex code generation capabilities.
- **Temperature:** Set to `0` for deterministic and consistent code outputs.
- **Max Tokens:** Increased to `5000` to support longer code generation without breaks, suitable for complex tasks.
- **Context Size (`ctx_size`):** Adjusted to `1000`, offering a large context window for relevant and coherent code generation, optimizing performance.
- **Verbose:** Enabled (`True`) to provide detailed logging, essential for debugging and insight into the model's processes.
- **Parameter Flexibility:** Comments out specific parameters like `repeat_penalty`, `top_p`, and `stop`, showcasing adaptability for different code generation nuances.





To check frontend sperately, you need to install llama.cpp and serve the model on default port.

# Next.js, Vercel AI SDK, Llama.cpp & ModelFusion starter


## Setup

1. Install dependencies: `npm install`
2. Start the development server: `npm run dev`
3. you also need to download the GGUF model and start the Llama.cpp server. (use default port 8080)

