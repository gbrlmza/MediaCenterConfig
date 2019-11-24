#!/bin/bash

# Start Deluge Daemon & Web-UI
/usr/bin/deluged -c /config
/usr/bin/deluge-web -c /config

# Flexget Daemon
/usr/local/bin/flexget -c /flexget/config.yml daemon start -d --autoreload-config

# Keep it running
tail -f /dev/null