from transformers import pipeline
from model.model_config import MODEL_NAME


class SentimentAnalyzer():
    def __init__(self, model_name=MODEL_NAME):
        self.classifier = pipeline("sentiment-analysis", model=model_name)

    def analyze(self, text):
        return self.classifier(text)
