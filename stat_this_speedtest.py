# -*- coding: utf-8 -*-

import json, time

import requests

from speedtest_cli import speedtest
from stathat import StatHat

STATHAT_URL = "http://api.stathat.com/ez"

STATHAT_KEY = "foo@bar.com"

def main():

    stathat = StatHat(STATHAT_KEY)

    payload = {"ezkey": STATHAT_KEY, "data": []}

    data = speedtest()

    stathat.value('Latency', data['latency'])
    stathat.value('Download', data['download'])
    stathat.value('Upload', data['upload'])

    print data


if __name__ == '__main__':
    main()
