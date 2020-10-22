.DEFAULT_GOAL := help
.PHONY: help

app:
#	build
#	docker-compose -f docker-compose-app.yml up

integration-test:
#	app
#	docker-compose -f docker-compose-integration-test.yml up

swagger-test:
#	app
#	docker-compose -f docker-compose-swagger-test.yml up

build:
	#docker build . -t docker.pkg.github.com/thoughtworks-dps/poc-va-api/poc-va-api:blah

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' Makefile | sed -n 's/^\(.*\): \(.*\)##\(.*\)/\1:\3/p'