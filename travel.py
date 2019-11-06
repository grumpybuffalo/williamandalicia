# -*- coding: pyxl -*-
from pyxl import html

import page

def compile():
  mainContents = (
    <frag>
      <h2>
        TRAVEL
      </h2>
      <div class="schedule-item" style="margin-top:50px;">
        <div class="schedule-item-basics">
          <div class="schedule-item-name">
            Austin Charter Services
          </div>
          <div class="schedule-item-datetime">
            Shuttle
          </div>
          <div class="schedule-item-location">
            Unfortunately, parking is limited at all event locations.
            Shuttle service will be provided from the <u>ceremony to the
            reception</u> and, at the end of the reception, from the <u>reception
            to the Holiday Inn Austin Town Lake</u>. That being said, if
            you do end up parking, here are some suggestions.
            <ul style="text-align:left;">
              <li>
                For the <b>rehearsal dinner / welcome party</b>, Capital
                Cruises <a href="http://www.capitalcruises.com/map-directions/">suggests</a> parking
                at the Hyatt Regency Hotel.
              </li>
              <li>
                For the <b>rehearsal / ceremony</b>, consider parking at
                the <a href="https://staustin.org/parking">St. Austin parking
                garage</a> at 500 W. Martin Luther King Blvd.
              </li>
              <li>
                For the <b>reception</b>, you can try parking in the
                overflow parking lot across Lake Austin Boulevard from
                Abel's. Follow signs for "Oyster Landing Additional
                Parking".
              </li>
            </ul>
          </div>
        </div>
        <div class="schedule-item-details">
          <img src="bus.jpg" class="schedule-photo" style="border:1px solid #c0c0c0;" />
        </div>
      </div>
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
                To book a room for Thursday and/or Friday night, please use <a href="https://www.holidayinn.com/redirect?path=hd&brandCode=HI&localeCode=en&regionCode=1&hotelCode=AUSTL&_PMID=99801505&GPC=THW&cn=no&viewfullsite=true">this link</a>, which will automatically fill in group code <b>THW</b>. You can also book your room over the phone by calling 1-888-615-0509; say you are a guest at the <b>Torres Hoza Wedding</b>.
              </li>
              <li>
                For other nights, please book your room by calling Lovinia at 512-634-1275. Say you are a guest at the <b>Torres Hoza Wedding</b>.
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
  
  page.compile("travel/index.html", mainContents, stylesheet="/schedule/index2.css", title="Travel")
