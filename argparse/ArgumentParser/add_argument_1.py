import argparse
import sys

parser = argparse.ArgumentParser(prog="ArgumentParser_1.py")
# ! Basic Usage of add_argument!
#  Add either optional argument with prefix - or positional argument
parser.add_argument('ip')
parser.add_argument('--port','-p')
parser.add_argument('--device', dest='mydevice') # use a different dest than the default one. In this case it's "device"

print(parser.parse_args(' 10.1.1.1 -p 1000  --devic tps'.split())) # Namespace(ip='10.1.1.1', mydevice='tps', port='1000')
# print(parser.parse_args('-p 1000   10.1.1.1 --devic tps'.split())) # same out as above


# ! Advanced Usage of add_argument!
parser.add_argument('--protocol', nargs='*')
print(parser.parse_args('--protocol tcp udp icmp_v4 -- 1.1.1.1'.split())) # Namespace(ip='1.1.1.1', mydevice=None, port=None, protocol=['tcp', 'udp', 'icmp_v4'])
# print(parser.parse_args(' 1.1.1.1 --protocol tcp udp icmp_v4'.split())) # same output as above

parser.add_argument('--devices', nargs=2)
print(parser.parse_args('--devices 10.2.3.4 10.2.3.5 -- 1.1.1.1 '.split()))

# In general, the argparse module assumes that flags like -f and --bar indicate optional arguments, which can always be omitted at the command line. To make an option required, True can be specified for the required= keyword argument to add_argument():
parser.add_argument('--src-ip', required=True)
print(parser.parse_args('--src-ip 8.8.8.8 -- 1.1.1.1 '.split()))


