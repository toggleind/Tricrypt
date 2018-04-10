#!/usr/bin/env python
import yaml
from random import shuffle, randint

import otp

#globals
shapes = list(set(['C', 'S', 'D', 'T'])) # make unique

class settings(object):
    def __init__(self, d=dict(), sites=dict()):
        self.__dict__ = d
        self.sites = sites

    def importYaml(self, filename):
        with open(filename, 'r') as stream:
            s = yaml.load(stream)
            try:
                self.__dict__ = s['settings']
                self.sites = s['sites']
            except KeyError:
                pass


def Tricrypt(totp, args, s):
    # get the formatting strings right
    # move this to seperate file?
    if args.xml: 
        header = "<code service=\"{0}\" validfor={1} length={2}>\n"
        linepre = "\t<line>\n"
        linepost = "\t</line>\n"
        shapeformat = "\t\t<{0}>{1}</{0}>\n"
        footer = "</code>"
        
    else:
        header = "{0} [{1} secs] [{2} digits]\n" +("-"*20) +"\n"
        linepre = ""
        linepost = "\n"
        shapeformat = "{}{} "
        footer = ""

    out = header.format(args.service, totp.validfor, args.length)

    k = 0
    for i in range(args.length):
        shuffle(shapes)
        out += linepre
        for y in shapes:
            if (y == s.pattern[k % len(s.pattern)]) and k < args.length:
                out += shapeformat.format(y, totp.code[k])
                k+=1

            else: 
                out += shapeformat.format(y, randint(0,9))
        
        out += linepost
    out += footer
        
    return out

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("service", help="a service name stored in the conf file.")
    parser.add_argument("-x", "--xml", help="enable xml output", action="store_true")
    parser.add_argument("-l", "--length", help="code length", type=int, default=6)
    parser.add_argument("--settings-file", help="Alternate Settings File", default="Tricrypt.yml")
    args = parser.parse_args()
    
    s = settings()
    s.importYaml(args.settings_file)
    
    if args.service in s.sites:
        totp = otp.otp(s.sites[args.service], args.length) # clean this up
        print Tricrypt(totp, args, s) # make this better, pass settings and shapes, and python3
