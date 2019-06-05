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
          &num;CAVEMANANDWIFE2019
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
      <div id="story">
        <p>
          In the fall of 2016, Alicia was an officer for UT's pro-life student organization, and she posted an advertisement for the org in a Catholic Facebook group. That was William's first semester as a PhD student at UT. He saw the Facebook post, attended the org's first meeting, and met Alicia for the first time.
        </p>
        <p>
          They became friends that semester, participating in org activities together and chatting about ethics, controversial issues, and math. In January of 2017, they went to the LBJ library on their first date. Alicia was so nervous that she asked Paige K. (a bridesmaid) to tell William she was sick and couldn't go. But she did go, and it went great. They went on a few more dates before William asked Alicia to officially be his girlfriend on January 14, 2017.
        </p>
        <p>
          They spent many joyful months growing close and developing a solid, resilient, loving relationship. Using their complementary skills and interests, they launched a small pro-life organization in 2018 ("What's My Pro-Life Line?"). That project is surely just one of many "fruits" their relationship will bear.
        </p>
        <p>
          On their second anniversary, at Alicia's favorite place in Austin, William proposed to Alicia with his late grandmother's engagement ring. Nowadays, Alicia and Paige H. (the maid of honor) are planning their wedding. Meanwhile, William and Alicia are both relieved that William is (mostly) not involved. The couple prays together on a regular basis for their relationship and future marriage, and they are currently reading books to help them prepare for the sacrament.
        </p>
      </div>
      <img id="bottom-photo" src="/photos/97.jpg" srcset="/photos/97-5876.jpg 5876w, /photos/97-4197.jpg 4197w, /photos/97-2997.jpg 2997w, /photos/97-2140.jpg 2140w, /photos/97-1528.jpg 1528w, /photos/97-1091.jpg 1091w, /photos/779.jpg 779w, /photos/97-556.jpg 556w, /photos/97-397.jpg 397w" sizes="(min-width:2000px) 2000px, 100vw" />
    </frag>
  )
  
  page.compile("index.html", mainContents, stylesheet="/index.css", script="/index.js")
