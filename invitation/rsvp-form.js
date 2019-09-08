const BASE_URL = "https://script.google.com/macros/s/AKfycbyA-EGH_wkttiVfrISk2CxIXZs5vs0QoHG0parEPg/exec"
const REPEAT_CHECKING_URL = "https://spreadsheets.google.com/feeds/cells/1D0OZG8QoXgn7O1MeKQP55cl9pIxNMHiBsGIcInyc53s/2/public/values?alt=json"
let partyID = "";
let guests = [];
let totalGuestsAllowed = 0;
let IDsOfReceivedRSVPs = null;

let weddingEvents = [
  new WeddingEvent("rehearsal", "Rehearsal", "Thursday at 4pm"),
  new WeddingEvent("rehearsalDinner", "Rehearsal Dinner", "Thursday at 6pm"),
  new WeddingEvent("welcomeParty", "Welcome Party", "Thursday at 7:30pm"),
  new WeddingEvent("ceremony", "Ceremony", "Friday at 3pm"),
  new WeddingEvent("reception", "Reception", "Friday at 6pm")
];

function WeddingEvent(id, name, timeText) {
  this.id = id;
  this.name = name;
  this.timeText = timeText;
  this.invited = true;
  this.responseContainer = document.createElement("div");
  this.responsePrompt = document.createElement("div");
  this.responsePrompt.innerHTML = "Who will attend the <strong>" + this.name.toLowerCase() + "</strong>? (" + this.timeText + ")";
  this.responseContainer.appendChild(this.responsePrompt);
  document.querySelector("#weddingEventContainer").appendChild(this.responseContainer);
  this.responseList = document.createElement("div");
  this.responseContainer.appendChild(this.responseList);
}
WeddingEvent.prototype.setInvited = function(invited) {
  this.invited = invited;
  this.responseContainer.style.display = this.invited ? "block" : "none";
}
WeddingEvent.prototype.generateResponseElements = function() {
  this.responsePrompt.style.display = guests.length > 1 ? "block" : "none";
  
  this.responseList.innerHTML = "";
  for (let i = 0; i < guests.length; i++) {
    let newResponseElement = document.createElement("div");
    newResponseElement.classList.add("response-element");

    let newCheckbox = document.createElement("input");
    newCheckbox.type = "checkbox";
    newCheckbox.id = this.id + "-" + i;
    newCheckbox.checked = guests[i].attending[this.id];
    let eventID = this.id;
    newCheckbox.onclick = function() {
      guests[i].attending[eventID] = newCheckbox.checked;
      guests[i].generateRecap();
    }
    
    let newLabel = document.createElement("label");
    newLabel.htmlFor = newCheckbox.id;
    labelText = guests.length > 1 ? guests[i].name : this.name + " (" + this.timeText + ")";
    newLabel.appendChild(document.createTextNode(labelText));
    
    newResponseElement.appendChild(newCheckbox);
    newResponseElement.appendChild(newLabel);
    this.responseList.appendChild(newResponseElement);
  }
}
WeddingEvent.prototype.attendeesString = function() {
  return guests.filter(guest => guest.attending[this.id]).map(guest => guest.name).join(", ");
}

function WeddingGuest(name, extra) {
  this.name = name;
  this.extra = extra;
  this.attending = {};
  for (let i = 0; i < weddingEvents.length; i++) {
    this.attending[weddingEvents[i].id] = false;
  }
  this.recapLI = document.createElement("li");
  document.querySelector("#recapUL").appendChild(this.recapLI);
  this.generateRecap();
}
WeddingGuest.prototype.generateRecap = function() {
  this.recapLI.innerHTML = "";
  this.recapLI.appendChild(document.createTextNode(this.name));
  eventsAttending = weddingEvents.filter(ev => this.attending[ev.id]);
  if (eventsAttending.length == 0) {
    this.recapLI.appendChild(document.createTextNode(" will not attend any events"));
  } else {
    let s = " will attend the ";
    for (i = 0; i < eventsAttending.length; i++) {
      s += eventsAttending[i].name.toLowerCase();
      if (i < eventsAttending.length - 1) {
        if (eventsAttending.length > 2) {
          s += ", ";
        }
        if (i == eventsAttending.length - 2) {
          s += " and ";
        }
      }
    }
    this.recapLI.appendChild(document.createTextNode(s));
  }
}

