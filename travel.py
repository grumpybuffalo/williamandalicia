# -*- coding: pyxl -*-
from pyxl import html

import page

def compile():
  mainContents = (
    <frag>
      <h2>
        TRAVEL
      </h2>
      <div class="schedule-item">
        <div class="schedule-item-basics">
          <div class="schedule-item-name">
            Holiday Inn Austin Town Lake
          </div>
          <div class="schedule-item-datetime">
            Hotel
          </div>
          <div class="schedule-item-location">
            The group rate is $145/night (while rooms are available). To get this rate:
            <ul style="text-align:left;">
              <li>
                If you are checking in on Thursday, November 7 and checking out on Saturday, November 9, you can book your room online using <a href="https://www.holidayinn.com/redirect?path=hd&brandCode=HI&localeCode=en&regionCode=1&hotelCode=AUSTL&_PMID=99801505&GPC=THW&cn=no&viewfullsite=true">this link</a>, which will automatically fill in group code <b>THW</b>. You can also book your room over the phone by calling 1-888-615-0509; say you are a guest at the <b>Torres Hoza Wedding</b>.
              </li>
              <li>
                Otherwise, please book your room over the phone by calling Lovinia at 512-634-1275. Say you are a guest at the <b>Torres Hoza Wedding</b>.
              </li>
            </ul>
          </div>
        </div>
        <div class="schedule-item-details">
          <img src="hotel.jpg" class="schedule-photo" />
          <div class="schedule-item-location">
            20 North Ih-35<br />
            Austin, TX 78701<br />
          </div>
        </div>
      </div>
      <div class="schedule-item">
        <div class="schedule-item-basics">
          <div class="schedule-item-name">
            Austin-Bergstrom International Airport (AUS)
          </div>
          <div class="schedule-item-datetime">
            Airport
          </div>
          <div class="schedule-item-location">
            This is the closest airport. If you're staying at the Holiday Inn Austin Town Lake, a free shuttle is available 24 hours a day.
          </div>
        </div>
        <div class="schedule-item-details">
          <img src="airport.jpg" class="schedule-photo" />
          <div class="schedule-item-location">
            3600 Presidential Blvd<br />
            Austin, TX 78719
          </div>
        </div>
      </div>
    </frag>
  )
  
  page.compile("travel/index.html", mainContents, stylesheet="/schedule/index.css", title="Travel")
