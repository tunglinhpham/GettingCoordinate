# Getting Coordinate for a list of addresses from Google Maps

Want a simple, CHEAP way to convert your free-text addresses into coordinates? This project is your friend!

You should have Python 3.10 and PyCharm (community version) on your computer to run this project. Also, you have to download a Chrome Webdriver (https://chromedriver.chromium.org/downloads), then unzip it into a folder. 

Before running the code, please change the link of your Chrome Webdriver, input file & output file, as well as the default point on Google Maps (optional).

At the start, a message will pop up to ask the user to allow using cookies. Click "I agree" as soon as possible, otherwise the code cannot continue.
![Picture 1](https://github.com/tunglinhpham/GettingCoordinate/blob/main/Screenshot/Accept%20Cookies.jpg)

After that, just wait until the code finishes. The output file should be inside the folder that you specified at the start of the code.

In some cases, the address cannot be found (for example, multiple results), which will result a "Cannot be found" in the output file. Also, this code is not fast, as it has to wait for 2 seconds after clicking the Search button to make sure Google can show the proper result. I'm very happy to see some suggestions to overcome those problems.

Happy scraping!
