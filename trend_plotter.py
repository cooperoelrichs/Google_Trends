import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.dates as mdates
import numpy as np
import datetime
import time
import re

class trendPlotter(object):
    def __init__(self, subplots = 2, x_is_dates = False):
        print('New plot created and setup')
        self.x_is_dates = x_is_dates
        self.setup_plot(subplots)
        
    colours = ['b','g','r','c','m','y','k','w']

    def setup_plot(self, subplots = 2):
        fig = plt
        f, self.ax = fig.subplots(subplots, sharex = True)
        #hfmt = mdates.DateFormatter('%m/%d %H:%M')
        
    def plot_trend(self, header, x, y, dx = False, plot_index = 0):
        colours = self.colours
        self.ax[0].plot(x,y,colours[plot_index],label=header,clip_on=0)
        if dx == False: return
        self.ax[1].plot(x,dx,'%(w)s' % {'w':colours[plot_index]},label='dx: %(w)s' % {'w':header},clip_on=0)

    def plot_trend_with_diff(self, data, header, x_index = 0, y_index = 1, plot_index = 0, normalise = False):
        x_data, y_data, dx = [], [], [0]
        colours = self.colours
        for x in data:
            if x == None or x[y_index] == None or x[y_index] == 0: continue
            if self.x_is_dates and (type(x[x_index]) == int or type(x[x_index]) == float or type(x[x_index]) == np.float64):
                date_obj = datetime.datetime.fromtimestamp(x[x_index])
                x_data.append(mdates.date2num(date_obj))
            elif self.x_is_dates and type(x[x_index]) == datetime.date:
                x_data.append(mdates.date2num(x[1]))
            else: x_data.append(x[x_index])
            y_data.append(x[y_index])
            
            if len(y_data) > 1: dx.append(y_data[-1]-y_data[-2])
            #if y_data[-1] == None: y_data[-1] = 0
        
        if normalise:
            dx = [0,0,0,0,0,0,0,0]
            y_max = max(y_data)
            for i,y in enumerate(y_data):
                y_data[i] = y / y_max * 100
                if i > 7: dx.append(y_data[i]-y_data[i-7])
        
        #ax.hist(y_data, len(x_data), facecolor='green', alpha=0.75)
        self.ax[0].plot(x_data,y_data,colours[plot_index],label=header,clip_on=0)
        self.ax[1].plot(x_data,dx,'%(w)s' % {'w':colours[plot_index]},label='dx: %(w)s' % {'w':header},clip_on=0)
            #label='dx: %(w)s' % {'w':header}
        #plot1, = ax.bar(x_data, y_data, 1, color='r')
        
    def show_plot(self):
        if self.x_is_dates:
            locator = mdates.AutoDateLocator()
            self.ax[0].xaxis.set_major_locator(locator)
            self.ax[0].xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))
        self.ax[0].set_ylim(bottom = 0)
        self.ax[0].set_title('Value')
        self.ax[1].set_title('Change (by week)')
        self.ax[0].set_ylabel('Value')
        self.ax[1].set_ylabel('Value Change')
        self.ax[0].legend(loc = 2, fontsize = 6)
        plt.xticks(rotation = 'vertical')
        #plt.subplots_adjust(bottom = .3)
        self.ax[0].grid(True)
        self.ax[1].grid(True)
        plt.xlabel('Date')
        #plt.ylabel('GTrend Score')
        #plt.legend(loc = 2, fontsize = 6)
        plt.show()