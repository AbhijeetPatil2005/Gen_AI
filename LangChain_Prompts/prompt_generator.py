from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}

Explanation Length: {length_input}

1. Mathematical Details:
- Include relevant mathematical equations if present in the paper.
- Explain mathematical concepts in simple terms.

2. Code Snippets:
- Provide simple intuitive code examples where applicable.

3. Analogies:
- Use relatable analogies to simplify complex ideas.

If certain information is not available, respond with:
"Insufficient information available"

Ensure the summary is clear, accurate, and aligned with the selected style and length.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    valid_template=True
)

template.save('template.json')