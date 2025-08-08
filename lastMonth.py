import datetime
import calendar

def getReportTimeRange():


    #
    # get today, then use it to derive last month's year, last month and
    # last month's last day
    #
    d = datetime.date.today()
    year = d.year
    month = d.month
    if month == 1:
        lastMonth = 12
        lastMonthYear = year -1
    else:
        lastMonth =  month - 1
        lastMonthYear = year

    lastMonthDays = calendar.monthrange(lastMonthYear, lastMonth)[1]

    #
    # form report time range
    #
    if lastMonth < 10:
        lastMonthString = '0' + str(lastMonth)
    else:
        lastMonthString = str(lastMonth)

    startTime = str(lastMonthYear) + '-' + lastMonthString + '-01T00:00:00Z'
    endTime = str(lastMonthYear) + '-' + lastMonthString + '-' + str(lastMonthDays) + 'T23:59:59.999Z'

    monthName = calendar.month_abbr[lastMonth]
    yearString = str(lastMonthYear)

    return (startTime, endTime, monthName, yearString)


