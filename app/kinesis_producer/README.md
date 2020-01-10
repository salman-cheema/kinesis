# Kinesis Data Stream - Producer

This module contains code for the Kinesis Producer written using API Gateway.

## How to use

1. Update `config.py` file with apt Kinesis API URL and Kinesis Stream name.
2. To use the code, import the `KinesisProducer` class from `kinesis_producer.py`.
3. Call `KinesisProducer.put_record` method to insert a record on Kinesis Data Stream.

## Format for sending the Kinesis Data Stream record

- The record can be either a string or dictionary.
- It should be provided a message at `data` and a "key" preferably unique at `partition_key`.
