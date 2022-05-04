# Monkeytype Bot
<img alt="Python" src="https://img.shields.io/badge/-Python-4B8BBE?style=flat-square&logo=python&logoColor=white" />
A python bot that does the typing test for you.

There are two different versions: script.py & script_anticheat.py

script.py is designed to go as fast as possible, while script_anticheat.py is designed to evade Monkeytype's anticheat. 

### Reporting Issues

I have only been able to test this on MacOS Big Sur (1.6.4), Windows and Linux Distros are still untested.

Please report any issues in the issues section on the GitHub if you have any and I will do my best to help/fix any issues.

### Required Apps
- Python 3 installed (May work on Python 2, but only tested on 3.8.5)
- Latest version of Google Chrome/Chromium 

### Installation

To be able to use the bot, you must have the chrome web driver installed (included in the files) so that the program is able to control a Chrome window along with Python. 

You must also install Selenium, Pynput & PyAutoGUI through pip.

```pip3 install selenium pynput pyautogui```

### Monkeytype ToS & Botting

Monkeytype's ToS prohibits botting, and this code was tested on a locally hosted version of monkeytype as to avoid violating the anticheat. 

I cannot be held responsible for any actions monkeytype may take against you, or your account for using this code. 

#### MacOS
On MacOS, you will need to install the Chrome Driver via homebrew along with using chromedriver file.

To install HomeBrew:

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

To install ChromeDriver:

`brew install chromedriver`
