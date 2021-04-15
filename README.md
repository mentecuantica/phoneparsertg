
# PhoneParserTg
It allows you to get all telephone numbers (if any are open) from telegram groups users, and save it to CSV file



### Installation and usage

- Download and install python 3 

[download python 3](https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe)

- Download 
[phoneparsertg](https://github.com/mentecuantica/phoneparsertg/archive/refs/heads/main.zip), and extract it to `C:\phoneparsertg`

- Win+X - Windows Powershell
`cd c:\phoneparsertg`

- run `pip install -r requirements.txt`

- Create config.ini file with the following contents from 
enter your phone number
you will recieve the code
enter this code
and afterwards create an application (it can be Android app, can be Desktop app - doesn't matter)
you will recieve `api_id` and `api_hash` values those need to be in config.ini, and the last value in config.ini is your TELEGRAM `username`
[mytgauth][https://my.telegram.org/auth]

### example of config.ini - no brackets in config ini
```
[main]
api_id = 3719444
api_hash = 7401507f43992e80d3e4fd400c1e4444
username = @yourusername
```


### How to use script
Win+X

`cd c:\phoneparsertg`
go to your command line to folder with phoneparsertg

enter: `python main.py`
then you will get a request for channel name, enter channel and wait data to parse, you will get an CSV file in folder csv , named after channel name
