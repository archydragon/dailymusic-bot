import requests
import lxml.html
import datetime

# Using iPhone user agent, as mobile version of Bandcamp is much lighter and easier to parse.
USER_AGENT = 'Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1'

def get_xpath(url, xpath):
    r = requests.get(url, headers={'User-Agent': USER_AGENT})
    r.raise_for_status()
    root = lxml.html.fromstring(r.text)
    return root.xpath(xpath)

def if_url_exists(url):
    r = requests.head(url, headers={'User-Agent': USER_AGENT})
    return r.status_code < 400

def rfctime():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def limit_string(s, charlimit):
    if len(s) < charlimit:
        return s
    array = s.split(" ")
    output = ""
    i = 0
    while len(output) < charlimit:
        output += " " + array[i]
        i += 1
    return output[1:] + "…"
