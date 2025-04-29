
 # ========================================= WITHOUT OUTPUT PARSER ===================================================================

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 

load_dotenv()

# model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# # 1st prompt detailed report on particular topic 
# template1 = PromptTemplate(
#     template='Write a detailed report on {topic}',
#     input_variables=['topic']  
# )

# # 2nd prompt 5-line summary on that topic

# template2 = PromptTemplate(
#     template='Write a 5 line summary on the following text. /n {text}',
#     input_variables=['text']
# )

# prompt1 = template1.invoke({'topic': 'black hole'}) 

# result = model.invoke(prompt1) 

# prompt2 = template2.invoke({'text': result.content})

# result2 = model.invoke(prompt2)
# print(result2.content)

# ============================================== USING OUTPUT PARSER WITHOUT CHAINING ====================================================

# model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# # 1st prompt detailed report on particular topic 
# template1 = PromptTemplate(
#     template='Write a detailed report on {topic}',
#     input_variables=['topic']  
# )

# # 2nd prompt 5-line summary on that topic

# template2 = PromptTemplate(
#     template='Write a 5 line summary on the following text. /n {text}',
#     input_variables=['text']
# )

# parser = StrOutputParser() 

# prompt1 = template1.invoke({'topic': 'black hole'}) 
# detailed_report = model.invoke(prompt1) 
# parsed_report = parser.invoke(detailed_report)

# prompt2 = template2.invoke({'text': parsed_report}) 
# summary = model.invoke(prompt2) 
# final_summary = parser.invoke(summary)
# print(final_summary)

# ============================================== USING OUTPUT PARSER WITH CHAINING =======================================================

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

# 1st prompt detailed report on particular topic 
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']  
)

# 2nd prompt 5-line summary on that topic

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser() 

chain = template1 | model | parser | template2 | model | parser 

result = chain.invoke({'topic': 'black hole'}) 

print(result)

