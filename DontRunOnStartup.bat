@echo off

del "C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\TwentyTwentyTwenty.lnk" && echo Success! This app shouldn't run on startup now

timeout /t 5