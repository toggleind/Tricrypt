#!/usr/bin/env python
# Include a license block here
import yaml
from random import shuffle, randint

from output import formats

#globals
shapes = list(set(['C', 'S', 'D', 'T'])) # make unique

class Settings(object):
    def __init__(self, d=dict()):
        self.__dict__ = d

    # this will overwrite any settings currently stored.
    def importYamlFile(self, filename):
        with open(filename, 'r') as stream:
            s = yaml.load(stream)
            self.__dict__ = s


# refactor this for the love of god.
# it's fine for now, but eventually,
# this needs a serious refactor.
def Tricrypt(totp, service_name, settings):

    try:
        fmt = formats[settings.output]
    except KeyError:
        raise KeyError("{} is not a known output format".format(settings.output))
        
    out = fmt['header'].format(
        service = service_name,
        sec = totp.validfor,
        digits = settings.pin_length
        )

    k = 0
    for _ in range(settings.pin_length):
        shuffle(shapes)
        out += fmt['linepre']
        for y in shapes:
            if ((y == settings.pattern[k % len(settings.pattern)]) and
            k < settings.pin_length):
 
                out += fmt['shapeformat'].format(shape = y, num = totp.code[k])
                k+=1

            else:
                out += fmt['shapeformat'].format(shape = y, num = randint(0,9))
        
        out += fmt['linepost']
        
    out += fmt['footer']
    return out
    