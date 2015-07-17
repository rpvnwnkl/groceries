#!/usr/bin/python
import urllib
import urlparse
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

tmpSite = urllib.urlretrieve('http://www.hannaford.com/catalog/browse_products.cmd', 'test')
tmpSite1 = urllib.urlretrieve('http://www.hannaford.com/thumbnail/Produce/Dressings-Dips-Juice/pc/28546/46810.uts?displayAll=true', 'test1')

tmpInfo = urlparse.urlparse('http://www.hannaford.com/catalog/browse_products.cmd')
tmpInfo1 = urlparse.urlparse('http://www.hannaford.com/thumbnail/Produce/Dressings-Dips-Juice/pc/28546/46810.uts?displayAll=true')
tmpInfo2 = urlparse.urlparse('http://www.hannaford.com/product/Chiquita-Banana-Bread-Mix/869835.uts?refineByCategoryId=46810')

##print tmpInfo, tmpInfo1, tmpInfo2

##Html Parser

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print 'Start tag: ', tag
		for attr in attrs:
			print '    attr: ', attr
	def handle_endtag(self, tag):
		print 'End tag  : ', tag
	def handle_data(self, data):
		print 'Data     : ', data
	def handle_comment(self, data):
		print 'Comment  : ', data
	def handle_entity(self, name):
		c = unichr(name2codepoint[name])
		print 'Named ent: ', c
	def handle_charref(self, name):
		if name.startswith('x'):
			c = unichr(int(name[1:], 16))
		else:
			c = unichr(int(name))
		print 'Num ent  : ', c
	def handle_decl(self, data):
		print 'Decl     : ', data

parser = MyHTMLParser()
##this url object is not correct. It is reading as an object, needs to be reading as string -->
tmpHtml = urllib.urlretrieve('http://www.hannaford.com/catalog/browse_products.cmd')##<--needs to be string?
print tmpHtml
parser.feed(tmpHtml)
