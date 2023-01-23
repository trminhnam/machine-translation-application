from typing import ContextManager
from flask import Flask, render_template, request, jsonify
from googletrans import Translator
import torch
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model_path = r"models/mbart-large-50-one-to-many-mmt"
device = 'cpu' if not torch.cuda.is_available() else 'cuda'
history_path = r"data/history.jsonl"

model = MBartForConditionalGeneration.from_pretrained(model_path)
model.to(device)
tokenizer = MBart50TokenizerFast.from_pretrained(model_path, src_lang="en_XX")

app = Flask(__name__)

translator = Translator()

def translate(text):
    # https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group
    # translation = translator.translate(text, dest='vi').text
    
    model_inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True, padding="max_length")
    model_inputs = {k: v.to(device) for k, v in model_inputs.items()}

    generated_tokens = model.generate(
        **model_inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id["vi_VN"]
    )
    translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]

    return translation

@app.route("/", methods=["GET"])
def home():
    return ("Hello World. To use the API, please make a POST request to /translation_api with the body containing the source text. The response will be a JSON object containing the translation.")

@app.route('/translation_api', methods=["GET", "POST"])
def translation_api():
    if request.method == "POST":
        data = request.get_json()
        source = data.get("source", None)
        print(source)

        result = translate(source)

        # send back the result to the client
        return jsonify(translation=result)
    else:
        return ("nothing")

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', 
#             port=8334, 
#             debug=True
#     )