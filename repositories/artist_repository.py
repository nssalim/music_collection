from models.artist import Artist
from models.album import Album
from db.run_sql import run_sql

# CREATE
def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    artist.id = id
    return artist

  


