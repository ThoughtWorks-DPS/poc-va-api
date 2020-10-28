FROM python:3.7-slim AS python-env
ADD . /poc-va-api
WORKDIR /poc-va-api
RUN pip3 install -r requirements.txt

FROM gcr.io/distroless/python3-debian10
COPY --from=python-env /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
COPY --from=python-env /poc-va-api /poc-va-api

EXPOSE 5000 5000/tcp

ENV PYTHONPATH=/usr/local/lib/python3.7/site-packages
ENV FLASK_APP=/poc-va-api/src/app.py
WORKDIR /poc-va-api
USER 1001

CMD ["-m", "flask", "run", "--host=0.0.0.0"]