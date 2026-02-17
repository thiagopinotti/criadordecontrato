FROM python:3.13

WORKDIR /app
COPY . /app

RUN pip install poetry && poetry install

EXPOSE 8501
CMD ["poetry", "run", "streamlit", "run", "sresrabrownies/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
