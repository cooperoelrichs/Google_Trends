from google_trends import googleTrends
from trend_plotter import trendPlotter

trend_dir = 'D:\Cooper\Google Drive\gtrends' #Windows trend dir
#trend_dir = '/Users/cooperoelrichs/Google Drive/gtrends' #Mac trend dir
key_words = ['debt']

trend = googleTrends()
#trend.login('cdo.gtrends@gmail.com','80gbhdoj')
plot = trendPlotter(2, True)

for i,key in enumerate(key_words):
    #trend.get_trend(key,'all','AU', trend_dir) #2004 - present
    csv  = trend.open_trend_file(key, trend_dir)
    data = trend.process_trend_to_mat(csv, key)
    plot.plot_trend_with_diff(data, key, 1, 2, i)

plot.show_plot()