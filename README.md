# Stock Notifier

If you like to stay updated on your favourite stock investments, this 
application keeps track of all your stocks and regularly checks for updates to
the stock prices. You can also configure the percentage change in stock value 
when you would like to receive alerts. The alerts are raised as desktop 
notifications.

## Feature list
| # | Feature                                                        | Implemented/Ongoing |
|---|----------------------------------------------------------------|---------------------|
| 1 | Notify stocks at regular intervals                             | Implemented         |
| 2 | Notifications when percentage change is greater than threshold | TODO                |
| 3 | Configurations to store as config in home as backup set        | TODO                |
| 4 | Ability to start on bootup                                     | TODO                |
| 5 | Add platform support to Linux                                  | TODO                |
| 6 | Add platform support to Windows                                | TODO                |

## Installation
To install the stock notifier application, run a pip install:
```sh
pip install stock-notifier
```

## Commands
To start monitoring run:
```sh
stock-notifier -s
```

To add a stock to the monitoring lists:
```sh
stock-notifier -a <STOCK_SYMBOL>
```

To remove a stock from the monitoring lists:
```sh
stock-notifier -r <STOCK_SYMBOL>
```