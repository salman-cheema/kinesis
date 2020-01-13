'''
'Consumer get messages,trigger OCR service.

'''
import time
import base64
# import logging
import json
# from os import path
from standard_consumer_functions import ocr_service, get_shard_iterators
from standard_kinesis_consumers_functions import set_logger,\
    get_records, get_kinesis_api_url
import ocr_config as config
import consumers_constants as const

import random
import pprint

# Set logger
logger = set_logger(config.STREAM_NAME)

kinesis_ocr_url = get_kinesis_api_url(config.STREAM_NAME, config.BASE_URL)


# Get shards
shard_iterators, shard_sequence_numbers, shards = \
    get_shard_iterators(kinesis_ocr_url, config.STREAM_NAME)


logger.info(const.STARTING_OCR_STREAM)


while True:
    try:
        for i, shard_iterator in enumerate(shard_iterators):
            response_records = get_records(kinesis_ocr_url, shard_iterator)
            if const.RECORDS in response_records:
                for record in response_records[const.RECORDS]:
                    message = base64.b64decode(
                        record[const.DATA]).decode(const.UTF_8)
                    sequence_number = record[const.SEQUENCE_NUMBER]
                    shard_sequence_numbers[shards[i]] = sequence_number
                    logger.info(const.NEW_MESSAGE)
                    logger.info(message)
                    ocr_service(message)
                    with open(config.STREAM_NAME + const.CHECKPOINT, const.WRITE) \
                            as outfile:
                        json.dump(shard_sequence_numbers, outfile, indent=4)
            else:
                logger.error(str(response_records))
            if response_records.get('__type') == 'ExpiredIteratorException':
                # Get shards
                shard_iterators, shard_sequence_numbers, shards = \
                    get_shard_iterators(kinesis_ocr_url, config.STREAM_NAME)
            else:
                shard_iterators[i] = response_records[const.NEXT_SHARD_ITERATOR]

            # To manage throttling
            time.sleep(1)
    except Exception as identifier:
        logger.exception(str(identifier))
        # To manage throttling
        time.sleep(60)
