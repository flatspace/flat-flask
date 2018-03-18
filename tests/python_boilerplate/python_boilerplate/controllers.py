#import logging

from flask import request

#LOGGER = logging.getLogger(__name__)


def hello_world(message):
#    LOGGER.info(request.headers)
    # do something
    return 'Hello World. {}'.format(message), 200
