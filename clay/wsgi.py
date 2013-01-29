from __future__ import absolute_import
from clay.server import application
from clay import config

log = config.get_logger('clay.wsgi')
for modulename in config.get('views'):
    log.debug('Loading views from %s' % modulename)
    module = __import__(modulename)