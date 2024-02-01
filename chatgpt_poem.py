import openai
import streamlit as st


OPENAI_API_KEY='8c91c5c7058847f3820f9d7c12bbb1fb' 

OPENAI_API_ENDPOINT='https://sktfly-ai.openai.azure.com/' 

OPENAI_API_TYPE = 'azure'

OPENAI_API_VERSION = '2023-05-15'


openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = OPENAI_API_ENDPOINT
openai.api_type = OPENAI_API_TYPE
openai.api_version = OPENAI_API_VERSION

st.header('인공지능 시인 서비스', divider='rainbow')

name = st.text_input('이름을 입력하세요')
a = st.button('확인')
   
if a and name:
    st.write(name + '님 반갑습니다')

subject = st.text_input('시의 주제는?')
content = st.text_area('시의 내용을 입력하세요')


b = st.button('run')
if b:
    with st.spinner('wait'):
        reslut = openai.chat.completions.create(
            model = 'dev-gpt-35-turbo',
            messages=[
                {'role':'system', 'content':'Remember, you are a poem.'},
                {'role':'user', 'content': '작가의 이름은 ' + name},
                {'role':'user', 'content': '시의 주제는 ' + subject},
                {'role':'user', 'content': '시의 내용은 ' + content},
                {'role':'user', 'content': '위 내용으로 시를 작성해줘.'}
            ]
        )
        st.write(f'{reslut.choices[0].message.content}')
        print(f'qurey : {reslut}\n{reslut.choices[0].message.content}')
        st.success('done')