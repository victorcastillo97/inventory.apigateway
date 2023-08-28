.PHONY: build.image.app


build.image.app: ## Build image for application.: make build.image.app
	@ docker build  \
		-f docker/app/Dockerfile \
		-t ${IMAGE_APP} \
		--target prod \
		. \
		--no-cache