dbutils.fs.mkdirs("dbfs:/databricks/scripts/")
dbutils.fs.put("/databricks/scripts/init_file_118.sh","""
#!/bin/bash
# do a backup of the source 
cp /etc/apt/sources.list{,.bak}
 
sudo apt-get update --fix-missing
sudo apt-get install -y libnss3 libgconf-2-4 libfontconfig1
version=118.0.5993.70
echo $version
wget -N https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${version}/linux64/chromedriver-linux64.zip -O /tmp/chromedriver_linux64.zip
unzip /tmp/chromedriver_linux64.zip -d /tmp/chromedriver/

sudo apt-get update
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get -y update
sudo apt -y install ./google-chrome*.deb
pip install selenium
pip install webdriver-manager==3.8.6
""", True)
display(dbutils.fs.ls("dbfs:/databricks/scripts/"))
