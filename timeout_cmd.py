#!/usr/bin/env python2.7

import subprocess
from threading import Timer
import pdb


def kill_proc(p, cmd, t):
    print('Killing: pid: {}, cmd:{} after {} seconds'.format(p.pid, cmd, t))
    p.kill()

def main():
    #cmd = '/home/ayousuf/scripts/infinit_loop.py'
    cmd = 'lls'
    timeout_sec = 5
    try:
        process = subprocess.Popen([cmd], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        print('Unable to run: {}'.format(cmd))
        quit(1)
    
    my_timer = Timer(timeout_sec, kill_proc, [process, cmd, timeout_sec])

    try:
        my_timer.start()
        stdout, stderr = process.communicate()
    finally:
        my_timer.cancel()

    print('stdout: {}'.format(stdout))
    print('stderr: {}'.format(stderr))

main()

