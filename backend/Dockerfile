FROM python:3

WORKDIR /usr/src/app

COPY server/ ./
COPY . .
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

CMD [ "poetry", "run", "python", "./server/main.py" ]
