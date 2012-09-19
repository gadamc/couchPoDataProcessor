#!/usr/bin/env python
from couchdbkit import Server, Database, Consumer
import runProc0
import datetime

def callback(line):
    n = datetime.datetime.now()
    print n, line
    runProc0.main('http://edwdbuser:***@127.0.0.1:5984', 'datadb')

def main():
    s = Server('http://edwdbuser:***@127.0.0.1:5984')
    db = s['datadb']
    c = Consumer(db)

    #start listening since = current update sequence.
    #callback function is run.main
    #heartbeat every minute to keep the connection alive.
    c.wait(callback, since = db.info()['update_seq'], filter='proc/newproc0', feed='continuous', heartbeat=60000)  

if __name__ == '__main__':
    main()