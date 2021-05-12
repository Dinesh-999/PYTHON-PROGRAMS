# URL Shortener with Python
# use in command line


import contextlib

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib import urlopen
import sys


def make_tiny(url):
    request_url = ('http://tinyurl.com/api-create.php?' +
                   urlencode({'url': url}))
    # print("Actual URL : " + request_url)
    with contextlib.closing(urlopen(request_url)) as response:
        return response.read().decode('utf-8')


def main():
    for tinyurl in map(make_tiny, sys.argv[1:]):
        print("Shortened URL : " + tinyurl)


if __name__ == '__main__':
    print("USAGE: (eg:) test2.py https://thecleverprogrammer.com/2021/01/09/digital-clock-with-python/")
    print("Use Command Line or Terminal\n")
    main()
