from google_trends  import googleTrends
from csv_reader     import csvReader
from trend_plotter  import trendPlotter

#trend_dir = 'D:\Cooper\Google Drive\gtrends' #Windows trend dir
trend_dir = '/Users/cooperoelrichs/Google Drive/gtrends' #Mac trend dir
asx_files = ['S&P200.csv']
key_words = ['debt']
#key_words += ['color', 'inflation', 'unemployment']

trend = googleTrends()
#trend.login('cdo.gtrends@gmail.com','80gbhdoj')
plot = trendPlotter(2, True)

for i,file_name in enumerate(asx_files):
    csv_dir = trend_dir + '/' + file_name
    asx200 = csvReader(csv_dir, headers = True, date = True)
    mat = asx200.get_mat()
    plot.plot_trend_with_diff(mat, file_name.split('.')[0], 0, 1, i, True)

for i,key in enumerate(key_words):
    #trend.get_trend(key,'all','AU', trend_dir) #2004 - present
    csv  = trend.open_trend_file(key, trend_dir)
    data = trend.process_trend_to_mat(csv, key)
    plot.plot_trend_with_diff(data, key, 1, 2, i + len(asx_files))

plot.show_plot()