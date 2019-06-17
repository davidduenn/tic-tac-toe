FROM centos:7.6.1810

LABEL maintainer="David Duenn <davidduenn@gmail.com>"

RUN yum update -y; yum clean all
RUN yum install -y ack epel-release gcc gcc-c++ gdb git make python-redis tmux tree vim

RUN cd /home/; git clone https://github.com/davidduenn/tic-tac-toe/
