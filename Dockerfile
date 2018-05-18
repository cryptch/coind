FROM cryptch/ubuntu:16.04

# Install python 3.6, hug need this version
RUN add-apt-repository -y ppa:jonathonf/python-3.6
RUN apt-get update && apt-get install -y python3.6 python3-pip

# Upgrade pip
RUN pip install --upgrade pip

# Add daemon
RUN cd /root/ && \
    wget https://github.com/VsyncCrypto/VSX/releases/download/v3.8.5.0/vsync-daemon-3.8.5.0-linux64.tar.gz && \
    tar -xvzf vsync-daemon-3.8.5.0-linux64.tar.gz && \
    rm vsync-daemon-3.8.5.0-linux64.tar.gz && \
    mv vsync* /usr/local/bin

# Add .conf
RUN mkdir /root/.vsync
COPY test/vsync.conf /root/.vsync/vsync.conf

# Open ports for vsync
EXPOSE 65010 65015

# Run daemon
CMD ['/usr/local/bin/vsyncd', '-daemon']