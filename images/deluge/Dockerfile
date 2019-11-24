FROM ubuntu:bionic

# Set the locale
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8
ENV TZ America/Argentina/Mendoza

# Install Apps
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deluge-team/stable && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3-pip deluged deluge-web deluge-console && \
    pip3 install flexget

# Dirs
RUN mkdir /config /downloads /flexget

# Init
COPY flexget.config.yml /flexget/config.yml
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]

# Ports and Volumes
EXPOSE 8112 58846 58946 58946/udp
VOLUME /config /downloads /flexget

