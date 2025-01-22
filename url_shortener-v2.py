from __future__ import with_statement
import contextlib
try:
	from urllib.parse import urlencode
except ImportError:
	from urllib import urlencode
try:
	from urllib.request import urlopen
except ImportError:
	pass
import sys


def make_tiny(url):
	request_url = ('http://tinyurl.com/api-create.php?' + 
	urlencode({'url':url}))
	with contextlib.closing(urlopen(request_url)) as response:
		return response.read().decode('utf-8')

def main():
	url = input("\n\t==> Enter the URL to shorten: ")
	tinyurl = make_tiny(url)
	print("\n\t..:: New url: " + tinyurl)
	print("\n")

if __name__ == '__main__':
	main()