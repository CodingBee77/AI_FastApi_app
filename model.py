from transformers import ViltProcessor, ViltForQuestionAnswering

# import requests
from PIL import Image


processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

# prepare image + question
# url = "https://www.sciencenews.org/wp-content/uploads/2023/06/071523_reviews_feat-1030x580.jpg"
# image = Image.open(requests.get(url, stream=True).raw)
# text = "How many bears are there?"


def model_pipeline(text: str, image: Image):
    # prepare inputs
    encoding = processor(image, text, return_tensors="pt")

    # forward pass
    outputs = model(**encoding)
    logits = outputs.logits
    idx = logits.argmax(-1).item()

    return model.config.id2label[idx]
