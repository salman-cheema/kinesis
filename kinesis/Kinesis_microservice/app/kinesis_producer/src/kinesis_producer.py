"""A simple module for Kinesis Producer.

This is a simple module for Kinesis Producer written to be used by
other programs that need to act as producer without getting exposed
to lower level code.
"""
# For logging.
import logging

import json
import config
from standard_kinesis_producer_functions import \
    get_kinesis_api_url, put_record


class KinesisProducer:
    """Kinesis Producer.
    A basic producer that pushes records on a
    Kinesis Data Stream.
    """

    def __init__(self, stream_name: str, logger=None):
        """Initializes Kinesis Producer.

        Arguments:
            stream_name {str} -- Name of the Kinesis Stream present in MongoDB.
        """
        if logger is None:
            self.logger = logging.getLogger()
            self.logger.setLevel(logging.INFO)
        else:
            self.logger = logger

        configs = {
            'baseUrl': config.KINESIS_API_BASE_URL,
            'streamKey': stream_name
        }

        self._url = get_kinesis_api_url(
            stream_key='streamKey',
            stream_config=configs,
            logger=self.logger
        )
        self.logger.info('''Use 'put_record' method to send records.''')

    def put_record(self, partition_key: str, data) -> dict:
        """Sends a record on to Kinesis Data Stream.

        Arguments:
            partition_key {str} -- Key by which the shard is selected.
            data {str|dict} -- Record that needs to be put on stream.

        Returns:
            dict -- Response from Kinesis in result of putting a record.
        """
        res = put_record(
            url=self._url,
            partition_key=partition_key,
            data=data,
            logger=self.logger
        )

        return res

    def set_logger(logger):
        """Sets a logger.
        
        Arguments:
            logger {logging.RootLogger} -- This allows 
        """
        self.logger = logger

if __name__ == '__main__':
    """This is for testing purposes.
    """

    # Sends a test message on stream set at `config.KINESIS_STREAM_NAME`.
    stream_producer = KinesisProducer(config.KINESIS_STREAM_NAME)

    res = stream_producer.put_record(
        partition_key='TEST',
        data='This is a test message. Very cool message.'
    )

    print('Sent a test messsage.')
    print(res)
