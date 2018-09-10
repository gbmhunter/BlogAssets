#!/usr/bin/env bash

docker build -t blog-assets .

docker run -it blog-assets bash