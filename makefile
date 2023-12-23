x :
	which python
	echo hello

setup :
	sudo make _setup
	pip install requests==2.23 folium==0.2.1 pyvirtualdisplay selenium webdriver_manager  > /dev/null

_setup :
	apt-get update # to update ubuntu to correctly run apt install
#	apt install chromium-chromedriver
	-cp /usr/lib/chromium-browser/chromedriver /usr/bin
	apt-get install firefox-geckodriver
	whereis geckodriver
	apt install firefox  xvfb > /dev/null
	wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux32.tar.gz
	gunzip geckodriver-v0.31.0-linux32.tar.gz
	tar xvf geckodriver-v0.31.0-linux32.tar 

chromedriver_patched :
#	wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.56/linux64/chromedriver-linux64.zip
	wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/linux64/chromedriver-linux64.zip
	unzip chromedriver-linux64.zip
	#-rm -fr LICENSE.chromedriver chromedriver-linux64 chromedriver* chromedriver_patched
#	 version 114
	#wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
	#unzip chromedriver_linux64.zip
	cat chromedriver-linux64/chromedriver | sed s/cdc_/abc_/g > chromedriver_patched
	chmod a+x ./chromedriver_patched

	wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/linux64/chrome-headless-shell-linux64.zip
	unzip chrome-headless-shell-linux64.zip

start : orange

toro :
	PATH=$(PATH):. python etoro2.py


orange : chromedriver_patched
	PATH=$(PATH):. python orange.py

franck-ferrand :
	PATH=$(PATH):. python ferrand.py
