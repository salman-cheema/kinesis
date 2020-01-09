# flake8: noqa
# pylint: disable-all
"""File for configs.

This gets updated after infrastructure provisioning.
"""

KINESIS_API_BASE_URL = "<KINESIS_API_BASE_URL>"
KINESIS_API_STAGE = '<KINESIS_API_STAGE>'

KINESIS_API_URL = KINESIS_API_BASE_URL + \
                  '/' + KINESIS_API_STAGE + \
                  '/streams/'

KINESIS_STREAM_NAME = "<KINESIS_STREAM_NAME>"
