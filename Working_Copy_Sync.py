# coding: utf-8

import ui
import editor
import os.path
import console
import webbrowser as wb
import clipboard as cb
import urllib

key = 'YourKeyHere'

def copy_from_wc(sender):
    # I haven't gotten this function to work yet.
    info = os.path.split(editor.get_path())
    repo = info[0].split('/')[-1]
    path = info[1]
    url = 'working-copy://x-callback-url/read/?'
    success = 'pythonista://WC_Sync/Update.py?action=run&args=' + editor.get_path() + ' '
    f = {'repo':repo,'path':path,'key':key,'x-success':success}
    url += urllib.urlencode(f).replace('+','%20')
    print url
    wb.open(url)

@ui.in_background
def update_wc(sender):
    info = os.path.split(editor.get_path())
    repo = info[0].split('/')[-1]
    path = info[1]
    path = console.input_alert('File Name', 'Specify which file to update on Working Copy', path)
    cb.set(editor.get_text())
    url = 'working-copy://x-callback-url/write/?'
    f = {'repo':repo,'path':path,'key':key,'x-success':'pythonista://'}
    url += urllib.urlencode(f).replace('+','%20')
    wb.open(url)
    
@ui.in_background    
def commit(sender):
    info = os.path.split(editor.get_path())
    repo = info[0].split('/')[-1]
    message = console.input_alert('Commit Message', 'Attach a message to your commit')
    url = 'working-copy://x-callback-url/commit/?'
    f = {'repo':repo,'message':message,'limit':100,'key':key,'x-success':'pythonista://'}
    url += urllib.urlencode(f).replace('+','%20')
    wb.open(url)
    
@ui.in_background    
def commitOne(sender):                                                                                                   
    info = os.path.split(editor.get_path())
    repo = info[0].split('/')[-1]
    path = info[1]
    message = console.input_alert('Commit Message', 'Attach a message to your commit')
    url = 'working-copy://x-callback-url/commit/?'
    f = {'repo':repo,'message':message,'key':key,'x-success':'pythonista://'}
    url += urllib.urlencode(f).replace('+','%20')
    wb.open(url)
    
def pushRepo(sender):
    info = os.path.split(editor.get_path())
    repo = info[0].split('/')[-1]
    f = {'repo':repo,'key':key,'x-success':'pythonista://'}
    url = 'working-copy://x-callback-url/push/?'
    url += urllib.urlencode(f).replace('+','%20')
    wb.open(url)
    
def pullRepo(sender):
    info = os.path.split(editor.get_path())
    repo = info[0].split('/')[-1]
    f = {'repo':repo,'key':key,'x-success':'pythonista://'}
    url = 'working-copy://x-callback-url/pull/?'
    url += urllib.urlencode(f).replace('+','%20')
    wb.open(url)

view = ui.load_view('Working_Copy_Sync')

repoList = view['repoList']
copyb = view['copyb']
writeb = view['writeb']
commitOneb = view['commitOneb']
commitb = view['commitb']
pushb = view['pushb']
pullb = view['pullb']
addCurrentb = view['addCurrentb']

view.present('sidebar')