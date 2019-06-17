FROM centos:7.6.1810

LABEL maintainer="David Duenn <davidduenn@gmail.com>"

RUN yum update -y; yum clean all
RUN yum install -y epel-release gcc gcc-c++ gdb git make python-devel tmux tree vim
RUN yum install -y ack python-pip # depend on epel-release installation
RUN pip install --upgrade pip
RUN pip install python-redis redis

RUN cd /home/; git clone https://github.com/davidduenn/tic-tac-toe/

RUN sed -i 's/localhost/ttt_redis/' /home/tic-tac-toe/main.py

ENTRYPOINT ["/bin/bash"]
