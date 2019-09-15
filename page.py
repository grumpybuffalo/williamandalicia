# -*- coding: pyxl -*-
from pyxl import html

def compile(filename, mainContents, title=None, stylesheet=None, scripts=[]):
  gaScript1 = <script src="https://www.googletagmanager.com/gtag/js?id=UA-123337994-2"></script>
  gaScript2 = <script>{html.rawhtml("""window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'UA-123337994-2');""")}</script>
  
  gaScript1.set_attr("async", "") # async is a Python keyword, so we have to set this attribute manually
  
  if stylesheet == None:
    stylesheetLink = None
  else:
    stylesheetLink = <link rel="stylesheet" href="{stylesheet}" />
  
  scriptElement = <frag></frag>
  for script in scripts:
    scriptElement.append(<script src="{script}"></script>)
  
  doc = (
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        {gaScript1}
        {gaScript2}
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>
          {title + " | " if title != None else None}Alicia Torres and William Hoza's Wedding Website
        </title>
        <link href="https://fonts.googleapis.com/css?family=PT+Sans|Quicksand:300,400&display=swap" rel="stylesheet" />
        <link rel="stylesheet" href="/assets/index4.css" />
        {stylesheetLink}
      </head>
      <body>
        <div id="flow">
          <header>
            <div id="header-event-basics">
              <time datetime="2019-11-08" style="margin-right:20px;">November 8, 2019</time>
              Austin, TX
              <span style="float:right;">
                &num;cavemanandwife2019
              </span>
            </div>
            <div id="h1-line">
              <h1>
                ALICIA &amp; WILLIAM
              </h1>
              <button id="nav-show-button" onclick="showNav();">Menu</button>
            </div>
            <nav>
              <div><button id="nav-hide-button" onclick="hideNav();">Hide</button></div>
              <div><a href="/">HOME</a></div>
              <div><a href="/schedule/">SCHEDULE</a></div>
              <div><a href="/rsvp/">RSVP</a></div>
              <div><a href="/travel/">TRAVEL</a></div>
              <div><a href="/wedding-party/">WEDDING PARTY</a></div>
              <div><a href="/photos/">PHOTOS</a></div>
              <div><a href="/our-catholic-wedding/">OUR CATHOLIC WEDDING</a></div>
              <div><a href="/places-of-interest/">PLACES OF INTEREST</a></div>
              <div><a href="https://www.zola.com/registry/alicia-william">REGISTRY</a></div>
            </nav>
          </header>
          <main>
            {mainContents}
          </main>
        </div>
        
        {scriptElement}
        <script src="/assets/index.js"></script>
      </body>
    </html>
  )
  
  file = open(filename, "w", encoding="utf-8")
  file.write("<!DOCTYPE html>" + str(doc))
