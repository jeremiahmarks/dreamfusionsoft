#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: jlmarks
# @Date:   2015-09-14 21:45:28
# @Last Modified 2015-09-15
# @Last Modified time: 2015-09-15 03:18:27


# dreamfusionsoft is the main package that I will build to make the importers job easier.
# it will work with the API, csv files, and be able to do basic, import related browser automation
# ie: file uploads or similar.

import ISServer


class MainController(object):
    """MainController is a class which will listen for various commands and then either start
    its loop or end it, depending on circumstances.
    """

    def __init__(self):
        print "Hello!  I am main controller.  You should be able to interact with me through various commands"
        print """The first of which will be "menu()". Please use that to bring up the menu!"""

    def menu(self):
        print """Hello and welcome to Dreamfusionsoft!

        """
    def hw(self):
        print "Hello World"

class interaction(object):
    """This class is a class which will govern the different actions in a
    """

a=MainController()

menu = a.menu
hw = a.hw
