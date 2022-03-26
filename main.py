#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import argparse
import bencode
import hashlib
import btdht
import binascii
from time import sleep

argparser = argparse.ArgumentParser(description='Scrape a torrent for peers.')
argparser.add_argument('torrent', help='The torrent file to scrape.')
argparser.add_argument('-t', '--timeout', type=int, default=10, help='The timeout in seconds for the scrape request.')
argparser.add_argument('-p', '--print', action='store_true', help='Print the peers.')
argparser.add_argument('-c', '--clear', action='store_true', help='Clear the screen before printing the peers.')

args = argparser.parse_args()


def scrape(torrent, timeout, print_peers, clear_screen):
    # Get the info hash from the torrent file.
    with open(torrent, 'rb') as f:
        torrent_data = bencode.bdecode(f.read())
        info_hash = hashlib.sha1(bencode.bencode(torrent_data['info'])).digest()

    dht = btdht.DHT()
    dht.start()
    sleep(15)
    while True and timeout > 0:
        #os.system('clear')
        peers = dht.get_peers(info_hash)
        if type(peers) is list:
            print("Tottal peers: %d" % len(peers))
            if print_peers:
                for peer in peers:
                    print(peer)
        sleep(5)
        if clear_screen:
            os.system('clear')
        timeout -= 5
        print("Timeout: %d seconds" % timeout)
scrape(args.torrent, args.timeout, args.print, args.clear)


# usage
# python3 main.py torrent-file -t time-in-seconds
# it will print the total nnumbers of peers it found from the given torrent for every 5 seconds for the given time   (default 10 seconds)
# python3 main.py torrent-file -t time-in-seconds -p
# it will print the peer lists every 5 seconds for the given time   (default 10 seconds)
# and it will print the peer lists every 5 seconds for the given time   (default 10 seconds)
# python3 main.py torrent-file -t time-in-seconds -c -p
# complete usage

# Path: main.py 

