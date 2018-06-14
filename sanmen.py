# coding=utf-8
import random
import time


class Sanmen():
    switch_win = 0
    stay_win = 0
    switch = 0
    stay = 0

    @staticmethod
    def sanmen():
        car_door = random.randint(0, 2)
        my_door = random.randint(0, 2)
        change = random.choice([True, False])
        if change:
            Sanmen.switch += 1
            if my_door != car_door:
                Sanmen.switch_win += 1
        else:
            Sanmen.stay += 1
            if my_door == car_door:
                Sanmen.stay_win += 1


if __name__ == '__main__':
    sanmen = Sanmen()
    starttime = time.time()
    for i in xrange(1, 10000000):
        sanmen.sanmen()
    endtime = time.time()
print Sanmen.switch
print Sanmen.switch_win
print 1.0 * Sanmen.switch_win / Sanmen.switch
print Sanmen.stay
print Sanmen.stay_win
print 1.0 * Sanmen.stay_win / Sanmen.stay
print "totaltime%f" % (endtime - starttime)






























