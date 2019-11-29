#!/usr/bin/python3
import transmissionrpc

tc = transmissionrpc.Client('localhost', port=9091)

for torrent in tc.get_torrents():
	if torrent.status == 'stopped' and torrent.progress < 100:
		torrent.start()

