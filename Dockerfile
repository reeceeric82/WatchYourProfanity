FROM python:3

ADD .env /
ADD main.py /
ADD resources.py /
ADD requirement.txt /

RUN pip install discord.py python-dotenv

CMD [ "python", "./main.py" ]

