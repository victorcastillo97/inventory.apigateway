.DEFAULT_GOAL := help

include makefiles/ct.mk

TYPE_APP 		= apigateway
SERVICE_NAME 	= inventory
ENV 			= dev

PROJECT_NAME 	= ${TYPE_APP}-${SERVICE_NAME}-${ENV}

#Params ECR
NAME_PROJECT_APP = app-${PROJECT_NAME}

IMAGE_APP = ${NAME_PROJECT_APP}:latest

build.image: ## Build image for application.: make build.image
	@ docker build  \
		-f docker/Dockerfile \
		-t ${NAME_PROJECT_APP}:latest \
		./app

run.app: ## Run image for application.: make run.app
	@docker run \
		-p 8000:8000 -d ${NAME_PROJECT_APP}:latest\
