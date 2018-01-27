#!/usr/bin/env python

import platform
import json
import os
import re
import sys

class MEW(object):

	package_manager = None
	command = None
	arguments = None
	version = None
	distro = None
	_package_manager = None
	translated = None
	_managers = ['apt-get','apt','pacman','dnf','rpm','zypper','emerge','equery']
	_superDistros = ['debian','ubuntu','redhat','fedora','sles','opensuse','gentoo']

	def __init__(self, package_manager, command, arguments):

		self.package_manager = package_manager # package manager in cli
		if not self.val_pac_manager():
			sys.exit("Error : '{0}' is not a valid Package Manager".format(self.package_manager))
		self.command = command # command in cli
		self.arguments = arguments # args in cli
		self.version = platform.version().lower() # version of linux
		self.distro = self.getDistro() # linux distro 
		self._package_manager = self.getPackageManager() # package manager for this distro
		self.translated = self.translate()

	def val_pac_manager(self):

		if self.package_manager in self._managers:
			return True
		return False

	def getDistro(self):

		for distro in self._superDistros:
			if distro in self.version:
				return distro

	def getPackageManager(self):

		distroData = json.load(open(os.path.join(os.path.realpath(__file__).replace("MEW.pyc","").replace("MEW.py","") ,"data", "distro.json")))

		if distroData[self.distro]:
			return distroData[self.distro]

	def translate(self):

		pacman_file = os.path.join(os.path.realpath(__file__).replace("MEW.pyc","").replace("MEW.py",""), "data", self.package_manager + ".json")
		pacman_data = json.load(open(pacman_file)) # load json of the package manager

		if re.match("-Sy+u",self.command):
			self.command = "-Syu"

		try:
			if not pacman_data[self.command]:
				return None
			return self.format(pacman_data[self.command][self.distro])
		except KeyError:
			return None

	def format(self, translate):

		if "$vars" in translate:
			if self.checkArgs():
				return translate.replace("$vars", ''.join(self.arguments).replace("@",' ')[1:])
			else:
				translate = None
		return translate	

	def checkArgs(self):

		if not len(self.arguments):
			print "Error : Arguments must start with '@'"
			return False

		for args in self.arguments:
			if not args.startswith("@"):
				print "Error : Arguments must start with '@'"
				return False

		return True



"""
.replace("MEW.pyc","").replace("MEW.py","")
replaces both of them so that we can get the directory 
from the MEW.py file. .pyc is replaced because after it is 
a used once then .pyc file is the main __file__
"""