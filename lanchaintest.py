from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
from langchain_experimental.chat_models import Llama2Chat
from langchain.prompts.chat import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
# Create Llama2Chat instance
llm = LlamaCpp(
    model_path="/Users/aman.meena/Documents/CodeReview/models/llama-2-7b-chat.Q5_K_M.gguf",
    temperature=0,
    max_tokens=5000,
    # max_tokens = 512,
    ctx_size= 1000,
    # repeat_penalty = 1.5,
    # stop= ['Human:'],
    # top_p=1,
    callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
)

# Define the chat prompt template
template_messages = [
    SystemMessage(content="You are a helpful code assistant that can teach a junior developer how to code. Your language of choice is Python. Don't explain the code, just generate the code block itself."),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{text}"),
]
prompt_template = ChatPromptTemplate.from_messages(template_messages)

# template_messages = [
#     SystemMessage(content="You are a chatbot having a conversation with a human."),
#     MessagesPlaceholder(variable_name="chat_history"),
#     SystemMessage(content="Ask me a question."),
# ]
# prompt_template = ChatPromptTemplate.from_messages(template_messages)
print()
print()
print(prompt_template)

# Create ConversationBufferMemory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Create LLMChain with Llama2Chat and Conversational Memory
chain = LLMChain(llm=llm, prompt=prompt_template, memory=memory)

question = "write a python code to factorize a number."
# chain.invoke({"text": question})
response = chain({"text": question, "chat_history": []})
# print(response)
if 'text' in response:
    answer_content = response["text"]
    memory.save_context({"input": question}, {"answer": answer_content})
    print("answer", answer_content)
else:
    print("error", "Answer not found in response")


print()
print(memory)
print()

question = "now also return sum of those factors"
response = chain({"text": question, "chat_history": []})
if 'answer' in response:
    answer_content = response["answer"].content
    memory.save_context({"input": question}, {"answer": answer_content})
    print("answer", answer_content)
else:
    print("error", "Answer not found in response")

print()
print(memory)
print()

# memory.chat_memory = []

# print(memory)