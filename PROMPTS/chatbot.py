from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

#  --------------------------- VERSION 1 ---------------------------------------
# while True:
#     user_input = input('You: ')
#     if user_input=='exit':
#         break
#     result = model.invoke(user_input)
#     print('AI: ', result.content)

# => it will not capture the previouse context

# ------------------------ VERSION 2 -------------------------

# chat_history = [

# ]

# while True:
#     user_input = input('You: ')
#     chat_history.append(user_input)
#     if user_input=='exit':
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(result.content)
#     print('AI: ', result.content)

# print(chat_history)

# => problem in version 2 when chat history is larger in size then our model would not able to find 
#  which response is used by user and which one is by model 
# so, for this we also store which message is sent by user and which one is by AI


# ================================= VERSION 3 {static message => human , system and ai messages }=============================

# chat_history = [
#     SystemMessage(content='You are a  helpful AI assistent')
# ]

# while True:
#     user_input = input('You: ')
#     chat_history.append(HumanMessage(content=user_input))
#     if user_input=='exit':
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(AIMessage(content=result.content))
#     print('AI: ', result.content)

# print(chat_history)

# =================== VERSION 4 {dynamic messages => chatPromptTemplate} =====================================================

# => A MessagesPlaceholder in LangChain is a special placeholder 
# used inside a ChatPromptTemplate to dynamically insert chat history 
# or a list of messages at runtime.

from langchain_core.prompts import ChatPromptTemplate 

chat_template = ChatPromptTemplate([
    ('system', 'You are helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic   }')
    # SystemMessage(content='You are helpful {domain} expert'),
    # HumanMessage(content='Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'Bouncer'})
print(prompt)