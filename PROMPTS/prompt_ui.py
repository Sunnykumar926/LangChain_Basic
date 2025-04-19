from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt 

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

st.header('Research Tool')

paper_input = st.selectbox('Select Research Paper Name', ['Attention Is All You Need', 'BERT: Pre-training of Deep Bidirectional Transformers', 'GPT-3: Language Models are Few-Shot Learners', 'Diffusion Models Beat GANs on Image Synthesis'])

style_input = st.selectbox('Select Explanation Style', ['Beginner-Friendly', 'Technical', 'Code-Oriented', 'Mathematical'])

length_input= st.selectbox('Select Explanation Length', ['Short (1-2 paragraph)', 'Medium (3-5 paragraph)', 'Long (detailed explanation)'])

template = load_prompt('template.json')

# -------------------- below code is not needed if you apply chaining --------------------------
# fill the placeholders
# prompt = template.invoke({
#     'paper_inputs': paper_input,
#     'style_inputs': style_input,
#     'length_inputs': length_input
# })

# if st.button('Summarize'):
#     result = model.invoke(prompt)
#     st.write(result.content)


# chaning => it is not allowed by chaining 

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_inputs': paper_input,
        'style_inputs': style_input,
        'length_inputs': length_input
    })
    st.write(result.content)
  