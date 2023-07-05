import sqlite3
from random import choice

from utils import rfctime

DB_TABLE = "albums"

def init(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute(f"""create table if not exists {DB_TABLE} (
        url,
        artist,
        album,
        tags,
        description,
        status,
        added,
        updated)
    """)
    return con

def is_album_in_db(con, album_url):
    cur = con.cursor()
    cur.execute(f"select url from {DB_TABLE} where url='{album_url}'")
    return cur.fetchone() is not None

def add_album(con, album_url, artist, album, tags, description):
    cur = con.cursor()
    now = rfctime()
    query = f"""
        insert into {DB_TABLE} values (
            '{album_url}',
            '{artist.replace("'", "''")}',
            '{album.replace("'", "''")}',
            '{tags}',
            '{description.replace("'", "''") if description else ""}',
            'new',
            '{now}',
            '{now}')
    """
    cur.execute(query)
    con.commit()

def get_random_album(con):
    cur = con.cursor()
    cur.execute(f"select * from {DB_TABLE} where status = 'new'")
    data = cur.fetchall()
    if data == []:
        raise Exception("Nothing to post, ether DB is empty, or we've posted everything we had in queue already.")
    return choice(data)

def mark_album_as_posted(con, album_url):
    cur = con.cursor()
    now = rfctime()
    cur.execute(f"update {DB_TABLE} set status='posted', updated='{now}' where url='{album_url}'")
    con.commit()

def mark_album_as_deleted(con, album_url):
    cur = con.cursor()
    now = rfctime()
    cur.execute(f"update {DB_TABLE} set status='deleted', updated='{now}' where url='{album_url}'")
    con.commit()
