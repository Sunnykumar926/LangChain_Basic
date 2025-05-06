from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 
from dotenv import load_dotenv 
from langchain.schema.runnable import RunnableSequence, RunnableParallel

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro') 

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate( 
    template = 'Generate a linkedIn post about {topic}',
    input_variables=['topic']
)

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedIN': RunnableSequence(prompt2, model, parser) 
})

result = parallel_chain.invoke({'topic': 'AI'})
print(result['tweet'])
print(f'------------------------------')
print(result['linkedIN'])

