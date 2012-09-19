#!/usr/bin/env python
from couchdbkit import Server, Database, Consumer
import remoterun

def main():
    s = Server('http://edwdbik.fzk.de:5984')
    db = s['datadb']
    c = Consumer(db)

    #start listening since = current update sequence.
    #callback function is run.main
    #heartbeat every minute to keep the connection alive.
    c.wait(remoterun.main, since = db.info()['update_seq'], filter='proc/statusgood', feed='continuous', heartbeat=60000)  

if __name__ == '__main__':
    main()