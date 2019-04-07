# -*- coding: pyxl -*-
from pyxl import html

import page

def compile():
  mainContents = (
    <frag>
      <div id="days-to-go">
        <img src="/photos/111-2525.jpg" srcset="/photos/111-2525.jpg 2525w, /photos/111-1803.jpg 1803w, /photos/111-1287.jpg 1287w, /photos/111-919.jpg 919w" sizes="2400px" id="top-img" />
        <span id="days-to-go-text"><span id="countdown">298</span> DAYS TO GO</span>
      </div>
      <div id="bride-and-groom">
        <div id="circle">
          <div class="spouse">
            ALICIA<br />TORRES
          </div>
          <div id="and">
            AND
          </div>
          <div class="spouse">
            WILLIAM<br />HOZA
          </div>
        </div>
      </div>
      <div id="event-basics">
        <div id="event-hashtag">
          #CAVEMANANDWIFE2019
        </div>
        <div id="place-and-date">
          <div class="event-fact">
            <div>AUSTIN, TEXAS</div>
          </div>
          <div class="event-fact">
            <div><time datetime="2019-11-08">NOVEMBER 8, 2019</time></div>
          </div>
        </div>
      </div>
      <img id="bottom-photo" src="/photos/97.jpg" srcset="/photos/97-5876.jpg 5876w, /photos/97-4197.jpg 4197w, /photos/97-2997.jpg 2997w, /photos/97-2140.jpg 2140w, /photos/97-1528.jpg 1528w, /photos/97-1091.jpg 1091w, /photos/779.jpg 779w, /photos/97-556.jpg 556w, /photos/97-397.jpg 397w" sizes="(min-width:2000px) 2000px, 100vw" />
    </frag>
  )
  
  page.compile("index.html", mainContents, stylesheet="/index.css", script="/index.js")
