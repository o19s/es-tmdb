import json


def indexableMovies():
    """ Generates TMDB movies, similar to how ES Bulk indexing
        uses a generator to generate bulk index/update actions """
    from tmdbMovies import tmdbMovies
    for movieId, tmdbMovie in tmdbMovies():
        try:
            releaseDate = None
            if 'release_date' in tmdbMovie and len(tmdbMovie['release_date']) > 0:
                releaseDate = tmdbMovie['release_date'] + 'T00:00:00Z'

            if movieId == '374430':
                print(tmdbMovie['vote_count'])

            yield {'id': movieId,
                   'title': tmdbMovie['title'],
                   'overview': tmdbMovie['overview'],
                   'tagline': tmdbMovie['tagline'],
                   'directors': [director['name'] for director in tmdbMovie['directors']],
                   'cast': " ".join([castMember['name'] for castMember in tmdbMovie['cast']]),
                   'genres': [genre['name'] for genre in tmdbMovie['genres']],
                   'release_date': releaseDate,
                   'vote_average': float(tmdbMovie['vote_average']) if 'vote_average' in tmdbMovie else None,
                   'vote_count': int(tmdbMovie['vote_count']) if 'vote_count' in tmdbMovie else 0,
                   }
        except KeyError as k: # Ignore any movies missing these attributes
            print(k)
            continue

def reindex(es, movieDict={}, schema='schema.json', index='tmdb'):
    import elasticsearch.helpers
    settings = json.load(open(schema))

    es.indices.delete(index, ignore=[400, 404])
    es.indices.create(index, body=settings)

    def bulkDocs(movieDict):
        for movie in indexableMovies():
            addCmd = {"_index": index,
                      "_type": "movie",
                      "_id": movie['id'],
                      "_source": movie}
            yield addCmd
            if 'title' in movie:
                print("%s added to %s" % (movie['title'], index))

    elasticsearch.helpers.bulk(es, bulkDocs(movieDict), chunk_size=1)

if __name__ == "__main__":
    from elasticsearch import Elasticsearch
    from sys import argv

    esUrl='http://localhost:9200'
    schema='schema.json'
    if len(argv) > 1:
        schema = argv[1]
    es = Elasticsearch(esUrl, timeout=30)
    movieDict = json.loads(open('tmdb.json').read())
    reindex(es, movieDict=movieDict, schema=schema)

