.DEFAULT_GOAL := help

include makefiles/ct.mk

TYPE_APP 		= apigateway
SERVICE_NAME 	= inventory
ENV 			= dev

PROJECT_NAME 	= ${TYPE_APP}-${SERVICE_NAME}-${ENV}

#Params ECR
NAME_PROJECT_APP = app-${PROJECT_NAME}
PORT_HOST = 8000

build.image: ## Build image for application.: make build.image
	@ docker build  \
		-f docker/Dockerfile \
		-t ${NAME_PROJECT_APP}:latest \
		./app \
		--no-cache

run.app: ## Run image for application.: make run.app
	@docker run \
		-p 8000:${PORT_HOST} -d ${NAME_PROJECT_APP}:latest\
