# coding: utf-8

import ui
import editor
import os
import console
import webbrowser as wb
import urllib
import base64
import time
import keychain

#This should not have leading or trailing /
INSTALL_PATH = 'wc_sync'

#Key set in checkKey funtion
key = None

def showPopupInputAlert(title, handler, text, yPos):
	v = ui.load_view('popoverInputAlert')
	v['label'].text = title
	v['buttonOK'].action = handler
	xPos = 990
	yPos = yPos + 84
	v['textfield'].text = text
	v['textfield'].begin_editing()
	v.height = 90
	v.present('popover', popover_location=(xPos,yPos), hide_title_bar=True)
	
def getPopupText(sender):
	text = None
	for v in sender.superview.subviews:
		if v.name =='textfield':
			text = v.text
	sender.superview.close()
	return text

def showPopupButton(title, handler, yPos):
	v = ui.load_view('popoverButton')
	v['button'].title = title
	v['button'].action = handler
	xPos = 990
	yPos = yPos + 75
	v.height = 6
	v.present('popover', popover_location=(xPos,yPos), hide_title_bar=True)
	
def closePopup(sender):
	sender.superview.close()

def info():
	documentsDir = os.path.expanduser('~/Documents')
	info = editor.get_path()
	#documentsDir starts with '/private' whereas info does not
	fullPath = info[len(documentsDir)-7:]
	path = fullPath.split('/',1)[1]
	repo = fullPath.split('/',1)[0]
	return repo,path
	
def sendB64(repo,path,text):
	url = 'working-copy://x-callback-url/write/?'
	b64 = base64.b64encode(text)
	f = {'repo':repo,'path':path,'key':key,'base64':b64,'x-success':'pythonista://'}
	url += urllib.urlencode(f).replace('+','%20')
	wb.open(url)

def sendText(repo,path,text):
	url = 'working-copy://x-callback-url/write/?'
	f = {'repo':repo,'path':path,'key':key,'text':text,'x-success':'pythonista://'}
	url += urllib.urlencode(f).replace('+','%20')
	wb.open(url)
	
def open_wc(sender): # Opens working copy
	wb.open('working-copy://')

@ui.in_background
def copyFromWCPt1(sender):
	showPopupButton('Pull', copyFromWCPt2, sender.y)
	
def copyFromWCPt2(sender):	 # Copies the text from the working copy version of the file and uses it to overwrite the contents of the corresponding file in pythonista.
	closePopup(sender)
	repo,path = info()
	url = 'working-copy://x-callback-url/read/?'
	success = 'pythonista://'+INSTALL_PATH+'/rxFile.py?action=run&argv=' + os.path.join(repo,path) +'&argv='
	f = {'repo':repo,'path':path,'key':key, 'base64':'1'}
	url += urllib.urlencode(f).replace('+','%20')
	url += '&x-success=' + urllib.quote_plus(success)
	wb.open(url)

def sendToWCPt1(sender):
	showPopupButton('Push', sendToWCPt2, sender.y)

def sendToWCPt2(sender): # Sends the contents of the file in pythonista to overwrite the working copy version.
	closePopup(sender)
	repo,path = info()
	sendText(repo,path,editor.get_text())

def sendPYUIToWCPt1(sender):
	showPopupButton('Push .pyui', sendPYUIToWCPt2, sender.y)
	
def sendPYUIToWCPt2(sender):
	closePopup(sender)
	repo,path = info()
	path += 'ui'
	fullPath = os.path.join(os.path.expanduser('~/Documents'), os.path.join(repo,path))
	with open(fullPath) as file:
		sendB64(repo,path,file.read())
		
def getZipPt1(sender):
	showPopupInputAlert('Repository', getZipPt2, "", sender.y)

def getZipPt2(sender):
	repo = getPopupText(sender)
	if len(repo) > 0: 
		url = 'working-copy://x-callback-url/zip/?'
		f = {'repo':repo, 'key':key}
		success ='pythonista://'+INSTALL_PATH+'/rxZip.py?action=run&argv='+repo+'&argv='
		url += urllib.urlencode(f).replace('+','%20')
		url += '&x-success=' + urllib.quote_plus(success)
		wb.open(url)

def checkKey():
	global key
	key = keychain.get_password('wcSync','xcallback')
	if key == None:
		pwd = console.password_alert('Working Copy Key')
		keychain.set_password('wcSync','xcallback',pwd)
	
def main():
	checkKey()
	view = ui.load_view('Working_Copy_Sync')
	view.present('sidebar')

#psuedo main() function
if __name__ == "__main__":
	main()