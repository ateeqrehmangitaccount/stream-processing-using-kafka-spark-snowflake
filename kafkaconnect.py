import kafka
from kafka import KafkaProducer
from json import dumps

kproducer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                          value_serializer=lambda x:dumps(x).encode('utf-8'))
                          data = {'product':product.productname, 'quantity': qty}
kproducer.send('firsttopic', value=data)