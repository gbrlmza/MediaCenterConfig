#!/bin/bash

# Start Transmission Daemon
# -T = No Auth
# -g = Config Dir
transmission-daemon -T -g /transmission

# Flexget Daemon
/usr/local/bin/flexget -c /flexget/config.yml daemon start -d --autoreload-config

# Keep it running
tail -f /dev/null