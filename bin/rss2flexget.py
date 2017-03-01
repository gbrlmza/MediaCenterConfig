#!/usr/bin/python3
'''
Convert ShAaNiG/MkvCage RSS feeds to be able to use them on flexget

Sample feeds:
- http://feeds.feedburner.com/MkvCage?format=xml
- https://www.shaanig.org/external.php?type=RSS2&forumids=30

E.g. calls:
- rss2flexget.py "http://feeds.feedburner.com/MkvCage?format=xml" /tmp/mkvcage.rss
- rss2flexget.py "https://www.shaanig.org/external.php?type=RSS2&forumids=30" /tmp/shaanig.rss

Usage in flexget:
task_name:
  exec:
    on_start:
      phase: rss2flexget.py "http://feeds.feedburner.com/MkvCage?format=xml" /tmp/mkvcage.rss
  rss:
    url: file:///tmp/mkvcage.rss

License:
Copyright (c) 2017 Gabriel Gonzalez
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Disclaimer:
New to python, sorry if the code sucks. All critics/suggestions are welcomed
'''
import re
import sys
import os
import xml.etree.ElementTree as et
import requests

def convert_items(xml):
    '''Convert items to link to torrent file/magnet link instead of forum page'''
    root = et.XML(xml)
    for item in root.iter('item'):
        content = item.find('{http://purl.org/rss/1.0/modules/content/}encoded')
        item.remove(content)

        # magnet link
        magnet_regex = re.compile(r'(?<=href=")magnet:?(.)*?(?=")')
        match = magnet_regex.search(content.text)
        if match:
            magnet_link = match.group(0)
            item.find('link').text = magnet_link
            continue # prefer magnet links if present (for MkvCage)

        # .torrent file
        torrent_regex = re.compile(r'(?<=href=")[0-9a-zA-Z-\/_\.:]*?\.torrent(?=")')
        match = torrent_regex.search(content.text)
        if match:
            torrent_link = match.group(0)
            item.find('link').text = torrent_link

    etree = et.ElementTree(root)
    return etree

def get_arguments():
    '''Get xml file path and rss url from arguments'''
    if len(sys.argv) != 3:
        sys.exit("USAGE: {0} <rss_url> <destination_file_path>".format(__file__))

    xml_file_path = sys.argv[2]
    if not os.path.exists(xml_file_path) and not os.access(os.path.dirname(xml_file_path), os.W_OK):
        sys.exit("Invalid file path {}".format(xml_file_path))

    rss_url = sys.argv[1]

    return [xml_file_path, rss_url]

def main():
    '''Main'''
    xml_file_path, rss_url = get_arguments()
    try:
        request = requests.get(rss_url)
        request.raise_for_status()
        if request.status_code == requests.codes.ok:
            etree = convert_items(request.text)
            etree.write(xml_file_path)
    except Exception as exc:
        print('There was an error accessing the feed: %s' % (exc))

main()