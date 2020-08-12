from tmdbMovies import tmdbMovies
from tmdbMovies import writeTmdbMoviesAsJSONNewLine

def indexableMovies(tmdb_source_file):
    """ Generates TMDB movies, similar to how ES Bulk indexing
        uses a generator to generate bulk index/update actions """
    for movieId, tmdbMovie in tmdbMovies(tmdb_source_file):
        print("Formatting %s" % movieId)
        try:
            releaseDate = None
            if 'release_date' in tmdbMovie and len(tmdbMovie['release_date']) > 0:
                releaseDate = tmdbMovie['release_date'] + 'T00:00:00Z'

            movie =  {'id': movieId,
                   'title': tmdbMovie['title'],
                   'poster_path': 'https://image.tmdb.org/t/p/w185' + tmdbMovie['poster_path'],
                   'overview': tmdbMovie['overview'],
                   'tagline': tmdbMovie['tagline'],
                   'directors': [director['name'] for director in tmdbMovie['directors']],
                   'cast': " ".join([castMember['name'] for castMember in tmdbMovie['cast']]),
                   'genres': [genre['name'] for genre in tmdbMovie['genres']],
                   'release_date': releaseDate,
                   'vote_average': float(tmdbMovie['vote_average']) if 'vote_average' in tmdbMovie else None,
                   'vote_count': int(tmdbMovie['vote_count']) if 'vote_count' in tmdbMovie else 0,
                   }

            addCmd = {
                        'index':{
                            '_index': 'tmdb',
                            '_id': movie['id']
                        }
                    }

            #addCmd = {"_index": 'tmdb',
            #          "_id": movie['id'],
            #          "_source": movie}

            yield addCmd, movie

        except KeyError as k: # Ignore any movies missing these attributes
            continue



if __name__ == "__main__":
    from sys import argv

    tmdb_source_file = argv[1]
    tmdb_es_file = argv[2]
    #writeTmdbMovies(list(indexableMovies(tmdb_source_file=tmdb_source_file)),tmdb_solr_file)

    writeTmdbMoviesAsJSONNewLine(list(indexableMovies(tmdb_source_file=tmdb_source_file)),tmdb_es_file)

    #movieDict = json.loads(open('tmdb.json').read())
    #reindex(movieDict=movieDict)
