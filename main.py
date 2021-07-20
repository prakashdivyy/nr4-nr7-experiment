import investpy

search_result = investpy.search_quotes(text='amd', products=['stocks'],
                                       countries=['united states'], n_results=1)
print(search_result)

recent_data = search_result.retrieve_recent_data()
print(recent_data.head())
