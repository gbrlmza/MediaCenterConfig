FROM ubuntu:bionic

# Install Apps
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y transmission-daemon locales python3-pip && \
    pip3 install flexget transmissionrpc requests python-telegram-bot

# Set Locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

# Dirs
RUN mkdir /transmission && \
    mkdir /flexget && \
    mkdir -p /data/torrent/completed && \
    mkdir -p /data/torrent/inprogress && \
    mkdir -p /data/torrent/watch

# Init
COPY flexget.config.yml /flexget/config.yml
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]

# Ports and Volumes
EXPOSE 8112 58846 58946 58946/udp
VOLUME /transmission /data /flexget
