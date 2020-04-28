import os
from  jinja2 import Template
from config import *
from termcolor import colored
if os.path.exists('tmp'):
    os.system('rm -rf tmp')
if hosts == ['127.0.0.1', '127.0.0.2']:
    print (colored('please change the default variable  hosts  in conf file','red'))
    exit(1)
if not os.path.exists('tmp'):
    os.mkdir('tmp')
def node_exporter():
    f = open('tmp/node_exporter.service', "w+")
    template = Template("""
    [Unit]
    Description=Node Exporter
    Wants=network-online.target
    After=network-online.target
    
    [Service]
    User=node_exporter
    Group=node_exporter
    Type=simple
    ExecStart=/usr/local/bin/node_exporter  --collector.meminfo --collector.loadavg --collector.filesystem --web.listen-address=:{{port}}
    
    [Install]
    WantedBy=multi-user.target  """)
    f.write(template.render(port=port))
    f.close()
    print(len(hosts))
    for i in range(len(hosts)):
        os.system(('scp -o ConnectTimeout=3 tmp/node_exporter.service root@{0}:/etc/systemd/system/').format(hosts[i])) == 0
        if exit(0):
            print('please go to server {0} and run systemctl enable node_exporter && systemctl start node_exporter'.format(hosts[i])) == 0

node_exporter()
