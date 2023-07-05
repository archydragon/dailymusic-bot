# Daily Music Mastodon bot

The source code for <a rel="me" href="https://botsin.space/@dailymusic">Daily Music</a> bot.

## What does it do?

It's purpose is very simple: to post good releases from Bandcamp to Mastodon, so people (including me) could enjoy some unexpected but nice music.

Fetching princinple: we read top-20 of the most popular tags on Bandcamp and then fetch one album for any three random ones.

## How exactly does it work?

`bot.py` is the main bot entrypoint which can do two things:

* fetch album information from Bandcamp
* post random album from fetched database to Mastodon

Those calls work as "fire and forget", you don't need to run the bot all the time. Right now, those are running as cron jobs on one of my machines.

## How to run it as it is?

You need either Python 3.8+ with pip, or Docker. SQLite is used as a "database" for kinda persistent data (mostly used to avoid accidental track double posting, and also some weak insurance that if Bandcamp changes their web site, and fetching will stop working, the posting will work for a bit longer before the things will break finally. I'm extremely lazy).

Also, obviously, you need a Mastodon app linked to your account you intent to post messages from. You can create it in `Settings > Development` in Mastodon web site. Only `write` OAuth scope is needed. Write access token for the application somewhere.

### Python

Requirements:

```bash
pip install lxml requests
```

Running:

```bash
# fetching
python bot.py --fetch --db-path dailymusic.db --albums 3

# posting
python bot.py --post --db-path dailymusic.db --instance botsin.space --token __________________________________
```

There is also an optional parameter `--message-limit` which might be handy if the instance you run your bot at has less strict message length limit than 500 characters.

### Docker

Requirements:

```bash
docker build -t dailymusic-bot .
```

Running:

```bash
# fetching
docker run --rm -v "/var/dailymusic-bot:/db" dailymusic-bot -f --db-path /db/dailymusic.db --albums 3

# posting
docker run --rm -v "/var/dailymusic-bot:/db" dailymusic-bot -p --db-path /db/dailymusic.db --instance botsin.space --token __________________________________
```

### License

MIT
