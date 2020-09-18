# Powershell script for Windows 10 and above to index the TMDB JSON file.

$schema = Get-Content 'schema.json';
$data = Get-Content 'tmdb_es.json';

Invoke-WebRequest -Method DELETE -Uri 'http://localhost:9200/tmdb';

Invoke-WebRequest -Method PUT -Uri 'http://localhost:9200/tmdb' -ContentType 'application/json' -UseBasicParsing -Body $schema;

Invoke-WebRequest -Method POST -Uri 'http://localhost:9200/tmdb' -ContentType 'application/json' -UseBasicParsing -Body $data;