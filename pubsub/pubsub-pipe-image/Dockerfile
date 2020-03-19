FROM python:2

RUN pip install --upgrade pip
RUN pip install tweepy
RUN pip install --upgrade google-api-python-client
RUN pip install python-dateutil

ADD twitter-to-pubsub2.py /twitter-to-pubsub2.py
ADD pubsub-to-bigquery2.py /pubsub-to-bigquery2.py
ADD controller.py /controller2.py
ADD utils2.py /utils2.py

CMD python controller2.py
