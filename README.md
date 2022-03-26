# torrent-peers-scrape

This is a simple python script that helps to scrape peers simply from a torrent file.

# Usage

## Download the repository

```
git clone https://github.com/imShakil/torrent-peers-scrape.git
cd torrent-peers-scrape
```

## Create Virtual Environment

```
virtualenv .venv
source .venv/bin/activate
```
## Install Packages

```
pip install -r requirements.txt
```

After all the above steps, run the main program:

```
python3 main.py name.torren
```
To get the help menu:

```
python3 main.py -h
```

# Example

In this project, I already added a torrent file `q.torrent`, let's get the peers from this torrent:

```
python3 main.py q.torrent

```

It will print only the numbers of peers it found fromt the torrent.

If you wish to display each of the peers, then:

```
python3 main.py q.torrent -p
```

Adding the time (in seconds) for 5x, which will run for x times:

```
python3 main.py q.torrent -t 30 -p
```
It will repeat the program for 6th times.


## Output

```
python3 main.py q.torrent -p -c -t


init socket for b'8e549053efc0cdc212591d7e105fdadbe33b92b8'
Bootstraping
0 nodes, 0 goods, 0 bads | in: 0, out: 3 en 1s
Timeout: 25 seconds
Tottal peers: 1
('31.208.147.22', 6881)
Timeout: 20 seconds
Tottal peers: 102
('89.64.9.212', 59438)
('185.171.114.248', 63161)
('76.11.54.229', 45256)
('152.32.96.1', 9677)
('198.54.130.132', 42306)
('136.32.140.70', 13664)
('69.178.103.105', 1118)
('156.146.62.204', 14221)
('24.150.22.123', 17286)
('86.59.176.136', 32319)
('47.180.218.12', 58931)
('89.178.233.234', 47686)
('37.138.16.89', 11624)
('80.217.132.87', 31846)
('47.180.218.11', 58931)
('67.183.3.89', 10437)
('93.78.124.149', 8999)
('67.180.234.76', 63155)
('45.14.195.247', 17751)
('66.25.105.236', 45054)
('71.92.61.32', 5239)
('178.212.96.147', 41694)
('100.7.251.109', 47899)
('45.83.220.217', 9931)
('109.76.33.106', 51515)
('183.83.143.180', 21026)
('47.183.233.117', 32121)
('194.110.84.135', 56847)
('91.156.10.60', 43216)
('92.35.68.67', 11807)
('178.90.222.50', 41943)
('46.242.10.222', 22456)
('181.164.58.59', 1388)
('108.49.203.179', 12318)
('85.249.108.29', 1024)
```

