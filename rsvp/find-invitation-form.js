function findInvitation() {
  firstName = document.querySelector("#firstName").value.toLowerCase();
  lastName = document.querySelector("#lastName").value.toLowerCase();
  fullName = firstName + " " + lastName;
  for (id in invitations) {
    for (let i = 0; i < invitations[id]["ng"].length; i++) {
      if (invitations[id]["ng"][i].toLowerCase() == fullName) {
        document.location.href = "/invitation/?id=" + encodeURIComponent(id);
        return;
      }
    }
  }
  
  // No exact matches. Let's search for partial matches
  document.querySelector("#partialMatchList").innerHTML = "";
  words = fullName.split(" ");
  let foundAnyPartialMatch = false;
  
  for (id in invitations) {
    let confirmedPartialMatch = false;
    for (let i = 0; i < invitations[id]["ng"].length; i++) {
      let guestMatched = false;
      invitationWords = invitations[id]["ng"][i].toLowerCase().split(" ");
      for (let j = 0; j < invitationWords.length; j++) {
        for (let k = 0; k < invitationWords.length; k++) {
          if (words[j] == invitationWords[k]) {
            guestMatched = true;
            foundAnyPartialMatch = true;
            newLI = document.createElement("li");
            newA = document.createElement("a");
            newA.appendChild(document.createTextNode(invitations[id]["ng"][i]));
            newA.href = "/invitation/?id=" + encodeURIComponent(id);
            newLI.appendChild(newA);
            document.querySelector("#partialMatchList").appendChild(newLI);
            break;
          }
        }
        if (guestMatched) break;
      }
    }
  }
  
  document.querySelector("#partialMatchDiv").style.display = foundAnyPartialMatch ? "block" : "none";
  document.querySelector("#notFoundMessage").style.display = foundAnyPartialMatch ? "none" : "block";
}
