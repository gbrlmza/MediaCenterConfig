#!/usr/bin/python3
import transmissionrpc

tc = transmissionrpc.Client('localhost', port=9091)
completedStatuses = ['seeding','stopped']

for torrent in tc.get_torrents():
    if torrent.status in completedStatuses and torrent.progress == 100:
        tc.remove(torrent.hashString, delete_data=False)

