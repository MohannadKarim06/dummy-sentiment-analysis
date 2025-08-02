# Stage 1 "Build Stage"
FROM python:3.9-slim-buster AS builder

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m textblob.download_corpora

COPY . .



# Stage 2 "Produciton Stage"
FROM python:3.9-slim-buster AS production

WORKDIR /app

COPY --from=builder /usr/local /usr/local

COPY --from=builder /app .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



