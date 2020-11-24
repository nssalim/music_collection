from models.artist import Artist
from models.album import Album
from db.run_sql import run_sql

def save(album):
    sql = "INSERT INTO albums (artist_id, title, genre) VALUES (%s, %s, %s) RETURNING id"
    

