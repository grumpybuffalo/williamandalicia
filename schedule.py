# -*- coding: pyxl -*-
from pyxl import html

import page

def compile():
  mainContents = (
    <frag>
      <h2>
        SCHEDULE
      </h2>
      <div id="shuttle-info" style="padding:0 10px;">
        Shuttle service will be provided from the <u>ceremony to the reception</u> and from the <u>reception to the Holiday Inn Austin Town Lake</u>.
      </div>
      <div class="schedule-item">
        <div class="schedule-item-basics">
          <div class="schedule-item-name">
            Rehearsal
          </div>
          <div class="schedule-item-datetime">
            (Special invitation required)
          </div>
          <div class="schedule-item-datetime">
            Thursday, November 7, 2019
          </div>
          <div class="schedule-item-datetime">
            4pm
          </div>
          <div class="schedule-item-datetime">
            Casual attire
          </div>
        </div>
        <div class="schedule-item-details">
          <img src="ucc.jpg" class="schedule-photo" />
          <div class="schedule-item-location">
            University Catholic Center<br />
            2010 University Ave<br />
            Austin, TX 78705
          </div>
        </div>
      </div>
      <div class="schedule-item">
        <div class="schedule-item-basics">
          <div class="schedule-item-name">
            Rehearsal Dinner
          </div>
          <div class="schedule-item-datetime">
            (Special invitation required)
          </div>
          <div class="schedule-item-datetime">
            Thursday, November 7, 2019
          </div>
          <div class="schedule-item-datetime">
            6pm
          </div>
          <div class="schedule-item-datetime">
            Dressy casual attire
          </div>
        </div>
        <div class="schedule-item-details">
          <img src="capital-cruises.jpg" class="schedule-photo" />
          <div class="schedule-item-location">
            Capital Cruises<br />
            208 Barton Springs Rd<br />
            Austin, TX 78704
          </div>
        </div>
      </div>
      <div class="schedule-item">
        <div class="schedule-item-basics">
          <div class="schedule-item-name">
            Welcome Party
          </div>
          <div class="schedule-item-datetime">
            (All guests are invited)
          </div>
          <div class="schedule-item-datetime">
            Thursday, November 7, 2019
          </div>
          <div class="schedule-item-datetime">
            7:30pm
          </div>
          <div class="schedule-item-datetime">
            Dressy casual attire
          </div>
        </div>
        <div class="schedule-item-details">
          <img src="capital-cruises.jpg" class="schedule-photo" />
          <div class="schedule-item-location">
            Capital Cruises<br />
            208 Barton Springs Rd<br />
            Austin, TX 78704
          </div>
        </div>
      </div>
      <div class="schedule-item">
        <div class="schedule-item-basics">
          <div class="schedule-item-name">
            Nuptial Mass
          </div>
          <div class="schedule-item-datetime">
            (All guests are invited)
          </div>
          <div>
            Friday, November 8, 2019
          </div>
          <div class="schedule-item-datetime">
            3pm
          </div>
          <div class="schedule-item-datetime">
            Semiformal attire
          </div>
        </div>
        <div class="schedule-item-details">
          <img src="ucc.jpg" class="schedule-photo" />
          <div class="schedule-item-location">
            University Catholic Center<br />
            2010 University Ave<br />
            Austin, TX 78705
          </div>
        </div>
      </div>
      <div class="schedule-item">
        <div class="schedule-item-basics">
          <div class="schedule-item-name">
            Reception
          </div>
          <div class="schedule-item-datetime">
            (All guests are invited)
          </div>
          <div class="schedule-item-datetime">
            Friday, November 8, 2019
          </div>
          <div class="schedule-item-datetime">
            6pm - 10pm
          </div>
          <div class="schedule-item-datetime">
            Semiformal attire
          </div>
        </div>
        <div class="schedule-item-details">
          <img src="abels.jpg" class="schedule-photo" />
          <div class="schedule-item-location">
            Abel's on the Lake<br />
            3825 Lake Austin Blvd<br />
            Austin, TX 78703
          </div>
        </div>
      </div>
    </frag>
  )
  
  page.compile("schedule/index.html", mainContents, stylesheet="/schedule/index2.css", title="Schedule")
