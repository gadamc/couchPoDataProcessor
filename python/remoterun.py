#!/usr/bin/env python
import pexpect
import datetime
import sys

def main(inputLine): #since this is called by the couchdbkit.Consumer, it will pass in a line from the db. just ignore it.
    #if inputLine == '': return #quit if nothing was sent.. this is probably a heartbeat

    startTime = datetime.datetime.now()
    print startTime, inputLine
    p = pexpect.spawn('/usr/bin/ssh gadamc@ccage.in2p3.fr "source /sps/edelweis/kdata/dataprocessing/schedule/remoteHook.sh"')
    ssh_newkey = 'Are you sure you want to continue connecting'
    i=p.expect([ssh_newkey,'password:',pexpect.EOF])
    if i==0:
        print 'accepting key'
        p.sendline('yes')
        i=p.expect([ssh_newkey,'password:',pexpect.EOF])
    if i==1:
        print startTime, 'sending password and running "source /sps/edelweis/kdata/dataprocessing/schedule/remoteHook.sh" '
        p.sendline("***")
        p.expect(pexpect.EOF)
    elif i==2:
        print "I either got key or connection timeout"
        pass
    
if __name__ == '__main__':
    if len(sys.argv) > 1: main(sys.argv[1])
    else: main('')