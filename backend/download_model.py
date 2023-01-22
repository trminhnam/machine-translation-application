import gdown
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

# gdown.download(
#     "https://drive.google.com/file/d/1vRyq2OBsVTt9NRaea4NGtGhifb1VdC2I&confirm=t", 
#     "mbart-large-50-one-to-many-mmt.zip",
#     fuzzy=True,
#     quiet=False
# )

tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt", src_lang="en_XX")
model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")

tokenizer.save_pretrained("models/mbart-large-50-one-to-many-mmt")
model.save_pretrained("models/mbart-large-50-one-to-many-mmt")