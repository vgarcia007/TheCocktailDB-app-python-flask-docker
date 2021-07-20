FROM python:3.8
ADD . /web
WORKDIR /web
RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/bash", "/web/run-flask.sh"]
