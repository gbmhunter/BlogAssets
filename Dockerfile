# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM ubuntu:bionic

# Use baseimage-docker's init system.
# CMD ["/sbin/my_init"]

# Set HOME directory
# RUN echo /root > /etc/container_environment/HOME

RUN apt-get update

RUN apt-get install -y libpcre3-dev
RUN apt-get install -y autotools-dev
RUN apt-get install -y automake
RUN apt-get install -y git-core
RUN apt-get install -y build-essential
RUN git clone https://github.com/swig/swig.git ~/swig/
WORKDIR /root/swig/
RUN ./autogen.sh
RUN ./configure

RUN apt-get install -y bison flex

RUN make
RUN make install



RUN apt-get install -y wget

WORKDIR /root/

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

# Make sure add command is as near the end as possible!
ADD . /root/BlogAssets

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]


# RUN wget https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86_64.sh
# RUN bash Anaconda3-4.2.0-Linux-x86_64.sh -b -p ~/anaconda
# RUN rm Anaconda3-4.2.0-Linux-x86_64.sh
# RUN echo 'export PATH="~/anaconda/bin:$PATH"' >> ~/.bashrc 


# RUN ~/anaconda/bin/conda update conda



# RUN useradd -ms /bin/bash user
# USER user
# WORKDIR /home/user

# # Install brew
# #RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"

# USER root

# Clean up APT when done.
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# USER user