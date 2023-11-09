from langchain.chains import LLMChain
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
import boto3
import os

##THIS FILE IS UNUSED RIGHT NOW##

#env permissions
os.environ["AWS_PROFILE"] = "trevor"

#bedrock client
bedrock_client = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)

modelId = "anthropic.claude-v2"

llm = Bedrock(
    model_id=modelId,
    client=bedrock_client,
    model_kwargs={"max_tokens_to_sample": 2000,"temperature": 0.9},
)

#Function to call claude with a prompt template and input variables
def my_chatbot(language,freeform_text):

    prompt_template_name = PromptTemplate(
        input_variables=['language','freeform_text'],
        template="You are a helpful assistant. Please respond in {language}.\nThe question is{freeform_text}.\n if you do not know the answer please say you do not know",
    )

    bedrock_chain = LLMChain(llm=llm, prompt=prompt_template_name)

    #Call claude with the input variables and save to response variable
    response=bedrock_chain({'language': language, 'freeform_text': freeform_text})
    return response

#test code to input variables into function
if __name__ == "__main__":
    print(my_chatbot("english","who is buddha?"))