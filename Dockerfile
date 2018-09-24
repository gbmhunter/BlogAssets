FROM ubuntu:bionic

# This allows apt-get to recognize packages when calling install
RUN apt-get update

###################################################################################################
# INSTALL SWIG
###################################################################################################
RUN apt-get install -y libpcre3-dev
RUN apt-get install -y autotools-dev
RUN apt-get install -y automake
RUN apt-get install -y git-core
RUN apt-get install -y build-essential
RUN apt-get install -y bison flex
RUN git clone https://github.com/swig/swig.git /opt/swig/
WORKDIR /opt/swig/
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install


###################################################################################################
# INSTALL ANACONDA
###################################################################################################
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

# Fix matplotlib issue
RUN apt-get install -y libgl1-mesa-glx

###################################################################################################
# INSTALL VALGRIND
###################################################################################################

# Used by ProfilingValgrind example
RUN apt-get install -y valgrind

###################################################################################################
# INSTALL CMAKE
###################################################################################################

RUN apt-get install -y cmake

###################################################################################################
# INSTALL msgpack
###################################################################################################

# This is required for building pybind11 projects
RUN pip install msgpack

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]


