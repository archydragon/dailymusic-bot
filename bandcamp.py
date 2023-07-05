import json
from itertools import islice
from random import shuffle, choice

import db
from tags import convert_keyword
from utils import get_xpath


BC_URL_BASE = 'https://bandcamp.com'
BC_URL_TAGS = f'{BC_URL_BASE}/tags'
MAX_RETRIES = 20


def fetch_albums(number, db_path):
    dbcon = db.init(db_path)

    xt = get_xpath(BC_URL_TAGS, '//*[@id="tags_cloud"]/*')
    # We only care about top-20 tags for now.
    urltags = list(islice(xt, 20))

    # Get required number of random tags
    shuffle(urltags)
    urltags = urltags[0:number]

    # Get random album for each of those tags.
    for rt in urltags:
        url = f'{BC_URL_BASE}{rt.get("href")}?tab=all_releases'
        results = get_xpath(url, '//*[@class="results"]/ul/*')
        chosen = False
        tried = 0
        # Trying to find an album we don't have in DB yet.
        while not chosen:
            # Endless loops are not nice, so.
            if tried > MAX_RETRIES:
                raise Exception(f"We already have too much stuff from '{rt.get('href')}'!")
            c = choice(results)
            album_url = c.find('a').get('href')
            chosen = not db.is_album_in_db(dbcon, album_url)
            tried += 1

        # Get album details from embedded JSON.
        x = get_xpath(album_url, '//script[@id="tralbum-jsonld"]/text()')
        jsonld = json.loads(x[0])
        artist = jsonld.get('byArtist').get('name')
        album = jsonld.get('name')
        description = jsonld.get('description')
        keywords = jsonld.get('keywords')

        # Only use the first paragraph of the description, and only if it's long enough.
        if description:
            description = description.split("\r\n\r\n")[0]
            if len(description) < 20:
                description = None

        # Convert fetched keywords for the album to normalized hashtags.
        tags = " ".join([convert_keyword(k) for k in keywords if convert_keyword(k) is not None])

        # Save album data to the database.
        db.add_album(dbcon, album_url, artist, album, tags, description)
        print(f"Added to DB: {album_url} - {artist} - {album}")