function submitRSVP() {
  if (document.querySelector("#rsvpForm").reportValidity()) {
    let url = BASE_URL + "?partyID=" + encodeURIComponent(partyID);
    
    let namedGuestsString = guests.filter(guest => !guest.extra).map(guest => guest.name).join(", ");
    let extrasString = guests.filter(guest => guest.extra).map(guest => guest.name).join(", ");
    url += "&namedGuests=" + encodeURIComponent(namedGuestsString) + "&extras=" + encodeURIComponent(extrasString);
    
    for (let i = 0; i < weddingEvents.length; i++) {
      url += "&" + weddingEvents[i].id + "Attendees=" + encodeURIComponent(weddingEvents[i].attendeesString());
    }
    
    additionalFields = ["comments"];
    
    url += additionalFields.map(s => "&" + s + "=" + encodeURIComponent(document.querySelector("#" + s).value)).join("");
    
    document.querySelector("#mainGuestListContainer").style.display = "none";
    document.querySelector("#weddingEventContainer").style.display = "none";
    if (document.querySelector("#comments").value == "") {
      document.querySelector("#comments").style.display = "none";
    } else {
      document.querySelector("#comments").disabled = true;
    }
    document.querySelector("#rsvpFormSubmitButton").style.display = "none";
    document.querySelector("#loadingDiv").style.display = "block";
    document.querySelector("#loadingDiv").innerHTML = "Submitting..."
    
    fetch(url).then(function(response) {
      document.querySelector("#loadingDiv").style.display = "none";
      if (response.ok) {
        document.querySelector("#successDiv").style.display = "block";
      } else {
        document.querySelector("#failureDiv").style.display = "block";
        console.log(response);
      }
    }).catch(function(error) {
      document.querySelector("#loadingDiv").style.display = "none";
      document.querySelector("#failureDiv").style.display = "block";
      console.log(error);
    });
    
    rescale();
  }
}

function checkParty() {
  urlParams = new URLSearchParams(window.location.search);
  foundInvitation = false;
  if (urlParams.has("id")) {
    partyID = urlParams.get("id");
    if (partyID in invitations) {
      foundInvitation = true;
      document.querySelector("#message").style.display = "none";
      document.querySelector("#content").style.display = "block";
      document.querySelector("#canv").style.display = "block";
      
      weddingEvents[0].setInvited(invitations[partyID]["itr"]);
      weddingEvents[1].setInvited(invitations[partyID]["itrd"]);
      
      fillInvitedEventsList();
      
      loadReceivedRSVPData();
    }
  }
  
  if (!foundInvitation) {
    // Invalid/missing ID parameter. Not invited?
    document.querySelector("#message").innerHTML = "Error: Invalid / missing invitation ID.";
  }
}

function fillInvitedEventsList() {
  evs = weddingEvents.filter(ev => ev.invited && ev.id != "ceremony");
  let s = "";
  for (let i = 0; i < evs.length; i++) {
    s += evs[i].name.toLowerCase();
    if (i < evs.length - 1 ) {
      if (evs.length > 2) {
        s += ", ";
      }
      if (i == evs.length - 2) {
        s += " and ";
      }
    }
  }
  document.querySelector("#invitedEventList").appendChild(document.createTextNode(s));
}

function registerGuest(name, extra) {
  guests.push(new WeddingGuest(name, extra));
}

