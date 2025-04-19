from langchain_core.prompts import PromptTemplate

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
Ensure the sumtemplatesmary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_inputs', 'style_inputs', 'length_inputs'],
validate_template=True # => it is used to check number of placeholders are equal to the length of input_variables
)

template.save('template.json')