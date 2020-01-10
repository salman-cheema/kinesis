## consumers_constants.py
 """
 summary:
        `consumers_constants.py` file contains all the constant which 
        are being used for the consumers and their function
 """

## ocr_config.py
""" 
 summary:
        File contains all the configuration which are need to run 
        `ocr stream` 

"""

## status_config.py
"""
 summary:
        File contains all the configuration which are need to run 
        `status stream`

"""

## Kinesis_ocr_stream.py
"""
 summary:
        It will use `ocr_config.py` for configuration
        File contain code which will consume messages from `ocr stream`
        It will trigger `ocr job` on each message and get the status that 
        job is submitted or not.
        On every message same process repeated.

"""

## Kinesis_status_stream.py
"""
 summary:
        It will use `status_config.py` for configuration
        File contain code which will receive message from every `ocr job` that was triggered by `kinesis_ocr_stream` code.
        Message contains the `success` or `failure` response on the basis of which mongodb localdata will be updated.
"""

## standard_kinesis_consumers_functions.py
"""
 summary:
        File contains all the functions which are neccessary for the consumers to get `records`

""" 

## standard_consumers_functions.py
"""
 summary:
        File conatins all the functions which are being used in the  `consumers`
        to run the `ocr job `, update the status of job in `mongodb` 
        and a function to maintain the `checkpoint` of all the shards. 
"""