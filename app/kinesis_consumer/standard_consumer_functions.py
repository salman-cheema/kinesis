'''
Functions for OCR JOB and it's response to mongodb
'''
import logging
import json
import grequests
import time
import requests
import ocr_config as ocr_config
import status_config as status_config
from os import path
import consumers_constants as const
from standard_kinesis_consumers_functions import \
    get_stream_shards, get_shard_iterator, get_stream_description


def ocr_service(msg):
    """
    This function will call OCR Job

    Arguments:
        msg {[string]} -- [Dictionary in the form of string will be recieved ]

    Returns:
        [string] -- [Dictionary in the form of string will be returned]
    """

    try:
        time.sleep(310)
        # check_health = requests.get(url=ocr_config.OCR_PING_URL)
        # if check_health.status_code == const.HTTP_200_OK:
        #     req = grequests.post(url=ocr_config.OCR_API_URL, data=msg)
        #     grequests.send(req, grequests.Pool(1))

        #     get_response = const.OCR_JOB_SUBMITTED
        #     logging.info(str(check_health.status_code))
        #     logging.info(get_response)
        # else:
        #     logging.error(str(check_health.status_code))
        #     logging.error(const.OCR_JOB_URL_ERROR)
    except Exception as identifier:
        logging.error(const.OCR_JOB_NOT_SUBMITTED)
        logging.error(str(identifier))


def process_message(message):
    """This function will receive messages and on the basis of 
       message it will decide the action.

    Arguments:
        message {[type]} -- [description]
    """
    try:
        ## call update state:
        message = json.loads(message)
        if message.get(const.STATE):
                response = requests.put(
                    status_config.WORKFLOW_API + message[const.PATIENT_OBJECT_ID], data=json.dumps(message))
                if response.status_code == const.HTTP_200_OK:
                    logging.info(const.OCR_JOB_STATUS_FOR_MONGODB + const.STATUS_CODE +
                                 str(response.status_code) + ' - ' + const.PATIENT_ID + ' - ' + str(message[const.PATIENT_ID]))
                else:
                    logging.error(const.OCR_JOB_STATUS_FOR_MONGODB + const.STATUS_CODE +
                                  str(response.status_code) + ' - ' + const.PATIENT_ID + ' - ' + str(message[const.PATIENT_ID]))
        else:
            logging.error(const.NO_STATE)
        if message.get(const.CALLER) == const.OCR and message.get(const.STATUS) == const.SUCCESS:
            if message.get(const.PATIENT_OBJECT_ID):
                check_health = requests.get(url=status_config.NLP_PING_API)
                if check_health.status_code == const.HTTP_200_OK:
                    req = grequests.put(url=status_config.NLP_DATES_API + message[const.PATIENT_OBJECT_ID], data=json.dumps(message))
                    grequests.send(req, grequests.Pool(1))
                    get_response = const.NLP_DATES_JOB_SUBMITTED_SUCCESSFULLY
                    logging.info(const.NLP_DATES_JOB_STATUS + str(check_health.status_code))
                    logging.info(get_response)
                else:
                    logging.error(const.NLP_DATES_JOB_STATUS + str(check_health.status_code))
                    logging.error(const.NLP_DATES_JOB_SUBMITTED_NOT_SUCCESSFULLY)
            else:
                logging.error(const.NO_PATIENT)
        elif message.get(const.CALLER) == const.REVIEW:
            if message.get(const.PATIENT_OBJECT_ID):
                check_health = requests.get(url=status_config.NLP_PING_API)
                if check_health.status_code == const.HTTP_200_OK:
                    req = grequests.put(url=status_config.NLP_CODES_API + message[const.PATIENT_OBJECT_ID], data=json.dumps(message))
                    grequests.send(req, grequests.Pool(1))
                    get_response = const.NLP_CODE_JOB_SUBMITTED_SUCCESSFULLY
                    logging.info(const.NLP_CODES_JOB_STATUS + str(check_health.status_code))
                    logging.info(get_response)
                else:
                    logging.error(const.NLP_CODES_JOB_STATUS +  str(check_health.status_code))
                    logging.error(const.NLP_CODE_JOB_SUBMITTED_NOT_SUCCESSFULLY)
            else:
                logging.error(const.NO_PATIENT)
        else:
            logging.error(const.NO_CALLER)
    except Exception as identifier:
        logging.error(str(identifier))




def get_shard_iterators(stream_url, stream_name):
    """This function will take care if programme crashes
       In that case it will store the sequence numbers
       of last read messages and start the
       programme again from that point so that no message could loss.

    Arguments:
        stream_url {[String]} -- [Give the url of Stream]
        stream_name {[String]} -- [Name of Stream]

    Returns:
        [List] -- [Shards iterators]
        [Dict] -- [Dictionary {'shardid':'sequencenumber'}]
        [List] -- [Shards ID's]
    """
    shards = get_stream_shards(stream_url)
    shard_sequence_numbers = {}
    stream_description = None

    shard_iterators = []
    check_file = path.exists(stream_name + const.CHECKPOINT)
    # Get Shard iterator
    if not check_file:
        for shard in shards:
            shard_sequence_numbers[shard] = ''
            shard_iterators.append(get_shard_iterator(stream_url, shard))
    else:
        with open(stream_name + const.CHECKPOINT, const.READ) \
                as sequence_number_checkpoint:
            shard_sequence_numbers = json.load(sequence_number_checkpoint)
        for shard in shards:
            # This is assuming that the shard not present in file
            # `_checkpoint.json`
            # are newly created and hence are read from the beginning.
            if shard not in shard_sequence_numbers:
                logging.info(" NEW SHARD HAS BEEN ADDED IN KINESIS STREAM " + str(shard))
                shard_sequence_numbers[shard] = ''
                if stream_description is None:
                    stream_description = get_stream_description(stream_url)
                for sequence_number_range in \
                        stream_description[const.STREAM_DESCRIPTION][const.SHARDS]:
                    shard_id = sequence_number_range[const.SHARD_ID]
                    if shard_id == shard:
                        StartingSequenceNumber = \
                            sequence_number_range[const.SEQUENCE_NUMBER_RANGE][const.STARTING_SEQUENCE_NUMBER_KEY]
                        res = get_shard_iterator(stream_url, shard,
                                                 const.AT_SEQUENCE_NUMBER,
                                                 StartingSequenceNumber)
            # Read sequence number from file for the messages.
            if shard in shard_sequence_numbers:
                if (shard_sequence_numbers[shard] != ""):
                    logging.info(str(shard) + ' : is started after sequence number ' + str(shard_sequence_numbers[shard]))
                    res = get_shard_iterator(stream_url, shard,
                                             const.AFTER_SEQUENCE_NUMBER,
                                             shard_sequence_numbers[shard])
                else:
                    logging.info(str(shard) + ' : is started from latest state ')
                    res = get_shard_iterator(stream_url, shard)

            # latest if 'StartingSequenceNumber' invalid or not given.
            for err in [const.INVALID_STARTING_SEQUENCE_NUMBER,
                        const.NO_STARTING_SEQUENCE_NUMBER]:
                if err in res:
                    res = get_shard_iterator(stream_url, shard)

            shard_iterators.append(res)
    return shard_iterators, shard_sequence_numbers, shards
