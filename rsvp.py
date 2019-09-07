# -*- coding: pyxl -*-
from pyxl import html

import csv
import hashlib
import json

import page

def compile():
  # Generate JS file with invitation data from CSV file
  invitations = {}
  
  with open("invitation-data.csv") as csvfile:
    reader = csv.reader(csvfile)
    first = True
    for row in reader:
      if first:
        first = False
      else:
        id = hashlib.sha1(row[0].encode()).hexdigest()[:8]
        invitations[id] = {}
        
        invitations[id]["ng"] = row[0].split(", ") # Named guests
        assert row[1] in {"Y", "N"}, "Invalid row %s" % str(row)
        invitations[id]["itr"] = (row[1] == "Y") # Invited to rehearsal
        assert row[2] in {"Y", "N"}, "Invalid row %s" % str(row)
        invitations[id]["itrd"] = (row[2] == "Y") # Invited to rehearsal dinner
        invitations[id]["noea"] = int(row[3]) # Number of extras allowed
        
  with open("assets/invitation-data.js", "w") as jsfile:
    jsfile.write("const invitations = " + json.dumps(invitations) + ";")
  
  mainContents = (
    <div id="outerRSVPContainer">
      <div id="rsvpMessage">
        RSVP at the bottom of your electronic invitation. Did you lose your invitation link? Find it again by entering your name here.
      </div>
      <form onsubmit="event.preventDefault(); findInvitation();" id="findPartyForm">
        <input type="text" id="firstName" placeholder="First name" />
        <input type="text" id="lastName" placeholder="Last name" />
        <input type="submit" value="Find invitation" />
      </form>
      <div id="partialMatchDiv">
        Hmm. We couldn't find an invitation under that <em>exact</em> name. Click on your name if you see it below.
        <ul id="partialMatchList">
        </ul>
        Otherwise, is there any chance we have a different name for you?
      </div>
      <div id="notFoundMessage">
        Hmm. We couldn't find an invitation under that name. Is there any chance we have a different name for you?
      </div>
    </div>
  )
  
  page.compile("rsvp/index.html", mainContents, stylesheet="/rsvp/index.css", scripts=["/assets/invitation-data.js", "/rsvp/find-invitation-form.js"], title="RSVP")
