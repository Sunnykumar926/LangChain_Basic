from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 
from langchain_core.output_parsers import JsonOutputParser 
from langchain_core.prompts import PromptTemplate 

load_dotenv() 

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro') 

parser = JsonOutputParser() 

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}', 
    input_variables=['topic'], 
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser 
result = chain.invoke({'topic': 'black hole'}) 
print(result) 


