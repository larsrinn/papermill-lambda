FROM lambci/lambda:python3.6

USER root

COPY requirements.txt .
RUN pip install -r requirements.txt
