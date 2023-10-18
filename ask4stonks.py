# Tell em
print("Stonk Data Visualizer")
print("----------------------")

# Ask the user to enter the stock symbol for the company they want data for.
stonkSymbol = input("Enter stonk symbol: ")

# Ask the user for the chart type they would like.
print("Chart Types")
print("------------")
print("1. Bar\n2. Line")
chartType = input("Enter the chart type you want (1, 2): ")

# Ask the user for the time series function they want the api to use.
print("Select the Time Series of the chart you want to Generate")
print("---------------------------------------------------------")
print("1. Intraday\n2. Daily\n3. Weekly\n4. Monthly")
timeSeries = input("Enter the time series option (1, 2, 3, 4): ")

# Ask the user for the beginning date in YYYY-MM-DD format.
beginDate = input("Enter the start Date (YYYY-MM-DD): ")

# Ask the user for the end date in YYYY-MM-DD format. The end date should not be before the begin date.
endDate = input("Enter the end Date (YYYY-MM-DD): ")

# Generate a graph and open in the user’s default browser.