#!/usr/bin/env python
from random import shuffle, randint
import otp

# TODO: move these into a conf file
# TODO: confirm that pattern is a subset of shapes

shapes  = list(set(['T', 'C', 'S'])) # every element must be unique
pattern = ['S', 'S', 'T', 'C'] # this is the users pattern.

def Tricrypt(totp, args):
    # get the formatting strings right
    if args.xml: 
        header = "<code service=\"{}\" validfor={} length={}>\n"
        linepre = "\t<line>\n"
        linepost = "\t</line>\n"
        shapeformat = "\t\t<{0}>{1}</{0}>\n"
    else:
        header = "{} [{} secs] [{} digits]\n" +("-"*20) +"\n"
        linepre = ""
        linepost = "\n"
        shapeformat = "{}{} "

    out = header.format(args.service, totp.validfor, args.length)

    k = 0
    for i in range(args.length):
        shuffle(shapes)
        out += linepre
        for s in shapes:
            if (s == pattern[k % len(pattern)]) and k < args.length:
                if args.color: 
                    out += "\x1b[0;31m"
                    out += shapeformat.format(s, totp.code[k])
                    out += "\x1b[0m"
                else:
                    out += shapeformat.format(s, totp.code[k])
                
                k+=1

            else: out += shapeformat.format(s, randint(0,9))
        out += linepost

    if args.xml: out += "</code>"
    return out

if __name__ == "__main__":
 	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument("service", help="a service name stored in the conf file.")
	parser.add_argument("-x", "--xml", help="enable xml output", action="store_true")
	parser.add_argument("-c", "--color", help="enable colored output", action="store_true")
	parser.add_argument("-l", "--length", help="code length", type=int, default=6)
	args = parser.parse_args()

	with open("secrets.conf", 'r') as f:
	    for line in f:
	        service_name, secret_key = line.strip().split('=', 1)
	        if (args.service == service_name):
                    totp = otp.otp(secret_key, args.length)
                    print Tricrypt(totp, args)
