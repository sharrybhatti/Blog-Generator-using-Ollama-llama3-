import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import Ollama



#function to get response from llama2 model
def getllama_response(input_text,no_words,blog_style):


    #llm model
    llm = Ollama(model="llama3")
    #prompt template
    template= """
         Write  a blog for {blog_style} for a topic{input_text} within {no_words} words.

              """

    prompt=PromptTemplate(input_variables=["blog_style","input_text","no_words"],
                          template=template)

    #generate response form llma2 model
    response= llm(prompt.format(blog_style=blog_style, input_text=input_text,no_words=no_words))
    print(response)
    return response



st.set_page_config(page_title="Geneate Blogs",
                 layout='centered',
                 page_icon='🤖',
                 initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter Blog topic")

#Creating 2 more additional columns
col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input("No Of Words")

with col2:
    blog_style=st.selectbox("Writing Blog for",('Reasearchers','Data Scientists',' Common People'),index=0)


Submit=st.button("Generate")

#final response
if Submit:
    st.write(getllama_response(input_text,no_words,blog_style))