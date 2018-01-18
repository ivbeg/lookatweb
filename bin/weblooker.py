#!/usr/bin/env python
import sys, time
from lookatweb.analyze import Analyzer

if __name__ == "__main__":
    import socket
    socket.setdefaulttimeout(7)
    an = Analyzer()
    if len(sys.argv) > 1:
        url = sys.argv[1]
        print(url)
        res = an.match_site(url, getDNS=False)
        sorted(res)
        for k in res.keys():
            print('- %s' % (k))
    else:
        print("Usage: weblooker.py <url>")
