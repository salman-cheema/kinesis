"""Standard functions for Kinesis Data Stream.

This file contains standardized functions for Kinesis Data Streams.
The main purpose of this file is to simplify the creation of producers,
and consumers.

Note:
- To make changes to default values, make changes in the constants file.
- Constants file name: standard_kinesis_functions_constants.py
"""


import logging
import requests
from datetime import date
from requests.exceptions import MissingSchema
import consumers_constants \
    as const
import sys


def get_kinesis_api_url(stream_name: str, base_url) -> str:
    """Gets Kinesis API URL for the given stream.

    Arguments:
        stream_name {str} -- Name of the Kinesis Data Stream.

    Raises:
        ValueError: [description]
        MissingSchema: [description]

    Returns:
        str -- Kinesis API URL to the given Kinesis Data Stream.
    """

    try:
        base_url = base_url

        stream_url = base_url + stream_name

        res = requests.get(stream_url)

        if const._TYPE in res.json():
            if res.json()[const._TYPE] == const.RESOURCE_NOT_FOUND_EXCEPTION:
                logging.error(const.INVALID_STREAM_NAME)
            else:
                logging.error(const.ERROR_TYPE_MESSAGE.format(etype=res.json()[const._TYPE],
                           message=res.json()[const.MESSAGE]))

            raise Exception(res.json()[const.MESSAGE])
    except MissingSchema as e:
        logging.error(const.BASE_URL_SCHEMA_MISIING)
        raise e

    logging.info(const.KINESIS_API_GENERATED_SUCCESSFULLY)
    return stream_url


def get_stream_description(url: str) -> dict:
    """Get's description of a stream.

    Arguments:
        url {str} -- Kinesis Data Stream API URL.

    Returns:
        dict -- Stream description.
    """

    response = requests.get(
        url=url
    )

    return response.json()


def get_stream_shards(url: str) -> list:
    """Returns Shard IDs of the give stream.

    Arguments:
        url {str} -- Kinesis Data Stream API URL.

    Returns:
        list -- List of Shard IDs.
    """
    stream_description = get_stream_description(url)

    shards = stream_description[const.STREAM_DESCRIPTION][const.SHARDS]

    shard_ids = []

    for shard in shards:
        shard_ids.append(shard[const.SHARD_ID])

    return shard_ids


def get_shard_iterator(url: str,
                       shard_id=const.DEFAULT_SHARD_ID,
                       shard_iterator_type=const.DEFAULT_SHARD_ITERATOR,
                       starting_sequence_number=None,
                       timestamp=None) -> str:
    """Returns a shard iterator to retireve records
    from Kinesis Data Stream.

    Arguments:
        url {str} -- Kinesis Data Stream API URL.

    Keyword Arguments:
        shard_id {str} -- ID of the Shard. (default: {'shardId-000000000000'})
        shard_iterator_type {str} -- Type of Shard Iterator.
                                    (default: {'LATEST'})
        starting_sequence_number {str} -- Sequence number to start from.
                                    (default: {None})
        timestamp {str} -- Timestamp to start from. (default: {None})

    Raises:
        ValueError: 'starting_sequence_number' is invalid for given shard
                    iterator type.
        ValueError: 'timestamp' is invalid for given shard iterator type.
        ValueError: 'shard_iterator_type' is invalid.

    Returns:
        str -- Shard Iterator.
    """
    url += const.GET_SHARD_ITERATOR_URL_PATH

    if shard_iterator_type in [const.LATEST, const.TRIM_HORIZON]:
        response = requests.get(
            url=url,
            headers={
                const.SHARD_IDS: shard_id,
                const.SHARD_ITERATOR_TYPE: shard_iterator_type
            }
        )
    elif shard_iterator_type in [const.AT_SEQUENCE_NUMBER,
                                 const.AFTER_SEQUENCE_NUMBER]:
        if starting_sequence_number is None:
            raise ValueError(
                const.STARTING_SEQUENCE_NUMBER_INVALID
            )

        response = requests.get(
            url=url,
            headers={
                const.SHARD_IDS: shard_id,
                const.SHARD_ITERATOR_TYPE: shard_iterator_type,
                const.STARTING_SEQUENCE_NUMBER: starting_sequence_number
            }
        )
    elif shard_iterator_type == const.AT_TIMESTAMP:
        if timestamp is None:
            raise ValueError(
                const.TIMESTAMP_INVALID
            )

        response = requests.get(
            url=url,
            headers={
                const.SHARD_IDS: shard_id,
                const.SHARD_ITERATOR_TYPE: shard_iterator_type,
                const.TIMESTAMP: timestamp
            }
        )
    else:
        raise ValueError(
          const.SHARD_ITERATOR_TYPE_INVALID
        )

    if const.SHARDITERATOR not in response.json():
        return response.json()[const.MESSAGE]

    return response.json()[const.SHARDITERATOR]


def get_records(url: str,
                shard_iterator: str,
                limit=const.DEFAULT_LIMIT) -> dict:
    """Retrieves records from Kinesis Data Stream.

    Arguments:
        url {str} -- Kinesis Data Stream API URL.
        shard_iterator {str} -- Shard Iteraor.

    Keyword Arguments:
        limit {str} -- Limit of records per request. (default: {'10000'})

    Returns:
        dict -- Metadata like 'NextShardIterator', and a list of 'Records'.
    """
    url += const.GET_RECORDS_URL_PATH

    response = requests.get(
        url=url,
        headers={
            const.SHARD_ITEARATOR: shard_iterator,
            const.LIMIT: limit
        }
    )

    return response.json()


def set_logger(consumer_name):
    """This function will send logs to specific consumer log file

    Arguments:
        consumer_name {[string]} -- Give the name of Consumer

    Returns:
        [object] -- It will return logger object
    """

    # set up logging to file
    # logging.basicConfig(filename=const.KINESIS_MICROSERVICES + ' - ' + consumer_name
    #                     + '_' + str(date.today()) + ".log",
    #                     format='%(asctime)s - %(levelname)s -'
    #                     + ' ' + const.KINESIS_MICROSERVICES + ' - '
    #                     + str(consumer_name) + '- %(message)s',
    #                     filemode='a')

    # Creating an object
    # logger = logging.getLogger()
    # # Setting the threshold of logger to INFO
    # logger.setLevel(logging.INFO)
    # # set up logging to console
    console = logging.StreamHandler(stream=sys.stdout)
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter(const.ASC_TIME + const.ASC_LEVEL
                                  + ' - ' + const.KINESIS_MICROSERVICES + ' - '
                                  + str(consumer_name) + const.ASC_MESSAGE,)
    console.setFormatter(formatter)
    # add the handler to the root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(console)


    return logger
