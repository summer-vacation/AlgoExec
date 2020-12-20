# -*- coding: utf-8 -*-
"""
File Name:    demo1.py
Author :      jynnezhang
Date:         2020/12/11 2:02 下午
Description:
"""


from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
offsets = []


def out_put(m):
    print(m)


def store_offset(rdd):
    global offsets
    offsets = rdd.offsetRanges()
    return rdd


def print_offset(rdd):
    for o in offsets:
        print("%s %s %s %s %s" % (o.topic, o.partition, o.fromOffset, o.untilOffset, o.untilOffset - o.fromOffset))


if __name__ == "__main__":
    spark = SparkSession\
            .builder\
            .appName("PythonWordCount") \
            .master("local") \
            .getOrCreate()

    sc = spark.sparkContext
    ssc = StreamingContext(sc, 5)
    sc.setCheckpointDir("/home/hadoop/log/kafka")

    def updateFunc(new_values, last_sum):
        return sum(new_values) + (last_sum or 0)
    # kafkaStream = KafkaUtils.createStream(ssc, \
    # [ZK quorum], [consumer group id], [per-topic number of Kafka partitions to consume])
    msg_stream = KafkaUtils.createDirectStream(ssc, ['test'],
                                               kafkaParams={"metadata.broker.list": "mini1:9092,"})
    result = msg_stream.map(lambda x: x[1]).flatMap(lambda x: x.split(" ")).map(lambda x: (x, 1)).updateStateByKey(updateFunc,sc.defaultParallelism)
    msg_stream.transform(store_offset,).foreachRDD(print_offset)
    result.pprint()
    ssc.start()
    ssc.awaitTermination()
