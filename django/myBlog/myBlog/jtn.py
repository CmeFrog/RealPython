import os
print "__file__ = " + __file__
SETTING_DIR = os.path.dirname(__file__)
print "SETTING_DIR = os.path.dirname(__file__) = " + SETTING_DIR
BASE_DIR = os.path.dirname(SETTING_DIR)
print "BASE_DIR = os.path.dirname(SETTING_DIR) = " + BASE_DIR
print "os.pardir = " + os.pardir
PROJECT_PATH = os.path.join(SETTING_DIR, os.pardir)
print "PROJECT_PATH = os.path.join(SETTING_DIR, os.pardir) = " + PROJECT_PATH
PROJECT_ROOT = os.path.abspath(PROJECT_PATH)
print "PROJECT_ROOT = os.path.abspath(PROJECT_PATH) = " + PROJECT_ROOT
