# Use a pipeline as a high-level helper
from PIL import Image
from transformers import pipeline

img = Image.open("C:\Users\AXW2KOR\Pictures\Tulips.jpg")
classifier = pipeline("image-classification", model="Falconsai/nsfw_image_detection")
classifier(img)

#Loading of model directly
import torch
from PIL import Image
from transformers import AutoModelForImageClassification, ViTImageProcessor

img = Image.open("C:\Users\AXW2KOR\Pictures\Tulips.jpg")
model = AutoModelForImageClassification.from_pretrained("Falconsai/nsfw_image_detection")
processor = ViTImageProcessor.from_pretrained('Falconsai/nsfw_image_detection')
with torch.no_grad():
    inputs = processor(images=img, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits

predicted_label = logits.argmax(-1).item()
model.config.id2label[predicted_label]


#file has been successfully updated
