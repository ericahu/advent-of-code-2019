DOCKER_REPO       := ericahu/advent-of-code-2019
DOCKER_IID_FILE   := .iidfile
DOCKER_BUILD_ARGS := --build-arg registryLibrary=dockerhub.artifactory.ai.cba/library/
DOCKER_RUN        := docker run --rm \
										 -v $(shell pwd)/../data:/data \
										 -v $(shell pwd)/../app-neo4j:/app-neo4j \
										 $$(cat $(DOCKER_IID_FILE))

all: clean build join-data validate generate-cypher clean

build: $(DOCKER_IID_FILE)
$(DOCKER_IID_FILE):
	@docker build --iidfile=$@ -t $(DOCKER_REPO) .

join-data:
	@$(DOCKER_RUN) python /JoinData.py -i /data/csv -o /data/joined-roadmap-data.csv

validate: join-data
	@$(DOCKER_RUN) python /ValidateData.py -i /data/joined-roadmap-data.csv

generate-cypher:
	@$(DOCKER_RUN) python /GenerateCypher.py -i /data/joined-roadmap-data.csv -o /app-neo4j/import/roadmap-model.cql

clean::
	-rm -f $(DOCKER_IID_FILE)

.PHONY: all build validate clean
