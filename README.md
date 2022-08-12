# trading_expiry
library to fetch nse trading expiry and holiday.

## installation
install using pip
```
pip install git+https://github.com/Rahulghuge94/trading_expiry.py
```

## usage
this library downloads holiday from nse india website. you may find error while
using this file on aws or colab. In that case create holiday_{year}.json from
https://www.nseindia.com/api/holiday-master?type=trading .
```
import trading_expiry
print(trading_expiry.week_expiry,
      trading_expiry.next_week_expiry,
      trading_expiry.month_expiry)
```
