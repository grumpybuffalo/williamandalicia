# -*- coding: pyxl -*-
from pyxl import html

import page

def compile():
  mainContents = (
    <frag>
      <div id="guestbook-link-block">
        <a href="https://airtable.com/shrEtBIDK9uzzDPrp">
          Click here to sign the public guestbook
        </a>
      </div>
      <iframe src="https://airtable.com/embed/shrsjEuhDPybMgVwd?backgroundColor=gray"></iframe>
    </frag>
  )
  
  page.compile("guestbook/index.html", mainContents, stylesheet="/guestbook/index.css", title="Guestbook")
