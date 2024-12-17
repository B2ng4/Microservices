


FROM python:3.10:alpine


WORKDIR /Chat-bot


COPY ./requirements.txt /Chat-bot/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /Chat-bot/requirements.txt


COPY ./app /Chat-bot/app


CMD ["python", "main.py"]