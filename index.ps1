# PowerShell script for Windows 10 and above to index the TMDB JSON file.

if (-not (Test-Path -Path '.\tmdb_es.json')) {
  Expand-Archive -LiteralPath tmdb_es.json.zip -DestinationPath ./
}

$schema = Get-Content 'schema.json';
$data = Get-Content -Raw 'tmdb_es.json';

Invoke-WebRequest -Method DELETE -Uri 'http://localhost:9200/tmdb' -UseBasicParsing;

Invoke-WebRequest -Method PUT -Uri 'http://localhost:9200/tmdb' -ContentType 'application/json' -UseBasicParsing -Body $schema;

Invoke-WebRequest -Method POST -Uri 'http://localhost:9200/tmdb/_bulk' -ContentType 'application/json' -UseBasicParsing -Body $data;
