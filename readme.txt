This streaming processing system is developed using 

1-Apache Kafka
2-Apache Spark
3-Snowflake
4-Ubuntu operating system 22.04 (Cloud hosted)

*******************************
Snowflake account is required to create data warehouse . Snowflake is giving 30 days free trial 
please check https://www.snowflake.com/en/

*******************************

Install kafka
please check https://kafka.apache.org/

********************************

Install Spark
Please check https://spark.apache.org/

********************************
Snowflake Ingest SDK
Get Snowflake Ingest SDK
https://mvnrepository.com/artifact/net.snowflake/snowflake-ingest-sdk
select latest version (2.3.0 is the latest version at the time of this document preparation)
click on latest version to get the next url
https://mvnrepository.com/artifact/net.snowflake/snowflake-ingest-sdk/2.3.0
select jar from file section and download file.
Copy the jar file into kafka/libs folder
********************************************

Create sf_connect.properties file in kafka/config folder and change the parameters accordingly.

name=mykafkaconnectsnowflake
connector.class=com.snowflake.kafka.connector.SnowflakeSinkConnector
tasks.max=8
topics=(Kafka Topic Name)
snowflake.topic2table.map= (Topic:Table Table will be generated automatically by kafka)
buffer.count.records=1
buffer.flush.time=10
buffer.size.bytes=5
snowflake.url.name=(snowflake url – from snowflake account admin account url)
snowflake.user.name=(snowflake user name)
snowflake.private.key=(key pair authentication -private and public keys generated using openssl )
snowflake.private.key.passphrase=
snowflake.database.name=(Snowflake DB name)
snowflake.schema.name=(Snowflake schema name)
value.converter.schema.registry.url=
key.converter=com.snowflake.kafka.connector.records.SnowflakeJsonConverter
value.converter=com.snowflake.kafka.connector.records.SnowflakeJsonConverter

**********************************************************
Set kafka variable path in .bashrc file upto kafka bin folder
************************************************
Run zookeeper

zookeeper-server-start.sh config/zookeeper.properties

************************************************
Run kafka server in other ternimal

kafka-server-start.sh config/server.properties

************************************************

Run connect standalone to run kaka connector

connect-standalone.sh config/connect-standalone.properties config/sf_connect.properties

************************************************







