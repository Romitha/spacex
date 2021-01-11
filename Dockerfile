FROM ubuntu:18.04
RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y 
RUN apt install libpq-dev -y
RUN apt-get install graphviz -y
RUN apt-get install  python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev -y
RUN apt-get install python-mysqldb -y
WORKDIR /
COPY . /
RUN pip3 install -r requirements.txt
CMD ["python3","manage.py","run"]
EXPOSE 5000/tcp  
