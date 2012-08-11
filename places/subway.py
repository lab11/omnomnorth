#!/usr/bin/env python

from datetime import time, date, datetime, timedelta
import math

from restaurant import Restaurant, State


class CourtyardSubway(Restaurant):
    reg_hours = {'open': {'hour': 8, 'min': 0},
                 'close': {'hour': 23, 'min': 0}}
    reg_sat_hours = {'open': {'hour': 8, 'min': 0},
                     'close': {'hour': 22, 'min': 0}}
    reg_sun_hours = {'open': {'hour': 9, 'min': 0},
                     'close': {'hour': 21, 'min': 0}}

    def get_hours(self, dt):
        if dt.weekday() == 5:
            return {'open': time(self.reg_sat_hours['open']['hour'],
                                 self.reg_sat_hours['open']['min'], 0),
                    'close': time(self.reg_sat_hours['close']['hour'],
                                  self.reg_sat_hours['close']['min'], 0)}
        if dt.weekday() == 6:
            return {'open': time(self.reg_sun_hours['open']['hour'],
                                 self.reg_sun_hours['open']['min'], 0),
                    'close': time(self.reg_sun_hours['close']['hour'],
                                  self.reg_sun_hours['close']['min'], 0)}
        return {'open': time(self.reg_hours['open']['hour'],
                             self.reg_hours['open']['min'], 0),
                'close': time(self.reg_hours['close']['hour'],
                              self.reg_hours['close']['min'], 0)}


if __name__ == '__main__':
    print 'Open: %i' % State.OPEN
    print 'Opening Soon: %i' % State.OPENING_SOON
    print 'Closed: %i' % State.CLOSED
    print 'Closing Soon: %i' % State.CLOSING_SOON
    test = datetime(2012, 5, 26, 15, 15)
    p = CourtyardSubway()
    print p.get_hours(test)
    print p.get_status(test)
