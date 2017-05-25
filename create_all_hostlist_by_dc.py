#!/usr/bin/env python2.7

dc = "asg chi chx dfw frf iad lon ord par phx tyo ukb was wax"
dc_list = dc.split(' ')

for dc in dc_list:
    dc_f = dc + '_f'
    with open('all_hostlist_' + dc + '.txt', 'w') as dc_f:
        pass

for dc in dc_list:
    dc_f = dc + '_f'
    with open('all_hostlist_' + dc + '.txt', 'a') as dc_f:
        with open('all_hosts.txt', 'r') as h:
            for l in h:
                if dc in l:
                    dc_f.write(l)

