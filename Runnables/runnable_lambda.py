from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.prompts import PromptTemplate 
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda 

load_dotenv() 

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template='Generate a joke about {topic}',
    input_variables=['topic']
)
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro') 

parser = StrOutputParser()

joke_gen_AI = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(), 
    'word_count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_AI, parallel_chain)
result = final_chain.invoke({'topic': 'Lord Krishna'})

print(result['joke'])
print(result['word_count'])