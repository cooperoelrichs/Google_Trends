import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.dates as mdates
import numpy as np
import datetime
import time
import re

class csvReader(object):
    def __init__(self, csv_dir, headers = False, date = False):
        print('opening and processing: %(w)s' % {'w':csv_dir})
        self.open_csv(csv_dir)
        self.csv_to_mat(headers, date)

    def get_mat(self):
        return self.mat
        
    def plot_csv(self, key_word = '', date_index = 0, data_index = 1, index = 0):
        self.setup_plot()
        self.plot_trend(key_word, date_index, data_index, index)
        self.show_plot()
    
    def open_csv(self, csv_dir):
        with open(csv_dir, 'r') as open_file:
            csv = open_file.read()
            open_file.close
        self.csv = csv
        return csv
    
    def csv_to_mat(self, headers = False, date = False):
        csv = self.csv
        print('Processing data...')
        lines = csv.split('\n')
        header = lines.pop(0)
        print('Data headers: %(w)s' % {'w':header})
        mat = np.zeros((len(lines),len(header.split(','))))
        
        for i, line in enumerate(lines):
            for j, x in enumerate(line.split(',')):
                if x == None or x == '': continue
                if date == True and j == 0:
                    y,m,d = [int(d) for d in x.split('-')]
                    j_date = datetime.date(y,m,d)
                    #x = (j_date - datetime.date(1,1,1)).total_seconds()
                    x = time.mktime(j_date.timetuple())
                mat[i,j] = x
        self.mat = mat
        return mat
    
    def mat_test(self):
        mat = self.mat
        print(mat[0])