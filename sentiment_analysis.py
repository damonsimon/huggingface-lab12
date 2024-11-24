from transformers import pipeline

sentiment_pipeline = pipeline('sentiment-analysis')

result = sentiment_pipeline("GitHub 내에서 작업하는 방법은 정말 편리해요!")
print(result)
