from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= 'Summarize the following report : {text}',
    input_variables=['text']
)

model = ChatGroq(model="llama-3.3-70b-versatile")
output_parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1,model,output_parser)

branch_chain = RunnableBranch(
    (lambda x : len(x.split())>500,RunnableSequence(prompt2 ,model,output_parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain,branch_chain)
result = final_chain.invoke({'topic':'AI'}) 
print(result)
