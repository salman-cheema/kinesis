"""Constants for Standard Kinesis Functions.

This file contains constants for the module `standard_kinesis_functions`.
To make changes to defaults, please modify this file.
"""

# Available Shard Iterator Types
LATEST = 'LATEST'
AT_TIMESTAMP = 'AT_TIMESTAMP'
TRIM_HORIZON = 'TRIM_HORIZON'
AT_SEQUENCE_NUMBER = 'AT_SEQUENCE_NUMBER'
AFTER_SEQUENCE_NUMBER = 'AFTER_SEQUENCE_NUMBER'


"""Kinesis API URL paths
"""

# get_shard_iterator
GET_SHARD_ITERATOR_URL_PATH = '/sharditerator'

# get_records
GET_RECORDS_URL_PATH = '/records'

# put_record
PUT_RECORD_URL_PATH = '/record'


"""Standard functions function arguments defaults.
"""

# get_shard_iterator
DEFAULT_SHARD_ID = 'shardId-000000000000'
DEFAULT_SHARD_ITERATOR = LATEST

# get_records
DEFAULT_LIMIT = '10000'


"""Error handling constants
"""

RESOURCE_NOT_FOUND_EXCEPTION = 'ResourceNotFoundException'
