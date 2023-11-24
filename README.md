# Whspdefendor Exploit Framework v1.0 💬
![banner image](https://github.com/anezatra/whspdefendor/blob/main/banner.jpg)
## What is a whspdefendor framework?
**Whatsapp Defendor is an advanced penetration testing tool that allows us to perform penetration testing on the messaging platform WhatsApp. This tool, designed to work entirely with selenium, can also perform penetration tests for Android.**
## All Commands 💻
**The commands available in whspdefendor are as follows:**
```
General commands
=================

	Command               Description
	---------             -------------
	help/?                Show this help menu.
	os      <command>     Execute a system command without closing the framework
	banner                Display banner.
	exit/quit             Exit the framework.

Core commands
=============

	Command               Description
	---------             -------------
	database              Prints the core version and then check if it's up-to-date.
	debug                 Drop into debug mode or disable it. (Making identifying problems easier)
	reset/format          Reset all outputs and database

Resources commands
==================

	Command               Description
	---------             -------------
	history               Display commandline most important history from the beginning.
	makerc                Save the most important commands entered since start to a file.
	
Sessions management commands
============================

	Command               Description
	---------             -------------
	sessions              Dump session listings and display information about sessions.
	jobs                  Displays and manages jobs.

Module commands
===============

	Command               Description
	----------            --------------
	show                  List modules you can use.
	options               Displays options for the current module.
	set                   Sets a context-specific variable to a value.
	run                   Launch the current module.
	use     <module>      Use an available module.
	info    <module>      Get information about an available module.
	back                  Move back from the current context.
```
## Current modules 📋
` exploit/windows/whatsapp/session_hijacking ` 
` exploit/android/whatsapp/grabber_files `   
## How to download 💡
**You can download whspdefendor directly by saying** <br/><br/>
` pip install -r requirements.txt `
## or <br/>
` python -m pip install -r requirements.txt ` <br/>
## Required python version 📌
` python 3.x `
## Required system platforms 🛠️
**Linux Debian/Ubuntu and Windows is working**
## About 🚀
**My gmail adress: anezatra@gmail.com**