function loadReceivedRSVPData() {
  fetch(REPEAT_CHECKING_URL).then(response => response.json()).then(function(data) {
    rows = data["feed"]["entry"].filter(
      entry => entry["gs$cell"]["col"] == 1).filter(
      entry => entry["content"]["$t"] == partyID).map(
      entry => entry["gs$cell"]["row"]);
      
    document.querySelector("#loadingDiv").style.display = "none";
    
    if (rows.length == 0) {
      // No RSVP submitted yet
      loadInvitation();
    } else {
      document.querySelector("#oldRSVP").style.display = "block";
      guestDict = {};
      
      for (let i = 0; i < weddingEvents.length; i++) {
        let nameList = data["feed"]["entry"].filter(
          entry => entry["gs$cell"]["row"] == rows[0] && entry["gs$cell"]["col"] == i + 4)[0]["content"]["$t"];
        weddingEvents[i].attendeeNames = nameList == "" ? [] : nameList.split(", ");
        for (let j = 0; j < weddingEvents[i].attendeeNames.length; j++) {
          s = weddingEvents[i].attendeeNames[j]
          if (!(s in guestDict)) {
            // The "extra" flag is not filled in correctly, but that doesn't matter
            registerGuest(s, false);
            guestDict[s] = guests[guests.length - 1];
          }
          guestDict[s].attending[weddingEvents[i].id] = true;
        }
      }
      
      for (let i = 0; i < guests.length; i++) {
        guests[i].generateRecap();
      }
      
      document.querySelector("#oldRSVP").appendChild(document.querySelector("#recapUL"));
      
      if (data["feed"]["entry"].filter(
        entry => entry["gs$cell"]["row"] == rows[0] && entry["gs$cell"]["col"] == 9)[0]["content"]["$t"] == "TRUE") {
        
        document.querySelector("#oldRSVP").appendChild(document.createTextNode("A comment was included with the RSVP."));  
      }
    }
  });
}

function loadInvitation() {
  document.querySelector("#newRSVP").style.display = "block";
  
  totalGuestsAllowed = invitations[partyID]["ng"].length + invitations[partyID]["noea"];
  document.querySelector("#totalGuestsAllowed").innerHTML = totalGuestsAllowed;
  document.querySelector("#addGuestForm").style.display = invitations[partyID]["noea"] > 0 ? "block" : "none";
    
  guests = []
  
  for (let i = 0; i < invitations[partyID]["ng"].length; i++) {
    registerGuest(invitations[partyID]["ng"][i], false);
  }
  
  updateGuestLists();
}

function updateGuestLists() {
  document.querySelector("#mainGuestList").innerHTML = "";
  
  for (let i = 0; i < guests.length; i++) {
    newLI = document.createElement("li");
    newLI.appendChild(document.createTextNode(guests[i].name))
    if (guests[i].extra) {
      xButton = document.createElement("input")
      xButton.type = "button";
      xButton.value = "Remove";
      xButton.classList.add("x");
      xButton.onclick = function() {
        removeGuest(i);
      }
      newLI.appendChild(xButton);
    }
    document.querySelector("#mainGuestList").appendChild(newLI);
  }
  
  document.querySelector("#newGuestName").disabled = (guests.length >= totalGuestsAllowed);
  document.querySelector("#newGuestSubmit").disabled = (guests.length >= totalGuestsAllowed);
  
  document.querySelector("#eventPrompt").style.display = guests.length > 1 ? "none" : "block";
  
  for (let i = 0; i < weddingEvents.length; i++) {
    weddingEvents[i].generateResponseElements();
  }
  
  rescale();
}

function addExtraGuest() {
  newName = document.querySelector("#newGuestName").value.replace(/\,/g, ";");
  registerGuest(newName, true);
  updateGuestLists();
  document.querySelector("#newGuestName").value = "";
}

function removeGuest(i) {
  document.querySelector("#recapUL").removeChild(guests[i].recapLI);
  guests.splice(i, 1);
  updateGuestLists();
}

checkParty();
