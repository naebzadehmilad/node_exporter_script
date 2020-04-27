import logging,colorlog
colorlog.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S')
import configparser , os
conf = configparser.ConfigParser()
def write_conf():
    conf.add_section('hosts')
    conf.set('hosts','nodes','127.0.0.1,127.0.0.2')
    conf.add_section('port')
    conf.set('port','port','9100')
    with open('conf','w') as configfile:
        conf.write(configfile)
def read_conf():
      conf.read('conf')
      global hosts
      global port
      hosts = str(conf.get('hosts', 'nodes')).replace(' ', '').replace(' ', '[').replace(' ',']').split(',')
      port = str(conf.get('port', 'port')).replace(' ', '').replace(' ','[')
      logging.info('  create conf \n')
if os.path.exists('conf') :
    read_conf()
else:
    write_conf()
    read_conf()
