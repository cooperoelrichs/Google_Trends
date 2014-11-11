from google_trends  import googleTrends
from csv_reader import csvReader
from trend_plotter import trendPlotter
from data_trend_analyzer import dataTrendAnalyzer

trend_dir = 'D:\Cooper\Google Drive\gtrends' #Windows trend dir
#trend_dir = '/Users/cooperoelrichs/Google Drive/gtrends' #Mac trend dir
asx_files = ['S&P200.csv']
key_words = ['debt']
#key_words += ['color', 'inflation', 'unemployment']

trend = googleTrends()
#trend.login('cdo.gtrends@gmail.com','80gbhdoj')
plot = trendPlotter(2, True)

for i,file_name in enumerate(asx_files):
    csv_dir     = trend_dir + '/' + file_name
    asx200      = csvReader(csv_dir, headers = True, date = True)
    datatrend   = dataTrendAnalyzer(asx200.get_mat(), [True,[0]])
    x           = datatrend.dates(0)
    y, dx       = datatrend.extract_weekly_normalised_data(1)
    plot.plot_trend(file_name.split('.')[0], x, y, dx, i)

for i,key in enumerate(key_words):
    #trend.get_trend(key,'all','AU', trend_dir) #2004 - present
    csv         = trend.open_trend_file(key, trend_dir)
    datatrend   = dataTrendAnalyzer(trend.process_trend_to_mat(csv, key), [True,[1,2]])
    x           = datatrend.dates(1)
    y           = datatrend.data(2)
    dx           = datatrend.dx(2)
    plot.plot_trend(key, x, y, dx, i + len(asx_files))

plot.show_plot()
