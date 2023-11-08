FROM python:3.8

WORKDIR /app

COPY trivia.py /app/trivia.py

RUN pip install requests

CMD ["python", "trivia.py"]
