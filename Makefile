.DEFAULT_GOAL := help
.PHONY: help build

unit-test:
	pytest test/unit

build:
	docker build . -t docker.pkg.github.com/thoughtworks-dps/poc-va-api/$(GIT_HASH)

app:build
	docker run -d -p 5000:5000 docker.pkg.github.com/thoughtworks-dps/poc-va-api/$(GIT_HASH)

integration-test:
	docker-compose -f docker-compose-integration-test.yml up --exit-code-from integration-test

swagger-test:
	docker-compose -f docker-compose-swagger-test.yml up --exit-code-from swagger-test

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' Makefile | sed -n 's/^\(.*\): \(.*\)##\(.*\)/\1:\3/p'