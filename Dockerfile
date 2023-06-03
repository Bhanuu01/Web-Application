FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code1
ADD . /code1
COPY requirement.txt /code1/requirement.txt

RUN pip install -r requirement.txt

COPY . /code1

EXPOSE 8000
CMD ["python","manage.py","runserver"]
