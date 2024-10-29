#! /usr/bin/env python3

import time

from pydwf import DwfLibrary

def standard_enumeration(deviceEnum):
    t1 = time.monotonic()
    num_dev = deviceEnum.enumerateDevices()
    t2 = time.monotonic()

    print("standard enumerateDevices:", num_dev, (t2 - t1))

def alternate_enumeration(deviceNum):
    t1 = time.monotonic()
    deviceEnum.enumerateStart()
    num_dev = deviceEnum.enumerateStop()

    t2 = time.monotonic()
    print("alternate enumStart:", num_dev, (t2 - t1))


dwf = DwfLibrary()

device = dwf.deviceControl.openEx("name:Discovery2")
print(type(device))

device.close()
