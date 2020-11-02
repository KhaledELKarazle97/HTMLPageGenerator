import pyautogui as p
import os
import sys
import subprocess
import time
import webbrowser

subprocess.Popen(['notepad.exe'])
time.sleep(2)
p.click(p.locateOnScreen('notepad.PNG')[0],p.locateOnScreen('notepad.PNG')[1])
time.sleep(1)
p.write('<!DOCTYPE html>\n'
'<html lang="en">\n'
'<head>\n'
    '<meta charset="UTF-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    "<link rel='stylesheet' href='site.css'>"
    '\n<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">'
    '\n<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">'
    '\n<link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.css">'
    '\n<link rel="stylesheet" href="https://unpkg.com/swiper/swiper-bundle.min.css">'   
    '\n<title>'+sys.argv[1]+'</title>'
'\n</head>'
'\n<body>')

p.press('enter', presses=2)
p.write('<nav class="navbar navbar-expand-lg navbar-light bg-light">'
  '\n<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03" aria-expanded="false" aria-label="Toggle navigation">'
    '\n<span class="navbar-toggler-icon"></span>'
  '\n</button>'
  '\n<a class="navbar-brand" href="#">'+sys.argv[1]+'</a>'

  '\n<div class="collapse navbar-collapse" id="navbarTogglerDemo03">'
    '\n<ul class="navbar-nav mr-auto mt-2 mt-lg-0">'
      '\n<li class="nav-item active">'
        '\n<a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>'
      '\n</li>'
      '\n<li class="nav-item">'
        '\n<a class="nav-link" href="#">Link</a>'
      '\n</li>'
      '\n<li class="nav-item">'
        '\n<a class="nav-link disabled" href="#">Disabled</a>'
      '\n</li>'
    '\n</ul>'
    '\n<form class="form-inline my-2 my-lg-0">'
      '\n<input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">'
      '\n<button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>'
    '\n</form>'
  '\n</div>'
'\n</nav>'
'\n<div class="container">'
'\n<h1>'+sys.argv[1]+' was actually created by a bot :) !</h1>'
'\n<div/>')
p.press('enter', presses=2)

p.write(
'\n</body>'
'\n<script defer src="https://code.jquery.com/jquery-3.5.1.js" integrity="sha256-QWo7LDvxbWT2tbbQ97B53yJnYU3WhH/C8ycbRAkjPDc=" crossorigin="anonymous"></script>'
'\n<script defer src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>'
'\n<script defer src="https://unpkg.com/swiper/swiper-bundle.js"></script>'
'\n<script defer src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>'
'\n</html>'
)

p.hotkey('ctrl','s')
p.write('index.html')
p.press('tab')
time.sleep(2)
p.press('down',presses=3)
time.sleep(2)
p.press('enter',presses=2)
time.sleep(2)
p.hotkey('alt','f4')
time.sleep(2)
webbrowser.open('file:///C:/Users/Khaled/Desktop/index.html')