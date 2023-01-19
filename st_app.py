import os
from datetime import datetime
import streamlit as st
import torch
import pandas as pd
import jsonlines
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model_path = r"models/mbart-large-50-one-to-many-mmt"
device = 'cpu' if not torch.cuda.is_available() else 'cuda'
history_path = r"data/history.jsonl"

# load model
@st.cache(allow_output_mutation=True,show_spinner=True,suppress_st_warning=True)
def load_model():
    model = MBartForConditionalGeneration.from_pretrained(model_path)
    model.to(device)
    tokenizer = MBart50TokenizerFast.from_pretrained(model_path, src_lang="en_XX")
    return model, tokenizer

@st.cache(persist=True,allow_output_mutation=True,show_spinner=True,suppress_st_warning=True)
def translate(source):
    if source in database:
        translation = database[source]
    else:
        model_inputs = tokenizer(source, return_tensors="pt", max_length=1024, truncation=True, padding="max_length")
        model_inputs = {k: v.to(device) for k, v in model_inputs.items()}

        generated_tokens = model.generate(
            **model_inputs,
            forced_bos_token_id=tokenizer.lang_code_to_id["vi_VN"]
        )
        translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

    with jsonlines.open(history_path, mode='a') as writer:
        writer.write({"time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "source": source, "translation": translation, })
    history.append({"time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "source": source, "translation": translation, })

    return translation

@st.cache(persist=True,allow_output_mutation=True,show_spinner=True,suppress_st_warning=True)
def load_history(history_path):
    with jsonlines.open(history_path) as reader:
        history = [obj for obj in reader]
    database = {obj["source"]: obj["translation"] for obj in history}
    return history, database

st.set_page_config(
    page_title="mBART50 English-Vietnamese Translation",
    page_icon="🌏",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("English Vietnamese Translation")
st.info('✨ This model is built with effort and tears 😉')
st.text("First enter the English sentence in the textbox below. \nThen click on the button to translate the text.")
        
with st.spinner(f"Loading model... 💫"): 
    model, tokenizer = load_model()
    history, database = load_history()

translate_tab, history_tab = st.tabs(["Translate", "History"])

with translate_tab:
    st.markdown("## 📝 Input")
    source = st.text_area("- ", height=200, max_chars=5000, help="Enter the English sentence here")

    if st.button("Translate"):
        with st.spinner(f"Generating Transcript... 💫"):
            transcript = translate(source)
            if transcript is not None:
                st.markdown("## 🌏 Translation")         
                st.info(transcript)
            else:
                st.error("Error: No transcript generated")

            st.success('✅ Successful !!')
            
with history_tab:
    st.markdown("## 📜 History")
    st.dataframe(pd.DataFrame(history, columns=["time", "source", "translation"]), use_container_width=True)