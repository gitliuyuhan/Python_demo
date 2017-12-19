#!/usr/bin/env python
# -*- coding:utf-8 -*-

from kafka import KafkaProducer

kafka_host = '127.0.0.1'
kafka_port = 9092

class KafkaSend:
    
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers = ['{kafka_host}:{kafka_port}'.format(\
                kafka_host = kafka_host,\
                kafka_port = kafka_port)])

    def sendMsg(self,topic,s):
        return self.producer.send(topic,s)

if __name__ == '__main__':

    k = KafkaSend()
    print k.sendMsg('test','hello')
