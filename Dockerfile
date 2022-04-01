FROM python:3.8

# ADD . /code

WORKDIR /code

RUN pip install flask
RUN pip install tensorflow
RUN pip install pandas

CMD ["python", "api.py"]