Elasticsearch Index for the [The Movie Database](https://www.themoviedb.org/).

This repository is part of the _Think Like a Relevancy Engineer_ training provided by [OpenSource Connections](https://opensourceconnections.com/events/training/).

## Steps to get up and running:
- Download this repo
- Install the software (using either Docker or installing manually)
- Index the TMDB movie data
- Confirm Elasticsearch has the data
- Install Postman (optional)

# Download this repo

Download the zip from https://github.com/o19s/es-tmdb/archive/master.zip, and you will get the file es-tmdb-master.zip. Unzip this file, resulting in the directory es-tmdb-master.

After you have this download, change into the newly created directory.

# Install Elasticsearch w/ Dependencies

## Docker option (recommended)

If you have [Docker](https://www.docker.com/products/docker-desktop) installed and running.

Make sure you have at least 4gb of memory available for Docker, the default is 2gb. See Docker's Preferences >>> Resources-tab, to adjust.

Linux/Windows/Mac:

```
docker-compose up
```

Give it a minute to fully boot up then use a browser to go to http://localhost:9200 and http://localhost:5601 to confirm Elasticsearch and Kibana are running.

## Local option

### Elasticsearch

1. Download [Elasticsearch 7.16.2](https://www.elastic.co/downloads/past-releases/elasticsearch-7-16-2)
2. Unzip to where you'd like to run Elasticsearch
3. Add the following to config/elasticsearch.yml

```
http.cors.allow-origin: "/https?:\\/\\/(.*?\\.)?(quepid\\.com|splainer\\.io)/"
http.cors.enabled: true
indices.query.bool.max_clause_count: 10240
```

4. Run Elasticsearch

```
bin/elasticsearch
```

5. In your browser, navigate to [http://localhost:9200](http://localhost:9200) to confirm Elasticsearch is running

### Kibana

1. Download [Kibana 7.16.2](https://www.elastic.co/downloads/past-releases/kibana-7-16-2)

2. Unzip to where you'd like to run Kibana

3. Install the matching version of the [Kibana Analyze Plugin](https://github.com/johtani/analyze-api-ui-plugin)

```
bin/kibana-plugin install https://github.com/johtani/analyze-api-ui-plugin/releases/download/7.16.2/analyzeApiUi-7.16.2.zip
```

4. Run Kibana

```
bin/kibana
```

6. In your browser, navigate to [http://localhost:5601](http://localhost:5601) to confirm Kibana is running with the Analyze plugin included

# Index TMDB movies

Once Elasticsearch and Kibana are ready go, we need to create our example search index.

Linux/Mac:

```
./index.sh
```

Windows:

```
powershell index.ps1
```

If you don't have admin permissions to run PowerShell scripts, then open up the PowerShell ISE application as an administrator.  Then switch to the downloaded code directory and cut and paste the contents of `index.ps1` into the console to work around this issue.

# Confirm Elasticsearch has TMDB movies

Run a [wildcard search](http://localhost:9200/tmdb/_search?q=*) and confirm you get results.

# Postman

[Postman](https://www.postman.com/) helps manage API requests. The examples from the TLRE slides exist here too as a Postman Collection (`es-postman-collection.json`). We like using Postman because it makes tinkering with query parameters nicer.

We will mainly Kibana's DevTools for tinkering, but if you already familiar with Postman you can use that and get similar milage.

If you want to use Postman during the TLRE class:

1. Download [Postman](https://www.postman.com/downloads/) for your OS
2. Open Postman and Import (top-menu >> File) `es-postman-collection.json`
3. Define a global variable (grey eye icon in the upper-right) `es_host` to point to your running Elasticsearch instance (default is `localhost:9200`)
4. Tinker with the base URL, Params or JSON Body (optional)
5. Press 'Send' (blue rectangle button right of URL bar) to Search!
