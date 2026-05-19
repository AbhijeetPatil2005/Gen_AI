from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGroq(model ="llama-3.3-70b-versatile")

parser = StrOutputParser()

class feedback(BaseModel):
    sentiments:Literal['positive', 'negative'] = Field(description="The sentiment of the feedback, either positive or negative")
    
parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions': parser2.get_format_instructions()}
)

classifier_chain=prompt1 | model | parser2

prompt2 =PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']    
)

prompt3 =PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']    
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiments=='positive', prompt2 | model | parser),
    (lambda x:x.sentiments=='negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment in the feedback")
)

chain = classifier_chain | branch_chain
result= chain.invoke({'feedback': 'I love this product! It has exceeded my expectations.'})
print(result)
chain.get_graph().print_ascii()