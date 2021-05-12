# candle stick chart
# neuralnine

import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mpf
import datetime as dt

start = dt.datetime(2019, 1, 1)
end = dt.datetime.now()

data = web.DataReader("TSLA", "yahoo", start, end)
# print(mpf.available_styles())  # prints all the style available
# mpf.plot(data, type="candle", style="nightclouds")    # we can use this also for simple usage
colors = mpf.make_marketcolors(up="#00ff00", down="#ff0000", wick="inherit", edge="inherit")

mpf_style = mpf.make_mpf_style(base_mpf_style="nightclouds", marketcolors=colors)
mpf.plot(data, type='candle', style=mpf_style, volume=True)
