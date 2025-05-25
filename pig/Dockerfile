FROM openjdk:8-jdk

# Instala wget y unzip
RUN apt-get update && apt-get install -y wget unzip && rm -rf /var/lib/apt/lists/*

# Variables de entorno
ENV HADOOP_HOME=/opt/hadoop
ENV PIG_HOME=/opt/pig
ENV PATH=$PATH:$HADOOP_HOME/bin:$PIG_HOME/bin
ENV PIG_CLASSPATH=$HADOOP_HOME/etc/hadoop

# Instala Hadoop 3.3.6
RUN wget https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz && \
    tar -xzf hadoop-3.3.6.tar.gz && mv hadoop-3.3.6 /opt/hadoop && rm hadoop-3.3.6.tar.gz

# Instala Pig 0.17.0
RUN wget https://archive.apache.org/dist/pig/pig-0.17.0/pig-0.17.0.tar.gz && \
    tar -xzf pig-0.17.0.tar.gz && mv pig-0.17.0 /opt/pig && rm pig-0.17.0.tar.gz

WORKDIR /data

COPY script.pig .

CMD ["pig", "-x", "local", "script.pig"]
