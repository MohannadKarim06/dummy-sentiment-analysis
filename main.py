from fastapi import FastAPI, HTTPException
from textblob import TextBlob

app = FastAPI(
    title="Simple FastAPI App"
)


@app.post("/analyse_sentiment")
async def analyse_sentiment(text: str):

    if not text:
        raise HTTPException(status_code=400, detail="Need some text to analyse dumb ass!")

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity

    if polarity > 0:
        sentiment_label = "Positive"

    elif polarity < 0:
        sentiment_label = "Negative, How dare you say something negative to me ?!!"

    else:
        sentiment_label = "Neutural"


    return {
        "text": text,
        "polarity": polarity,
        "subjectivity": subjectivity,
        "sentiment_label": sentiment_label
    }



