from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

llm= HuggingFacePipeline.from_model_id(
    model_id="mistralai/Mistral-7B-Instruct-v0.3",
    task="conversational",
    pipeline_kwargs=dict(
        max_new_tokens=100,
        temperature=0.9
    )  
)

model = ChatHuggingFace(llm=llm)

result= model.invoke("What is the capital of India?")
print(result.content)