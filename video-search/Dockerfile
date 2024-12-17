FROM python:3.10:alpine


WORKDIR /video-search


COPY ./requirements.txt /auth/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /video-search/requirements.txt


COPY ./app /video-search/app


CMD ["uvicorn", "main:app", "--port 8006"]