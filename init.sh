#!/bin/bash
DB_FILE_NAME="wallets.db"
DB_TABLE_NAME="wallets"

sudo apt update
sudo apt install sqlite3
sqlite3 --version
COMMAD="""
CREATE TABLE Wallet (
   id INTEGER PRIMARY KEY   AUTOINCREMENT,
   mnemoric CHAR(256)
);
"""
echo $COMMAD| sqlite3 $DB_FILE_NAME



sudo apt install python3.10
sudo apt install python3.10-venv
sudo apt install python3.10-dev
sudo apt install libgmp-dev
sudo apt install python3.10-full
sudo apt install build-essential
sudo apt install gcc
sudo apt install libpq-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev libjpeg-dev zlib1g-dev



python3.10 -m venv venv

source venv/bin/activate

venv/bin/python3.10 -m pip install bitcoinlib
venv/bin/python3.10 -m pip install requests
venv/bin/python3.10 -m pip install tronpy
venv/bin/python3.10 -m pip install mnemonic
venv/bin/python3.10 -m pip install web3

deactive

echo "poyalnx Dooni path. 2023"