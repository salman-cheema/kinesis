'''
Configuration file for all 'Kinesis Functions'
'''

STREAM_NAME = '<KINESIS_OCR_DATA_STREAM>'
API_BASE_URL = '<API_GATEWAY_KINESIS>'
BASE_URL = API_BASE_URL + '/streams/'

'''
Configuration file for all 'Kinesis Functions'
'''
HTTP = 'http://'
OCR_HOSTNAME = '<OCR_HOSTNAME>'
OCR_PORT = '<OCR_PORT>'
OCR_SIGNATURE = '/ocr-process'
OCR_CHECK_SIGNATURE = '/ocr/ping'

OCR_API_URL = HTTP + OCR_HOSTNAME + ':' + OCR_PORT + OCR_SIGNATURE
OCR_PING_URL = HTTP + OCR_HOSTNAME + ':' + OCR_PORT + OCR_CHECK_SIGNATURE
