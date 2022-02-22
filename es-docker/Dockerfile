FROM docker.elastic.co/elasticsearch/elasticsearch:7.16.2

RUN bin/elasticsearch-plugin install -b https://github.com/o19s/elasticsearch-learning-to-rank/releases/download/v1.5.8-es7.16.2/ltr-plugin-v1.5.8-es7.16.2.zip
RUN bin/elasticsearch-plugin install -b "https://repo1.maven.org/maven2/org/querqy/querqy-elasticsearch/1.5.es7162.0/querqy-elasticsearch-1.5.es7162.0.zip"
COPY --chown=elasticsearch:elasticsearch elasticsearch.yml /usr/share/elasticsearch/config/
RUN cat  /usr/share/elasticsearch/config/elasticsearch.yml

