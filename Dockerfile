
FROM tiangolo/uwsgi-nginx-flask:python3.6

ARG PORT=8080
ENV LISTEN_PORT $PORT

EXPOSE $PORT

COPY ./app /app
