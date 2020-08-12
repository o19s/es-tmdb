import json
from io import StringIO


def rawTmdbMovies(tmdb_source_file):
    return json.load(open(tmdb_source_file))


def writeTmdbMoviesAsJSONNewLine(rawMoviesJson, path):
    with open(path, 'w') as f:
        #json.dump(rawMoviesJson, f)
        for record in rawMoviesJson:
            f.write(json.dumps(record[0]))
            f.write('\n')
            f.write(json.dumps(record[1]))
            f.write('\n')


def tmdbMovies(tmdb_source_file):
    tmdbMovies = rawTmdbMovies(tmdb_source_file)
    for movieId, tmdbMovie in tmdbMovies.items():
        yield (movieId, tmdbMovie)
