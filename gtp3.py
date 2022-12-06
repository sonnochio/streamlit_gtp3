import streamlit as st
import os
import openai


st.markdown("# Click here to predict")

st.write('Enter keywords seperated by commas, for example: Lady Gaga, Cups, London')

openai.api_key = os.getenv("OPENAI_API_KEY")
#  "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"


key_words=st.text_input(" ")
def generate_title_gtp3(text):

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"write a YouTube title about {text}",
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )

    return ((response["choices"])[0]["text"])

st.write('A good title would be', generate_title_gtp3(key_words))

# import time

#     'Starting a long computation...'

#     # Add a placeholder
#     latest_iteration = st.empty()
#     bar = st.progress(0)

#     for i in range(100):
#         # Update the progress bar with each iteration.
#         latest_iteration.text(f'Iteration {i+1}')
#         bar.progress(i + 1)
#         time.sleep(0.1)

#     '...and now we\'re done!'
