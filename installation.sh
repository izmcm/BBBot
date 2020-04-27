#!/bin/sh

echo "instalando python3..."
sudo apt-get install python3

echo "instalando Selenium..."
sudo pip3 install selenium

echo "instalando OpenCV..."
sudo pip3 install opencv-python

echo "install geckodriver..."
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/