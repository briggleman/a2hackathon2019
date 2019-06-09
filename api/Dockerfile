FROM python:3.7.3

ENV PYTHONUNBUFFERED 1
ENV PORT 8080
ENV PBR_VERSION ${CI_COMMIT_TAG}
ENV HOME /app

WORKDIR ${HOME}

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE ${PORT} 8545

CMD python runserver.py --port $PORT --host 0.0.0.0
