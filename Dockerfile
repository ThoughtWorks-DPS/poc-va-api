FROM golang:1.14

RUN git clone https://github.com/coredns/coredns.git /coredns
RUN cd /coredns && make

FROM python:3.8.6-slim
COPY --from=0 /coredns/coredns /coredns

EXPOSE 53 53/udp

ADD . /poc-va-api
WORKDIR /poc-va-api

RUN pip3 install -r requirements.txt

ENV FLASK_APP=/poc-va-api/src/app.py

CMD ["flask", "run",  "--host=0.0.0.0"]