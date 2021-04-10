1. Download and install python 3 

[download python 3](https://www.python.org/ftp/python/3.9.4/python-3.9.4-amd64.exe)

2. Download 
[phoneparsertg](https://github.com/mentecuantica/phoneparsertg/archive/refs/heads/main.zip)

2. Win+X - Windows Powershell
`Goto extracted folder phoneparsetg`

3. run `pip install -r requirements.txt`

4. Create config.ini file with the following contents from 
enter your phone number
you will recieve the code
enter this code
and afterwards create an application (it can be Android app, can be Desktop app - doesn't matter)
you will recieve `api_id` and `api_hash` values those need to be in config.ini, and the last value in config.ini is your TELEGRAM `username`
[mytgauth][https://my.telegram.org/auth]

### example of config.ini
```[main]
api_id = 3719444
api_hash = "7401507f43992e80d3e4fd400c1e4444"
username = @yourusername
```


### How to use script
Win+X

go to your command line to folder with phoneparsertg

enter: `python3 main.py`
then you will get a request for channel name, enter channel and wait data to parse, you will get an CSV file in folder csv , named after channel name
