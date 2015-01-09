# coding: utf-8

import ui
import editor
import os.path
import console
import webbrowser as wb
import clipboard as cb
import urllib

#cb.set(editor.get_text())

def update_wc(sender):
    info = os.path.split(editor.get_path())
    repo = info[0].split('/')[-1]
    path = info[1]
    cb.set(editor.get_text())
    url = 'working-copy://x-callback-url/write/?'
    f = {'repo':repo,'path':path,'x-success':'pythonista://'}
    url += urllib.urlencode(f).replace('+','%20')
    wb.open(url)

@ui.in_background    
def commit(sender):
    info = os.path.split(editor.get_path())
    repo = info[0].split('/')[-1]
    message = console.input_alert('Commit Message', 'Attach a message to your commit')
    url = 'working-copy://x-callback-url/commit/?'
    f = {'repo':repo,'message':message,'x-success':'pythonista://'}
    url += urllib.urlencode(f).replace('+','%20')
    wb.open(url)
    
@ui.in_background    
def commitOne(sender):                                                                                                   
    info = os.path.split(editor.get_path())
    repo = info[0].split('/')[-1]
    path = info[1]
    message = console.input_alert('Commit Message', 'Attach a message to your commit')
    url = 'working-copy://x-callback-url/commit/?'
    f = {'repo':repo,'message':message,'x-success':'pythonista://'}
    url += urllib.urlencode(f).replace('+','%20')
    wb.open(url)
    
def pushRepo(sender):
    info = os.path.split(editor.get_path())
    repo = info[0].split('/')[-1]
    f = {'repo':repo}
    url = 'working-copy://x-callback-url/push/?'
    url += urllib.urlencode(f).replace('+','%20')
    wb.open(url)
    
def pullRepo(sender):
    info = os.path.split(editor.get_path())
    repo = info[0].split('/')[-1]
    f = {'repo':repo}
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