dbutils.fs.mkdirs("dbfs:/databricks/scripts/")
dbutils.fs.put("/databricks/scripts/selenium-init.sh","""
#!/bin/bash

# do a backup of the source 
cp /etc/apt/sources.list{,.bak}
 
sudo apt-get update --fix-missing
sudo apt-get install -y libnss3 libgconf-2-4 libfontconfig1
version=`curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE`
echo $version
wget -N https://chromedriver.storage.googleapis.com/${version}/chromedriver_linux64.zip -O /tmp/chromedriver_linux64.zip
unzip /tmp/chromedriver_linux64.zip -d /tmp/chromedriver/


sudo apt-get update
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get -y update
sudo apt -y install ./google-chrome*.deb

pip install selenium
pip install webdriver-manager
""", True)
display(dbutils.fs.ls("dbfs:/databricks/scripts/"))
