FROM ubuntu:bionic

# Install Apps
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deluge-team/stable && \
    apt-get update && \
    apt-get install -y locales python3-pip deluged deluge-web deluge-console && \
    pip3 install flexget deluge-client

# Set the locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

# Dirs
RUN mkdir /deluge /downloads /flexget

# Init
COPY flexget.config.yml /flexget/config.yml
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]

# Ports and Volumes
EXPOSE 8112 58846 58946 58946/udp
VOLUME /deluge /downloads /flexget
