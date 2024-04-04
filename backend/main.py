from fastapi import FastAPI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
from langchain_experimental.chat_models import Llama2Chat
from langchain.prompts.chat import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage


app = FastAPI()

# Initialize Llama2Chat and ConversationBufferMemory
llm = LlamaCpp(
    model_path="models/llama-2-7b-chat.Q5_K_M.gguf",
    temperature=0,
    max_tokens=5000,
    # max_tokens = 512,
    ctx_size= 1000,
    # repeat_penalty = 1.5,
    # stop= ['Human:'],
    # top_p=1,
    # callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
)
# Define the chat prompt template
template_messages = [
    SystemMessage(content="You are a helpful code assistant that can teach a junior developer how to code. Your language of choice is Python. Don't explain the code, just generate the code block itself."),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{text}"),
]
prompt_template = ChatPromptTemplate.from_messages(template_messages)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# Create LLMChain with Llama2Chat and Conversational Memory
chain = LLMChain(llm=llm, prompt=prompt_template, memory=memory)

@app.post("/answer_question")
def answer_question(question: str):
    # Answer the question and save to memory
    # chain.invoke({"text": question})
    response = chain({"text": question, "chat_history": []})
    if 'text' in response:
        answer_content = response["text"]
        memory.save_context({"input": question}, {"answer": answer_content})
        # print("answer", answer_content)
        return {"answer" : answer_content}
    else:
        print("error", "Answer not found in response")
        return {"status" : "Answer not found in response"}

@app.post("/follow_up_question")
def follow_up_question(question: str):
    # Ask a follow-up question
    response = chain({"text": question, "chat_history": []})
    
    if 'text' in response:
        answer_content = response["text"]
        memory.save_context({"input": question}, {"answer": answer_content})
        # print("answer", answer_content)
        return {"answer" : answer_content}
    else:
        memory.chat_memory = []
        print("error", "Answer not found in response")
        return {"status" : "Answer not found in response"}

@app.post("/clear_memory")
def clear_memory():
    # Clear the memory
    memory.chat_memory = []
    return {"message": "Memory cleared"}

@app.get("/memory_content")
def get_memory_content():
    # Get the content of the memory
    memory_content = memory.chat_memory
    return {"memory_content": memory_content}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)