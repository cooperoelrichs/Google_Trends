from pyGTrends_mod import pyGTrends
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.dates as mdates
import datetime
import re

class googleTrends(object):
    def __init__(self):
        print('init googleTrends')

    def login(self, username, password):
        print('Logging in... as %(u)s, %(p)s' % {'u':username, 'p':password})
        self.gtrends = pyGTrends(username,password)
        print('...Logged in')
        #gtrends = pyGTrends('cdo.gtrends@gmail.com','80gbhdoj')

    def get_trend(self, word, date_in, geo_in, trend_dir):
        print('Downloading report... %(w)s, for %(d)s, in %(g)s' % {'w':word, 'd':date_in, 'g':geo_in})
        self.trend = self.gtrends.download_report(word,date = date_in,geo = geo_in)
        csv = self.gtrends.csv('Week')
        #self.gtrends.download_report(('google'),date = '2004 - present', geo = 'Australia')
        asx200_name = 'gtrend_%(w)s.csv' % {'w':word}
        csv_dir  = trend_dir + '/' + asx200_name
        print('saving file: %s' % {asx200_name})
        with open(csv_dir, 'w') as trend_file:
            trend_file.write(csv)
            trend_file.close
        print('...done')
        return csv

    def open_trend_file(self, key_word, trend_dir):
        asx200_name = 'gtrend_%(u)s.csv' % {'u':key_word}
        csv_dir  = trend_dir + '/' + asx200_name
        with open(csv_dir, 'r') as trend_file:
            csv = trend_file.read()
            trend_file.close
        return csv

    def process_trend_to_mat(self, csv, key_words):
        # Change array to numpy Matrix!!!
        print('Processing data...')
        lines = csv.split('\n')
        data = [None]*len(lines)

        for i, x in enumerate(lines):
            x1, x2 = x.split(',')
            if    '%(w)s' % {'w':key_words} in x2            : continue
            elif  bool(re.compile('\d').search(x2)) == False : x2 = None
            else: x2 = int(x2)
            x1 = [[int(z) for z in y.split('-')] for y in x1.split(' - ')]
            dates = [datetime.date(y,m,d) for y,m,d in x1]
            data[i] = dates + [x2]
        print('...Done')
        return data




    #OLD
    def setup_plot(self):
        fig = plt
        f, (self.ax1, self.ax2) = fig.subplots(2, sharex = True)
        #hfmt = mdates.DateFormatter('%m/%d %H:%M')

    def plot_trend(self,data,header,plot_index):
        dates, trend_values, dx = [], [], [0]
        colours = ['b','g','r','c','m','y','k','w']
        for i, x in enumerate(data):
            if x == None or x[2] == None: continue
            dates.append(mdates.date2num(x[1]))
            trend_values.append(x[2])
            if len(trend_values) > 1: dx.append(trend_values[-1]-trend_values[-2])
            #if trend_values[-1] == None: trend_values[-1] = 0
        
        #ax.hist(trend_values, len(dates), facecolor='green', alpha=0.75)
        plot1, = self.ax1.plot(dates,trend_values,colours[plot_index],label=header,clip_on=0)
        plotdx, = self.ax2.plot(dates,dx,'%(w)s' % {'w':colours[plot_index]},label='dx: %(w)s' % {'w':header},clip_on=0) #label='dx: %(w)s' % {'w':header}
        #plot1, = ax.bar(dates, trend_values, 1, color='r')

        
    def show_plot(self):
        locator = mdates.AutoDateLocator()
        self.ax1.xaxis.set_major_locator(locator)
        self.ax1.xaxis.set_major_formatter(mdates.AutoDateFormatter(locator))
        self.ax1.set_ylim(bottom = 0)
        self.ax1.set_title('Google Trend')
        self.ax2.set_title('Change (by week)')
        self.ax1.set_ylabel('GTrend Score')
        self.ax2.set_ylabel('GTrend Score Change')
        self.ax1.legend(loc = 2, fontsize = 6)
        plt.xticks(rotation = 'vertical')
        #plt.subplots_adjust(bottom = .3)
        plt.grid(True)
        plt.xlabel('Date')
        #plt.ylabel('GTrend Score')
        #plt.legend(loc = 2, fontsize = 6)
        plt.show()
        
        #INFO: http://stackoverflow.com/questions/5498510/creating-graph-with-date-and-time-in-axis-labels-with-matplotlib
        #INFO: http://stackoverflow.com/questions/3034162/plotting-a-cumulative-graph-of-python-datetimes
        
        #ms.plot(dates,trend_values,'ro',label='gtrend',clip_on=0)
        #ms.Gll('x')
        #ms.show()
        
        
        
        
        
        
        
        
        
        
        
        
