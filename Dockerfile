FROM python:3.7-alpine

ADD . /autoclean

WORKDIR /autoclean

RUN pip install -r requirements.txt

CMD ["python", "autoclean.py"]