import requests, requests.exceptions
import time

import db
from utils import limit_string

COMMON_TAGS = "#music #dailymusic"

def post(instance, token, message_length_limit, db_path):
    dbcon = db.init(db_path)
    (album_url, artist, album, tags, description, _, _, _) = db.get_random_album(dbcon)
    if description:
        limit = message_length_limit - len(album_url) - len(artist) - len(album) - len(tags) - len(COMMON_TAGS) - 20
        description = limit_string(description, limit) + "\n\n"
    else:
        description = ""

    url = f"https://{instance}/api/v1/statuses"
    auth = {"Authorization": f"Bearer {token}"}
    message = f"""{artist} — {album}
{album_url}

{description}{COMMON_TAGS} {tags}"""
    try:
        r = requests.post(url, data={'status': message}, headers=auth)
        r.raise_for_status()
    except requests.exceptions.HTTPError as ex:
        if r.status_code != 422:
            raise ex
        else:
            print(message)

    db.mark_album_as_posted(dbcon, album_url)
    print(f"Album {album_url} posted to Mastodon")
