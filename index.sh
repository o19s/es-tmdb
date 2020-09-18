#!/bin/bash

curl -XDELETE "http://localhost:9200/tmdb";

curl -XPUT "http://localhost:9200/tmdb/" -H 'Content-Type: application/json' --data-binary @schema.json;

curl -XPOST "http://localhost:9200/tmdb/_bulk" -H 'Content-Type: application/json' --data-binary @tmdb_es.json;
