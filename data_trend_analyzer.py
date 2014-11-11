import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.dates as mdates
import numpy as np
import datetime
import time
import re

class dataTrendAnalyzer(object):
    def __init__(self, mat, remove_zero_dates = [False]):
        print('New data trend analyzer')
        self.mat = mat
        if remove_zero_dates[0]: self.remove_zero_dates(remove_zero_dates[1])
        
    def remove_zero_dates(self, indexs = [0]):
        incorrect_dates = []
        for i,x in enumerate(self.mat):
            for j in indexs:
                if x == None or x[j] == None or x[j] == 0: incorrect_dates.append(i)
        #adjusted_len = len(self.mat)  - len(incorrect_dates)
        mat = [] #np.zeros((adjusted_len, len(self.mat[1])))
        #j = 0
        for i,x in enumerate(self.mat):
            if i in incorrect_dates: continue
            #mat[j] = x
            mat.append(x)
            #j += 1
        self.mat = mat
        
    def get_trend_and_diff(self, data_index):
        data = self.extract_trend_data(data_index)
        dx = self.extract_trend_diffs(data_index)
        return [data, dx]
    
    def dates(self, dates_index = 0):
        return self.extract_dates(dates_index)
    
    def data(self, data_index = 1):
        return self.extract_trend_data(data_index)
    
    def dx(self, data_index = 1):
        return self.extract_trend_diffs(data_index)
        
    def get_normalised_weekly_trend(self, data_index):
        data = self.extract_trend_data(data_index)
        return self.extract_and_normalise_data(data)
        
    def extract_dates(self, dates_index):
        dates = []
        for x in self.mat:
            #if x == None or x[dates_index] == None or x[dates_index] == 0: continue
            if type(x[dates_index]) == int or type(x[dates_index]) == float or type(x[dates_index]) == np.float64:
                date_obj = datetime.datetime.fromtimestamp(x[dates_index])
                dates.append(mdates.date2num(date_obj))
            elif type(x[dates_index]) == datetime.date: dates.append(mdates.date2num(x[1]))
            else: raise('Dates data type not supported')
        return dates
    
    def extract_trend_data(self, data_index):
        data = []
        mat = self.mat
        for x in mat:
            data.append(x[data_index])
        return data
    
    def extract_trend_diffs(self, data_index):
        mat = self.mat
        dx = [0]
        for i,x in enumerate(self.mat):
            if i > 0: dx.append(mat[i][data_index] - mat[i-1][data_index])
        return dx
    
    def extract_weekly_normalised_data(self, data_index):
        dx = [0,0,0,0,0,0,0,0]
        norm_data = []
        data = [x[data_index] for x in self.mat]
        max_value = max(data)
        for i,x in enumerate(data):
            norm_data.append(x / max_value * 100)
            if i > 7: dx.append(norm_data[i]-norm_data[i-7])
        self.norm_data = norm_data
        return [norm_data, dx]
    
    
    