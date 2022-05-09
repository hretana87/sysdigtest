Sysdig test for Henry Retana.

The main goal of this brieaf proyect is to show basic knowledge with Selenium Web Driver and Python. The exercise consists in writing automated tests against app.sysdigcloud.com, with the goal of testing the log-in webpage (do not log in/no need to log in). Since log in is not necesary and in order to add some context, I will assume that this is a negative test for an invalid or not registered user.

Test case steps:

1-Open web browser Firefox (I am assuming the web browser).
2-Open site: app.sysdigcloud.com
3-Fill username text field with a valid email account but not registered on the site.
4-Fill password text field with a random text.
5-Click on login button.
6-Verify that error message is showed with text: "SOMETEXT"

Operating System: Ubuntu 20.04.3 LTS

Steps taken to create the test:

1- Check Python version: 
python3 --version 
Python 3.8.10

2- Checkk pip version:
pip3 --version
pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)

3- Install Selenium:
pip3 install selenium

4- Find for Selenium documentation: https://selenium-python.readthedocs.io/
5- Drivers for Web Browser(Firefox for this test) are required and can be downloaded at: https://github.com/mozilla/geckodriver/releases
6- Unzip and save the downloaded browser drivers into an specific location at the Oparating System and create a PATH to it:
export PATH=$PATH:/usr/local/bin/geckodriver
7-Write test code with Python and Selenium library
8-Improvement points:
  -Since this is a quick test, I wroted all the test in a single file, however it should implement Methods and Classes.
  -time.sleep() is used with showing purposes, however its not recommended for Production environments.
  -In order to improve element location, it is a good practice to specify more than one option at XPATH.
  -Also its a good practice to check error message text content, not only class name.


