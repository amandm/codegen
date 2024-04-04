from typing import Any, Dict, List, Optional
from pydantic import root_validator
from langchain.memory.chat_memory import BaseMemory
from langchain.memory.utils import get_prompt_input_key
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate
from langchain_experimental.chat_models import Llama2Chat
from langchain.prompts.chat import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage

class LlamaConversationMemory(BaseMemory):
    """Buffer for storing conversation memory."""

    human_prefix: str = ""
    ai_prefix: str = ""
    """Prefix to use for AI generated responses."""
    buffer: str = ""
    output_key: Optional[str] = None
    input_key: Optional[str] = None
    memory_key: str = "history"  #: :meta private:

    @root_validator()
    def validate_chains(cls, values: Dict) -> Dict:
        """Validate that return messages is not True."""
        if values.get("return_messages", False):
            raise ValueError(
                "return_messages must be False for LlamaConversationMemory"
            )
        return values

    @property
    def memory_variables(self) -> List[str]:
        """Will always return list of memory variables.
        :meta private:
        """
        return [self.memory_key]

    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, str]:
        """Return history buffer."""
        return {self.memory_key: self.buffer}

    def save_context(self, inputs: Dict[str, Any], outputs: Dict[str, str]) -> None:
        """Save context from this conversation to buffer."""
        if self.input_key is None:
            prompt_input_key = get_prompt_input_key(inputs, self.memory_variables)
        else:
            prompt_input_key = self.input_key
        if self.output_key is None:
            if len(outputs) != 1:
                raise ValueError(f"One output key expected, got {outputs.keys()}")
            output_key = list(outputs.keys())[0]
        else:
            output_key = self.output_key
        human = inputs[prompt_input_key]
        ai = outputs[output_key]
        self.buffer += " [/INST] ".join([human, ai])
        self.buffer += " </s><s>[INST] "

    def clear(self) -> None:
        """Clear memory contents."""
        self.buffer = ""

# Define the chat prompt template
template_messages = [
    SystemMessage(content="You are a chatbot having a conversation with a human."),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template("{text}"),
]
prompt_template = ChatPromptTemplate.from_messages(template_messages)

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])     
llm = LlamaCpp(
    model_path="/Users/aman.meena/Documents/CodeReview/models/llama-2-7b-chat.Q5_K_M.gguf",
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
)
memory = LlamaConversationMemory()

# Create LLMChain with Llama2Chat and Conversational Memory
chain = LLMChain(llm=llm, prompt=prompt_template, memory=memory)

question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"
chain.invoke({"text": question})

