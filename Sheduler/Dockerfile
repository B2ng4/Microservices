FROM python:3.10:alpine


WORKDIR /Sheduler


COPY ./requirements.txt /auth/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /Sheduler/requirements.txt


COPY ./app /Sheduler/app


CMD ["uvicorn", "main:app", "--port 8003"]