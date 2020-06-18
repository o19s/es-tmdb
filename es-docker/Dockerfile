FROM docker.elastic.co/elasticsearch/elasticsearch:7.6.2

RUN bin/elasticsearch-plugin install -b http://es-learn-to-rank.labs.o19s.com/ltr-1.2.1-es7.6.2.zip
RUN bin/elasticsearch-plugin install -b "https://repo1.maven.org/maven2/org/querqy/querqy-elasticsearch/1.2.es762.0/querqy-elasticsearch-1.2.es762.0.zip"
COPY --chown=elasticsearch:elasticsearch elasticsearch.yml /usr/share/elasticsearch/config/
RUN cat  /usr/share/elasticsearch/config/elasticsearch.yml

