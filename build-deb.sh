#!/bin/bash
mkdir ./deb/bin
cp ubuntu/* ./deb/bin/
sudo chown -R root:root ./deb
dpkg -b ./deb mew.deb
