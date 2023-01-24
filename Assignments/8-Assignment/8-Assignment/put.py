from kafka import KafkaProducer
from time import sleep

producer = KafkaProducer(bootstrap_servers =['localhost:9092'])
#key_bytes = bytes('MYID', encoding='utf-8')
#value_bytes = bytes('A20506653', encoding='utf-8')
producer.send('sample', key=bytes('MYID', encoding='utf-8'), value=bytes('A20506653', encoding='utf-8'))
producer.send('sample', key=bytes('MYNAME', encoding='utf-8'), value=bytes('Ramya Krishnan', encoding='utf-8'))
producer.send('sample', key=bytes('MYEYECOLOR', encoding='utf-8'), value=bytes('Brown', encoding='utf-8'))
sleep(5)
producer.close()