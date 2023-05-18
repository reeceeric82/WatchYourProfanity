FROM python:3

ADD .env .
ADD main.py .

RUN pip install discord python-dotenv

CMD [ "python", "./main.py" ]

