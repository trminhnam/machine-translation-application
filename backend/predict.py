import warnings

import gdown
import torch
from transformers import MBart50TokenizerFast, MBartForConditionalGeneration

warnings.filterwarnings("ignore")

model_path = r"models/mbart-large-50-one-to-many-mmt"

def load_model():
    model = MBartForConditionalGeneration.from_pretrained(model_path)
    tokenizer = MBart50TokenizerFast.from_pretrained(model_path, src_lang="en_XX")
    return model, tokenizer

def tokenize(tokenizer, source):
    model_inputs = tokenizer(source, return_tensors="pt", max_length=1024, truncation=True, padding="max_length")
    return model_inputs

def predict(model, tokenizer, source, device='cpu'):
    model_inputs = tokenize(tokenizer, source)
    model_inputs = {k: v.to(device) for k, v in model_inputs.items()}

    generated_tokens = model.generate(
        **model_inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id["vi_VN"]
    )
    return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

def translate(source):
    model, tokenizer = load_model()
    return predict(model, tokenizer, source)

if __name__ == "__main__":
    source = "The quick brown fox jumps over the lazy dog"
    print(f"Source: {source}")
    print(f"Translation: {translate(source)}")
    