# Monkeytype Bot
<img alt="Python" src="https://img.shields.io/badge/-Python-4B8BBE?style=flat-square&logo=python&logoColor=white" />

There are two different versions: `script.py` & `script_anticheat.py`

`script.py` is designed to go as fast as possible, while `script_anticheat.py` is designed to evade Monkeytype's anticheat. 

### Reporting Issues

I have only been able to test this on MacOS Big Sur (1.6.4), Windows and Linux Distros are still untested.

Please report any issues in the issues section on the GitHub if you have any and I will do my best to help/fix any issues.

### Required Apps
- Python 3 installed (May work on Python 2, but only tested on 3.8.5)
- Latest version of Google Chrome/Chromium 

### Monkeytype ToS & These scripts

At the time of writing (4 May 2022), monkeytype prohibits botting typing tests. 

This bot was tested using a locally hosted version of the monkeytype website (obtainable through their GitHub) as to avoid breaking their ToS. 

As already agreed in the GNU licensing of this software:

In no event unless required by applicable law or agreed to in writing will I or any other party who was involved in the creation/modification of this program as permitted above, be liable to you for damages, including general, special, incidential or consequential damages arising out of the use or inability to use the program (including but not limited to loss of data or data being rendered inaccurate or losesses sustained by you or third parties or a failure of the program to operate with any other programs), even if such holder or other party has been advised of the possibility of such damages.

### Installation

To be able to use the bot, you must have the chrome web driver installed (included in the files) so that the program is able to control a Chrome window along with Python. 

You must also install Selenium, Pynput & PyAutoGUI through pip.

```pip3 install selenium pynput pyautogui```

#### MacOS
On MacOS, you will need to install the Chrome Driver via homebrew along with using chromedriver file.

To install HomeBrew:

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

To install ChromeDriver:

`brew install chromedriver`
