#!/usr/bin/python

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
args = argparser.parse_args()


def scrape(torrent, timeout, print_peers):
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
        if peers:
            print("Tottal peers: %d" % len(peers))
            if print_peers:
                for peer in peers:
                    print(peer)
        sleep(5)
        os.system('clear')
        timeout -= 5

scrape(args.torrent, args.timeout, args.print)

