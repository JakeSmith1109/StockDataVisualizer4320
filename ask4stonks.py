 # import random things to make code work
import re
import datetime
import requests

# Tell em
print("Stonk Data Visualizer")
print("----------------------")

# Ask the user to enter the stock symbol for the company they want data for.
stonkSymbol = input("\nEnter stonk symbol: ")
while not re.match("^[A-Z0-9]+$", stonkSymbol):
    print("Invalid input. Please enter a valid stock symbol.")
    stonkSymbol = input("Enter stonk symbol: ")

# Ask the user for the chart type they would like.
print("Chart Types")
print("------------")
print("1. Bar\n2. Line")
chartType = input("\nEnter the chart type you want (1, 2): ")
while chartType not in ['1', '2']:
    print("Invalid input. Please enter either '1' for Bar or '2' for Line chart.")
    chartType = input("Enter the chart type you want (1, 2): ")

# Ask the user for the time series function they want the api to use.
print("Select the Time Series of the chart you want to Generate")
print("---------------------------------------------------------")
print("1. Intraday\n2. Daily\n3. Weekly\n4. Monthly")
timeSeries = input("\nEnter the time series option (1, 2, 3, 4): ")
while timeSeries not in ['1', '2', '3', '4']:
    print("Invalid input. Please enter a valid time series option (1, 2, 3, 4).")
    timeSeries = input("Enter the time series option (1, 2, 3, 4): ")

# get those damn dates
while True:
    beginDate = input("\nEnter the start Date (YYYY-MM-DD): ")
    endDate = input("Enter the end Date (YYYY-MM-DD): ")

    try:
        # Ensure that the year has no more than 4 digits
        if len(beginDate) != 10 or len(endDate) != 10:
            print("Invalid date format. Please use YYYY-MM-DD format for dates.")
            continue

        begin_year = int(beginDate[:4])
        end_year = int(endDate[:4])

        # Ensure that the month has no more than 2 digits
        begin_month = int(beginDate[5:7])
        end_month = int(endDate[5:7])

        # Ensure that the day has no more than 2 digits
        begin_day = int(beginDate[8:10])
        end_day = int(endDate[8:10])

        if not (1000 <= begin_year <= 9999 and 1000 <= end_year <= 9999):
            print("Year should have 4 digits.")
        elif not (1 <= begin_month <= 12 and 1 <= end_month <= 12):
            print("Month should have 2 digits or sbe in the range 1-12.")
        elif not (1 <= begin_day <= 31 and 1 <= end_day <= 31):
            print("Day should have 2 digits or be in the range 1-31.")
        elif endDate < beginDate:
            print("End date should not be before the begin date.")
        else:
            break
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format for dates.")


#Pulling from api based on time series
if timeSeries==1:
    #intraday is a little more tricky because there's an interval, and an optional month
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+stonkSymbol+'&interval=5min&apikey='+apiKey
    r = requests.get(url)
    data = r.json()

    print(data)
elif timeSeries==2:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+stonkSymbol+'&apikey='+apiKey
    r = requests.get(url)
    data = r.json()

    print(data)
    #Started architecture for filtering, the first line is to get to the actual data, which looks like a dictionary inside a dictionary 
    data=data["Time Series (Daily)"]
    #this will go through each of the dictionaries for each time series (day,week,month), each of which uses the date as the key value
    for dat in data:
        if dat==beginDate:
            continue
elif timeSeries==3:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+stonkSymbol+'&apikey='+apikey
    r = requests.get(url)
    data = r.json()

    print(data)
    data=data["Time Series (Weekly)"]
    for dat in data:
        if dat==beginDate:
            continue
elif timeSeries==4:
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='+stonkSymbol+'&apikey='+apikey
    r = requests.get(url)
    data = r.json()

    print(data)
    data=data["Time Series (Monthly)"]
    for dat in data:
        if dat==beginDate:
            continue


# Generate a graph and open in the user’s default browser.