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

RESOURCE_NOT_FOUND_EXCEPTION = 'ResourceNotFoundException'

# Path of file
FILE_PATH = 's3://'

STARTING_OCR_STREAM = 'STARTING OCR STREAM CONSUMER...'
STARTING_STATUS_STREAM = 'STARTING STATUS STREAM CONSUMER...'
CHECKPOINT = '_checkpoint.json'


# JOB STATUS
OCR_JOB_SUBMITTED = ' OCR JOB IS SUBMITTED STATUS CODE: '
OCR_JOB_NOT_SUBMITTED = ' OCR JOB NOT SUBMITTED : '
OCR_JOB_URL_ERROR = 'OCR JOB IS NOT SUBMITTED CHECK YOUR REQUESTED URL'
OCR_JOB_STATUS_FOR_MONGODB = ' STATUS OF OCR JOB IN MONGODB: '


# ERROR 
INVALID_STREAM_NAME = "Stream by given name doesn't exists Please verify that the stream exists in Kinesis."
BASE_URL_SCHEMA_MISIING = "Base URL schema is missing. Please verify that 'https://' is present before the URL."


# CONSTANTS
STREAM_DESCRIPTION = "StreamDescription"
SHARDS = "Shards"
SHARD_ID = "ShardId"
SEQUENCE_NUMBER_RANGE = "SequenceNumberRange"
STARTING_SEQUENCE_NUMBER_KEY = "StartingSequenceNumber"
INVALID_STARTING_SEQUENCE_NUMBER = "Invalid StartingSequenceNumber."
NO_STARTING_SEQUENCE_NUMBER = "no StartingSequenceNumber."
KINESIS_API_GENERATED_SUCCESSFULLY = "Kinesis Data Stream API URL generated successfully."

RECORDS = "Records"
DATA = "Data"
SEQUENCE_NUMBER = "SequenceNumber"
NEXT_SHARD_ITERATOR = "NextShardIterator"
KINESIS_MICROSERVICES = "KinesisMicroservices"
OCR_JOB_SUBMITTED = {
            "message": "Submitted OCR Job Successfully."
        }
STATE = 'state'
PATIENT_OBJECT_ID = 'patientObjectID' 
PATIENT_ID = 'patientID'

NEW_MESSAGE = 'NEW MESAGE'

WRITE = 'w'
READ = 'r'

HTTP_200_OK = 200

_TYPE = '__type'

MESSAGE = 'message'

SHARD_IDS = 'shard-id'
SHARD_ITERATOR_TYPE = 'shard-iterator-type'
STARTING_SEQUENCE_NUMBER = 'starting-sequence-number'
TIMESTAMP = 'timestamp'

SHARDITERATOR = 'ShardIterator'

SHARD_ITEARATOR = 'shard-iterator'
LIMIT = 'limit'

SHARD_ITERATOR_TYPE_INVALID =   '''
                'shard_iterator_type' is invalid.
                    Please use one of the following:
                    - AT_SEQUENCE_NUMBER
                    - AFTER_SEQUENCE_NUMBER
                    - AT_TIMESTAMP
                    - TRIM_HORIZON
                    - LATEST
            '''

STARTING_SEQUENCE_NUMBER_INVALID = '''\'starting_sequence_number\' is invalid for given '
                ' shard iterator type.''' 
TIMESTAMP_INVALID = '''\'timestamp\' is invalid for given shard iterator type.'''


UTF_8 = 'utf-8'

ASC_TIME = '%(asctime)s -'
ASC_LEVEL =  '%(levelname)s -'
ASC_MESSAGE = '- %(message)s'

ERROR_TYPE_MESSAGE = '''
                    Error type: {etype}.
                    Error message: {message}.
                '''
NLP_DATES_JOB_STATUS = 'STATUS OF NLP DATES : '
NLP_CODES_JOB_STATUS = 'STATUS OF NLP CODES : '
NLP_CODE_JOB_SUBMITTED_SUCCESSFULLY = 'NLP CODES JOB SUBMITTED SUCCESSFULLY : '
NLP_CODE_JOB_SUBMITTED_NOT_SUCCESSFULLY = 'NLP CODES JOB IS NOT SUBMITTED SUCCESSFULLY : '
NLP_DATES_JOB_SUBMITTED_SUCCESSFULLY = 'NLP DATES JOB SUBMITTED SUCCESSFULLY : '
NLP_DATES_JOB_SUBMITTED_NOT_SUCCESSFULLY = 'NLP DATES JOB IS NOT SUBMITTED SUCCESSFULLY : '
NO_CALLER = 'No caller is specified'
NO_STATE = 'State id is not provided in message'
NO_PATIENT = 'Patient ID is not given in message'
STATUS_CODE = 'STATUS_CODE : '
OCR = 'OCR'
REVIEW = 'Review'
CALLER = 'caller'
STATUS = 'status'
SUCCESS = 'success'