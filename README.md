Simple automation example that automates the "Rush" piano game found at http://tanksw.com/piano-tiles/.  Work based upon work done by [Kian Brose](https://github.com/KianBrose/Image-Recognition-Botting-Tutorial).

This work leverages the pyautogui and pywin32 libraries.  The pywin32 library, in particular, caused a lot of issues due to Python version compatibility issues.  To solve the issue in Python 3.8 or 3.9, specialized libraries and administrator-level access was necessary.

In this repo, the environment.yml file has been included to help with conflicts.  To utilize it:
* Install Anaconda
* Create a environment `conda create -n pyautogui_demo`
* Activate that environment `conda activate pyautogui_demo`
* Create a directory for this repository to be cloned to: `New-Item  ~\repos\pyautogui_demo -ItemType Directory; cd ~\repos\pyautogui_demo`
* Clone this repo
* Execute environment.yml `conda env update --name pyautogui_demo --file environment.yml`
* Run `python ./pyautogui_demo.py`
* Use the first part to find the coordinates of the piano keys
* Hit control-C to exit pyautogui.pixel and start the game
