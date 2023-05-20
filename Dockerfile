FROM python:3

ADD .env .
ADD main.py .
ADD resources.py .
ADD checker.py .

RUN pip install discord python-dotenv

CMD [ "python", "./main.py" ]

