from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate   

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

st.header('Research Tool')

paper_input = st.selectbox('Select Research Paper Name', ['Attention Is All You Need', 'BERT: Pre-training of Deep Bidirectional Transformers', 'GPT-3: Language Models are Few-Shot Learners', 'Diffusion Models Beat GANs on Image Synthesis'])

style_input = st.selectbox('Select Explanation Style', ['Beginner-Friendly', 'Technical', 'Code-Oriented', 'Mathematical'])

length_input= st.selectbox('Select Explanation Length', ['Short (1-2 paragraph)', 'Medium (3-5 paragraph)', 'Long (detailed explanation)'])

# template 
template = PromptTemplate(
    template="""
Please summarize the research paper titled {paper_inputs} with the following specifications:
Explanation Style: {style_inputs}
Explanation Length: {length_inputs}
1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
2. Analogies:
    - Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient information available."
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_inputs', 'style_inputs', 'length_inputs'],
validate_template=True #=> it is used to check number of placeholders are equal to the length of input_variables
)

# fill the placeholders
prompt = template.invoke({
    'paper_inputs': paper_input,
    'style_inputs': style_input,
    'length_inputs': length_input
})

if st.button('Summarize'):
    result = model.invoke(prompt)
    st.write(result.content)
