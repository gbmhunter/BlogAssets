#!/usr/bin/env bash

# Build a docker image using the Dockerfile in the current directory
docker build -t blog-assets .

# Run the container, and enter to the bash prompt. Mount the BlogAssets directory so we
# can inspect output on the host machine (e.g. images)
docker run -it -v $PWD:/root/BlogAssets blog-assets bash