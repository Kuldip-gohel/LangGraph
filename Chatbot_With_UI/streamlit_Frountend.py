import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG = {'configurable': {'thread_id':'thread-1'}}

# st.session_state - > dict -> only erase when we relod page , so using this dict we can solve this problem like when we press enter it will not erase.

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []


# loading the conversasion history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

user_input = st.chat_input('type here')

if user_input:

    # First add the message to message hitory.
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

    response = chatbot.invoke({'messages': HumanMessage(content=user_input)}, config=CONFIG)
    ai_message = response['messages'][-1].content
    # First add the message to message hitory.
    st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)












# ------------------------------------------------------
# # Chat_message component

# with st.chat_message('user'):  # Have to tell here who will write message like user or AI 
#     st.text('hi')

# with st.chat_message('assistant'):
#     st.text('how can i help you ?')

# # Chat input component
# user_input = st.chat_input('Type here')

# if user_input:   
#     with st.chat_message('user'): # We store into user component and disply it 
#         st.text(user_input)
# -------------------------------------------
