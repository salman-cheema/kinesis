'''
'Consumer get messages from OCR Job , Update the Staus in mongodb'

'''
import time
import base64
import json
import logging

from standard_consumer_functions import process_message,\
    get_shard_iterators
from standard_kinesis_consumers_functions import set_logger,\
      get_records, get_kinesis_api_url
import status_config as config
import consumers_constants as const

# Set logger
logger = set_logger(config.STREAM_NAME)

kinesis_status_url = get_kinesis_api_url(config.STREAM_NAME, config.BASE_URL)

# Get shards
shard_iterators, shard_sequence_numbers, shards = \
    get_shard_iterators(kinesis_status_url, config.STREAM_NAME)

logger.info(const.STARTING_STATUS_STREAM)

while True:
    try:
        for i, shard_iterator in enumerate(shard_iterators):
            response_records = get_records(kinesis_status_url, shard_iterator)
            if const.RECORDS in response_records:
                for record in response_records[const.RECORDS]:
                    message = base64.b64decode(record[const.DATA]).decode(const.UTF_8)
                    sequence_number = record[const.SEQUENCE_NUMBER]
                    shard_sequence_numbers[shards[i]] = sequence_number
                    logger.info(message)
                    process_message(message)
                    with open(config.STREAM_NAME + const.CHECKPOINT, const.WRITE) \
                            as outfile:
                        json.dump(shard_sequence_numbers, outfile)
            else:
                logger.error(str(response_records))
            shard_iterators[i] = response_records[const.NEXT_SHARD_ITERATOR]
            time.sleep(1)
    except Exception as identifier:
        logging.exception(str(identifier))
        time.sleep(60)
