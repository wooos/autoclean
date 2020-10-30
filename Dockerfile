FROM python:3.7-alpine

ADD . /autoclean

WORKDIR /autoclean

CMD ["python", "autoclean.py"]