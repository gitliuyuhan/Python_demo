#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
from kafka import KafkaConsumer

import kafka_send

consumer = KafkaConsumer(\
        'test',\
        group_id='1',\
        bootstrap_servers=['{kafka_host}:{kafka_port}'.format(\
        kafka_host=kafka_send.kafka_host,\
        kafka_port=kafka_send.kafka_port)]\
        )

for msg in consumer:
    print msg
    print msg.value
    try:
        content = json.loads(msg.value)
    except Exception,e:
        print e
    else:
        print content
