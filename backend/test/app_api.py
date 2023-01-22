import os
import time
import requests
import streamlit as st

# API_URL = "https://api-inference.huggingface.co/models/NlpHUST/t5-en-vi-small"
URLS = [
    "https://api-inference.huggingface.co/models/NlpHUST/t5-en-vi-small",
    "https://api-inference.huggingface.co/models/haotieu/en-vi-mt-model",
    "https://api-inference.huggingface.co/models/VietAI/envit5-translation",
    "https://api-inference.huggingface.co/models/vinai/vinai-translate-en2vi"
]
API_URL = URLS[2]
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

st.set_page_config(
    page_title="Whisper & GPT-3",
    page_icon="musical_note",
    layout="wide",
    initial_sidebar_state="auto",
)

@st.cache(persist=True,allow_output_mutation=False,show_spinner=True,suppress_st_warning=True)
def save_transcript(transcript_data, txt_file):
    with open(os.path.join(txt_file),"w") as f:
        f.write(transcript_data)
        
@st.cache(persist=True,allow_output_mutation=False,show_spinner=True,suppress_st_warning=True)
def translate(source):
    while True:
        try:
            output = query({"inputs": source})
            output = output[0]['generated_text']
            break
        except Exception as e:
            # delay 2 seconds
            time.sleep(2)
            print(e )
            # st.error("Error: {}".format(e))
            pass
    return output

st.title("English Vietnamese Translation")
st.info('✨ This model is built with effort and tears 😉')
st.text("First enter the English sentence in the textbox below. \nThen click on the button to translate the text.")


st.markdown("## 📝 Input")
source = st.text_area(" ", height=200)

if st.button("Translate"):
    with st.spinner(f"Generating Transcript... 💫"):
        transcript = translate(source)
        print(transcript)
        if transcript is not None:
            st.markdown("## 🌏 Translation")
            st.text(transcript)

            # st.header("Sentiment analysis:")
            # st.caption("very negativ, negativ, neutral, positive, very positive")
            # st.text("Classified as:" + response.choices[0].text)
        else:
            st.error("Error: No transcript generated")

        st.success('✅ Successful !!')