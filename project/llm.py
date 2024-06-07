from langchain.chains import ConversationChain
from langchain.memory import ConversationEntityMemory
from langchain.prompts import PromptTemplate
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from langchain_openai import OpenAI
# from config import get_config
import os

os.environ["OPENAI_API_KEY"] = "sk-proj-2LvdOnO8NG9Mr9YsER9KT3BlbkFJSR1BhU3XiW18tq1LiQD4"

messages_chat = []

global llm
global chain

# def load_embedding_model(model_path, normalize_embedding=True):
#     return OllamaEmbeddings(model=model_path)

template = "You are an AI.\nDon't repeat answers from your History.\nEntities: {entities}\nHistory: {history}\nAnswer the following question:\nHuman: {input}\nPlease provide a relevant response.\nAI:"
    
def get_response(query, chain):
    return chain.invoke(input=query)["response"]

def input_message(inp):
    global chain
    return get_response(inp, chain)

def add_to_messages_and_gen(inp):
    ai = input_message(inp)
    print(ai)
    messages_chat.append({"title" : "User", "text" : inp})
    messages_chat.append({"title" : "AI", "text" : ai})
    
def setup_chat():
    global chain,llm
    
    llm = OpenAI()
    PROMPT = PromptTemplate(input_variables=['entities', 'history', 'input'], template=template)
    chain = ConversationChain(llm=llm, memory=ConversationEntityMemory(llm=llm), prompt=PROMPT, verbose=False)
