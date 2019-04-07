# -*- coding: pyxl -*-
from pyxl import html

import page

def compile():
  mainContents = (
    <frag>
      <h2>
        SCHEDULE
      </h2>
      <div class="schedule-item">
        <div class="schedule-item-basics">
          <div class="schedule-item-name">
            Ceremony
          </div>
          <div class="schedule-item-datetime">
            Friday, November 8, 2019
          </div>
          <div class="schedule-item-datetime">
            (Time TBA)
          </div>
        </div>
        <div class="schedule-item-details">
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
            Friday, November 8, 2019
          </div>
          <div class="schedule-item-datetime">
            6pm - 10pm
          </div>
        </div>
        <div class="schedule-item-details">
          <div class="schedule-item-location">
            Abel's on the Lake<br />
            3825 Lake Austin Blvd<br />
            Austin, TX 78703
          </div>
        </div>
      </div>
    </frag>
  )
  
  page.compile("schedule/index.html", mainContents, stylesheet="/schedule/index.css", title="Schedule")
