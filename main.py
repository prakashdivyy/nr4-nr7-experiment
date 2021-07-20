import investpy
import pandas as pd
from datetime import datetime, timedelta
pd.options.mode.chained_assignment = None


def show_nr_4(ticker):
    search_result = investpy.search_quotes(text=ticker, products=['stocks'],
                                           countries=['united states'], n_results=1)

    today_date = datetime.utcnow().date()

    recent_data = search_result.retrieve_recent_data()

    try:
        recent_data.loc[today_date.strftime("%Y-%m-%d")]
        last_day = today_date - timedelta(days=1)

        five_days_data = recent_data.tail(5)
        four_days_data = five_days_data.head(4)
        return calculate_nr_4(four_days_data, last_day)
    except:
        last_day = list(recent_data.tail(1).index)[0].to_pydatetime().date()
        four_days_data = recent_data.tail(4)
        return calculate_nr_4(four_days_data, last_day)


def calculate_nr_4(four_days_data, last_day):
    four_days_data['Narrow'] = abs(
        four_days_data['High'] - four_days_data['Low'])

    lowest_narrow = four_days_data.nsmallest(1, 'Narrow')
    lowest_date = list(lowest_narrow.index)[0].to_pydatetime().date()

    is_equal_date = last_day == lowest_date
    return is_equal_date


stock_list = ["AAPL", "MSFT", "AMZN", "GOOG", "GOOGL", "FB", "TSLA"]
today_watchlist = []
for s in stock_list:
    if show_nr_4(s):
        today_watchlist.append(s)

print(today_watchlist)
