Elasticsearch Index for the [The Movie Database](http://themoviedb.com).

This repository is part of the _Think Like a Relevancy Engineer_ training provided by [OpenSource Connections](https://opensourceconnections.com/events/training/).

## Steps to get up and running:
- Download this repo
- Install the software (using either Docker or installing manually)
- Index the TMDB movie data
- Confirm Elasticsearch has the data
- Install Postman (optional)

# Download this repo

Download the zip from https://github.com/o19s/es-tmdb/archive/master.zip

or clone it:

```
git clone https://github.com/o19s/es-tmdb.git
```

After you have this repo, change into the newly created directory.

# Install Elasticsearch w/ Dependencies

## Docker option (recommended)

If you have [Docker](https://www.docker.com/products/docker-desktop) installed and running.

Make sure you have at least 4gb of memory available for Docker, the default is 2gb. See Docker's Preferences >>> Resources-tab, to adjust.

Linux/Windows:

```
docker-compose up
```

Give it a minute to fully boot up then use a browser to go to http://localhost:9200 and http://localhost:5601 to confirm Elasticsearch and Kibana are running.

## Local option

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

Linux:

```
bin/elasticsearch-plugin install -b http://es-learn-to-rank.labs.o19s.com/ltr-1.2.1-es7.6.2.zip
```

Windows:

```
bin\elasticsearch-plugin.bat install -b http://es-learn-to-rank.labs.o19s.com/ltr-1.2.1-es7.6.2.zip
```

5. Install the Querqy plugin for 7.6.2

```
bin/elasticsearch-plugin install -b https://repo1.maven.org/maven2/org/querqy/querqy-elasticsearch/1.2.es762.0/querqy-elasticsearch-1.2.es762.0.zip
```

6. Run Elasticsearch

```
bin/elasticsearch
```

7. In your browser, navigate to [http://localhost:9200](http://localhost:9200) to confirm Elasticsearch is running

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

Once Elasticsearch and Kibana are ready go, we need to create our example search index.

1. Load the data:

Unzip the `tmdb_es.json.zip` file first.

Linux/Windows:

```
unzip tmdb_es.json.zip
```

2. Index the data into Elasticsearch

Linux:

```
./index.sh
```

Windows:

```
powershell index.ps1
```

# Confirm Elasticsearch has TMDB movies

Run a [wildcard search](http://localhost:9200/tmdb/_search?q=*) and confirm you get results.

# Postman

[Postman](https://www.postman.com/) helps manage API requests. The examples from the TLRE slides exist here too as a Postman Collection (`es-postman-collection.json`). We like using Postman because it makes tinkering with query parameters nicer and we think it is a useful way to follow along as you learn about tuning search relevance.

If you want to use Postman during the TLRE class:

1. Download [Postman](https://www.postman.com/downloads/) for your OS
2. Open Postman and Import (top-menu >> File) `es-postman-collection.json`
3. Define a global variable (grey eye icon in the upper-right) `es_host` to point to your running Elasticsearch instance (default is `localhost:9200`)
4. Tinker with the base URL, Params or JSON Body (optional)
5. Press 'Send' (blue rectangle button right of URL bar)
