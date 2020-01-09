"""Standard functions for Kinesis Data Stream.

This file contains standardized functions for Kinesis Data Streams.
The main purpose of this file is to simplify the creation of producers,
and consumers.

# TODO: config.py gets updated after infrasturcture provisioning.

Note:
- To make changes to default values, make changes in the constants file.
- Constants file name: constants.py
"""

import json
import requests
from requests.exceptions import MissingSchema
import constants as const


# Kinesis Producer functions
def get_kinesis_api_url(stream_key: str, stream_config: dict,
                        logger) -> str:
    """Gets Kinesis API URL for the given stream.

    Arguments:
        stream_key {str} -- Key for the Kinesis Data Stream name.
        stream_config {dict} -- Configurations for the Kinesis Data Stream.
        logger {logging.RootLogger} -- logger.

    Raises:
        ValueError: [description]
        MissingSchema: [description]

    Returns:
        str -- Kinesis API URL to the given Kinesis Data Stream.
    """

    # Following will come from MongoDB.
    try:
        base_url = stream_config['baseUrl']
        stream_name = stream_config[stream_key]

        stream_url = base_url + stream_name

        res = requests.get(stream_url)

        if '__type' in res.json():
            if res.json()['__type'] == const.RESOURCE_NOT_FOUND_EXCEPTION:
                logger.error('''
                    Stream by given name doesn't exists
                    Please verify that the stream exists in Kinesis.
                ''')
            else:
                logger.error('''
                    Error type: {etype}.
                    Error message: {message}.
                '''.format(etype=res.json()['__type'],
                           message=res.json()['message']))

            raise Exception(res.json()['message'])
    except MissingSchema as e:
        logger.error('''
            Base URL schema is missing.
            Please verify that 'https://' is present before the URL.
        ''')

        raise e

    logger.info('Kinesis Data Stream API URL generated successfully.')
    return stream_url


def put_record(url: str, data, partition_key: str,
               logger) -> dict:
    """Put a record in Kinesis Data Stream.

    Arguments:
        url {str} -- Kinesis Data Stream API URL.
        data {str|dict} -- Data to insert into Kinesis Data Stream.
        partition_key {str} -- Determines record's shard assignment.
        logger {logging.RootLogger} -- logger.

    Returns:
        dict -- Contains 'SequenceNumber' and 'ShardId' of assigned Shard.
    """
    url += const.PUT_RECORD_URL_PATH

    res = requests.put(
        url=url,
        data=json.dumps(
            {
                'Data': data,
                'PartitionKey': partition_key
            }
        )
    )

    logger.info('Message sent on Kinesis Data Stream.')
    return res.json()
