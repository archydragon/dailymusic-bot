import argparse
from pathlib import Path

import bandcamp
import mastodon

def main():
    parser = argparse.ArgumentParser(
        description="Daily Music Mastodon bot",
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--fetch", action="store_true",
        help="fetch albums from Bandcamp and store information about them in the database")
    group.add_argument("-p", "--post", action="store_true",
        help="post one random album information to Mastodon")

    parser.add_argument("--db-path", metavar="PATH", type=Path,
        help="SQLite3 database file path")
    parser.add_argument("--albums", metavar="NUMBER", type=int,
        help="the number of albums to fetch and add to database (each album is fetched from a unique tag)")
    parser.add_argument("--instance", type=str,
        help="Mastodon instance hostname the bot lives on (just hostname, no schema and slashes!)")
    parser.add_argument("--token", type=str,
        help="Mastodon access token")
    parser.add_argument("--message-limit", metavar="LIMIT", type=int, default=500,
        help="Maximum message length allowed on Mastodon instance (default: 500)")

    args = parser.parse_args()
    error = ""

    if not args.db_path:
        error += "\n--db-path is not specified"
    if args.fetch and not args.albums:
        error += "\n--albums is not specified"
    if args.post:
        if not args.instance:
            error += "\n--instance is not specified"
        if not args.token:
            error += "\n--instance is not specified"

    if error != "":
        raise Exception(error)

    if args.fetch:
        print(f"Fetching {args.albums} albums from Bandcamp...")
        bandcamp.fetch_albums(args.albums, args.db_path)
    elif args.post:
        print(f"Posting to {args.instance} Mastodon instance...")
        mastodon.post(args.instance, args.token, args.message_limit, args.db_path)

    print("Done.")

if __name__ == '__main__':
    main()
