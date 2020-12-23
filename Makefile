.DEFAULT_GOAL := help
.PHONY: help build build-test

unit-test:
	pytest test/unit

build:
	docker build . -t docker.pkg.github.com/thoughtworks-dps/poc-va-api/poc-va-api:$(GIT_HASH)

app:build
	docker run --env SEM_VERSION="1.0.0" --env GIT_HASH="a1b2c3d45e" --name va-api -d -p 5000:5000 docker.pkg.github.com/thoughtworks-dps/poc-va-api/poc-va-api:$(GIT_HASH)

build-test:
	docker build -t integration:latest -f Dockerfile.integration_test .

integration-test:build-test
	docker run --network container:va-api integration:latest pytest test/integration

swagger-test:
	docker-compose -f docker-compose-swagger-test.yml up --exit-code-from swagger-test

smoke-test:
	./smoke-test.sh $(HOST)

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' Makefile | sed -n 's/^\(.*\): \(.*\)##\(.*\)/\1:\3/p'