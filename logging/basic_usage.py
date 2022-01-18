import logging
logger=logging.getLogger()
logger.warning(' fn=%(funcName)s(), id=%(id)d', {'funcName':'boo', 'id':123})

FORMAT = '%(asctime)-10s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'Kevin'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'connection reset', extra=d)
