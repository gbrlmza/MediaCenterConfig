#!/bin/bash

# Start Deluge Daemon & Web-UI
/usr/bin/deluged -c /deluge
/usr/bin/deluge-web -c /deluge

# Flexget Daemon
/usr/local/bin/flexget -c /flexget/config.yml daemon start -d --autoreload-config

# Keep it running
tail -f /dev/null