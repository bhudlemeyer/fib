
FROM tiangolo/uwsgi-nginx-flask:python3.6

ARG PORT
ENV LISTEN_PORT $PORT

EXPOSE $PORT

COPY ./app /app
