# ES-TMDB 

Elasticsearch Index for the [The Movie Database](http://themoviedb.com).

Resources to stand up an EK stack for search relevance education, with an example index of movies.

## Steps to get up and running:
- Install the software (using either Docker or installing manually)
- Index the TMDB movie data
- Confirm Elasticsearch has the data
- Install Postman (optional)

# Install Elasticsearch w/ Dependencies

## Using Docker

Make sure you have at least 4gb of memory available for Docker, the default is 2gb. See Docker's Preferences >>> Resources-tab, to adust.

### Run containers

```
docker-compose up
```

Give it a minute to fully boot up then use a browser to go to http://localhost:9200 and http://localhost:5601 to confirm ES and Kibana running.

## Install Manually

### Elasticsearch

1. Download [Elasticsearch 7.6.2](https://www.elastic.co/downloads/past-releases/elasticsearch-7-6-2)
2. Unzip to where you'd like to run Elasticsearch
3. Add the following to config/elasticsearch.yml

```
http.cors.allow-origin: "/https?:\\/\\/(.*?\\.)?(quepid\\.com|splainer\\.io)/"
http.cors.enabled: true
indices.query.bool.max_clause_count: 10240
```

4. Install the LTR plugin for 7.6.2:

```
bin/elasticsearch-plugin install -b http://es-learn-to-rank.labs.o19s.com/ltr-1.2.1-es7.6.2.zip
```

4b. Install the Querqy plugin for 7.6.2

```
bin/elasticsearch-plugin install -b https://repo1.maven.org/maven2/org/querqy/querqy-elasticsearch/1.2.es762.0/querqy-elasticsearch-1.2.es762.0.zip
```

5. Run Elasticsearch

```
bin/elasticsearch
```

6. In your browser, navigate to [http://localhost:9200](http://localhost:9200) to confirm Elasticsearch is running

### Kibana

1. Download [Kibana 7.6.2](https://www.elastic.co/downloads/past-releases/kibana-7-6-2)

2. Unzip to where you'd like to run Kibana

3. Install the matching version of the [Kibana Analyze Plugin](https://github.com/johtani/analyze-api-ui-plugin)

```
bin/kibana-plugin install https://github.com/johtani/analyze-api-ui-plugin/releases/download/7.6.2/analyze_api_ui-7.6.2.zip
```

4. Run Kibana

```
bin/kibana
```

6. In your browser, navigate to [http://localhost:5601](http://localhost:5601) to confirm Kibana is running with the Analyze plugin included

# Index TMDB movies

Once Elasticsearch and Kibana are ready go, we need to build our example index.

1. Install [Python 3.6] or greater (https://www.python.org/downloads/)
2. Download <a download href="https://s3.amazonaws.com/es-learn-to-rank.labs.o19s.com/tmdb_2020-05-20.json">tmdb.json</a>, run:

`curl -o tmdb.json https://s3.amazonaws.com/es-learn-to-rank.labs.o19s.com/tmdb_2020-05-20.json` 

*Optional* Set-up a virtual ennvironment before install python libraries, run as separate lines:

```
python3 -m venv venv
source venv/bin/activate
```

3. Install [elasticsearch Python libraries](https://elasticsearch-py.readthedocs.io/en/master/) library, run:

`pip3 install elasticsearch`

4. Index the movies finally, run:

`python3 indexTmdb.py`


# Confirm Elasticsearch has TMDB movies

Run a [wildcard search](http://localhost:9200/tmdb/_search?q=*) and confirm you get results.

# Postman

[Postman](https://www.postman.com/) helps manage API requests. The examples from the TLRE slides exist here too as a Postman Collection (`es-TLRE-postman_collection.json`). Postman makes tinkering with query parameters easier and offers a structured way to follow along as you learn about tuning search relevance.

If you want to use Postman during the TLRE class:

1. Download [Postman](https://www.postman.com/downloads/) for your OS
2. Open Postman and Import (top-menu >> File) `es-postman-collection.json`
3. Define a global variable (grey eye icon in the upper-right) `es_host` to point to your running Elasticsearch instance (default is `localhost:9200`)
4. Tinker with the base URL, Params or JSON Body (optional)
5. Press 'Send' (blue rectangle button right of URL bar)

