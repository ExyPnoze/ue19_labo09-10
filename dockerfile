FROM python:3.8

WORKDIR /usr/app/src

COPY trivia.py /usr/app/src/trivia.py

RUN pip install requests

CMD ["python", "trivia.py"]
