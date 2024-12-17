

FROM python:3.10:alpine


WORKDIR /auth


COPY ./requirements.txt /auth/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /auth/requirements.txt


COPY ./app /auth/app


CMD ["uvicorn", "main:app", "--port 8004"]