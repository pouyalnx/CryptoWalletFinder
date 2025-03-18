import sqlite3



DB_FILE_NAME="wallet.db"
DB_TABLE_NAME="Wallet"

def insert_to_db(mnemoric:str):
    connection=sqlite3.connect(DB_FILE_NAME)
    cur=connection.cursor()
    cmd= f"INSERT INTO {DB_TABLE_NAME} ('mnemoric') VALUES (\'{mnemoric}\');"
    cur.execute(cmd)
    connection.commit()
    cur.close()
    connection.close()

from mnemonic import Mnemonic
mne=Mnemonic('english')

for _ in range(32):
    words=mne.generate()
    insert_to_db(words)

    print("----------------------------------------------------------------")
