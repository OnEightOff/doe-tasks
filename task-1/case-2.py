#!/usr/bin/env python3

import random
import argparse
import sys

def random_mac():
    """
    macaddr variable is a list of 6 random integers between 0 to 255
    return, the remainder of  "%02x" and each integer is a hex code without
    the 0x.
    If the random integer is 131 then "%02x" % 131 is 83(0x83)
    """
    macaddr = [ random.randint(0x00, 0xff),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff),
            random.randint(0x00, 0xff)]
#    print(mac)
    return ':'.join(["%02x" % x for x in macaddr])


def random_uuid():
    """
    Variable uid generates a list of 16 random integers
    '-'.join is generates 
    '%02x%02x%02x%02x-%02x%02x-%02x%02x-%02x%02x-%02x%02x%02x%02x%02x%02x'
    and each "%02x" is divisioned by each number from the tuple.
    """
    uid = [random.randint(0, 255) for ignore in range(0, 16)]
    # print(uid)
    return "-".join(["%02x" * 4, "%02x" * 2, "%02x" * 2, "%02x" * 2,
                          "%02x" * 6]) % tuple(uid)                   

def parser_args():
    parser = argparse.ArgumentParser(
        prog='case-2.py',
        description='List the no. of devices from the specified numbers.'
        )
    parser.add_argument('--begin', type=int, help='The starting no. to generate the data')
    parser.add_argument('--end', type=int, help='The end no. to generate the data')
    args = parser.parse_args()
#    print(args)
    return args.begin, args.end


device_num_start, device_num_end = parser_args()

print("Device no" + ", \t" + "Device UID " + ", \t" + "Ethernet MAC Address" + ", \t" + "Wifi MAC Address")

for no in range(device_num_start, device_num_end+1):
# Add device_num+1 since a list begins with 0
    print(str(no) + ', \t' + random_uuid() + ', \t' + random_mac() + ', \t' +  random_mac())