@echo off

powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%userprofile%\Start Menu\Programs\Startup\TwentyTwentyTwenty.lnk');$s.TargetPath='%~dp0/TwentyTwentyTwenty.exe';$s.Save()" && echo Success! This app should run on startup now

timeout /t 5