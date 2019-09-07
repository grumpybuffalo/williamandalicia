# -*- coding: pyxl -*-
from pyxl import html

import page

def compile():
  mainContents = (
    <frag>
      <h2>
        PLACES OF INTEREST
      </h2>
      <iframe src="https://www.google.com/maps/d/embed?mid=1pUpNUiTR31d4H1y7oi_1gWX2teB_cm3f"></iframe>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="peter-pan-mini-golf.png" />
          <div class="party-name">
            PETER PAN MINI-GOLF
          </div>
          <div class="place-location">
            1207 Barton Springs Rd
          </div>
          <div class="place-description">
            We've been on a couple of dates here. Be aware: it's cash-only!
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="cherrywood.png" />
          <div class="party-name">
            CHERRYWOOD COFFEEHOUSE
          </div>
          <div class="place-location">
            1400 E 38th 1/2 St
          </div>
          <div class="place-description">
            Alicia's favorite restaurant! The manager knows us here and has our regular order memorized. Alicia gets the grilled shrimp taco plate, and William gets a gluten-free chicken and cheese sandwich.
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="wilder-wood.png" />
          <div class="party-name">
            WILDER WOOD
          </div>
          <div class="place-location">
            1300 E 7th St
          </div>
          <div class="place-description">
            Our go-to gluten-free restaurant. Their original location recently closed, but this new location has a beautiful view of downtown!
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="lbj-library.jpg" />
          <div class="party-name">
            LYNDON B. JOHNSON LIBRARY
          </div>
          <div class="place-location">
            2313 Red River St
          </div>
          <div class="place-description">
            Our first date spot! We got a parking-ticket, but it was worth it.
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="blue-cat-cafe.png" />
          <div class="party-name">
            BLUE CAT CAFÉ
          </div>
          <div class="place-location">
            95 Navasota St
          </div>
          <div class="place-description">
            A very Austin kind of place: Alicia once spent an entire day here hanging out with cats and snacking on cafe food.
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="boardwalk.jpg" />
          <div class="party-name">
            The Boardwalk at Lady Bird Lake
          </div>
          <div class="place-location">
            1820 S Lakeshore Blvd
          </div>
          <div class="place-description">
            Our proposal spot! Alicia has often called this the best place in the world.
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="lone-star-riverboat.png" />
          <div class="party-name">
            Lone Star Riverboat
          </div>
          <div class="place-location">
            208 Barton Springs Rd
          </div>
          <div class="place-description">
            We've had a few dates here, both on their river cruises and on rented kayaks and their unique swan boats!
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="hideout-theater.png" />
          <div class="party-name">
            The Hideout Theatre
          </div>
          <div class="place-location">
            617 Congress Ave
          </div>
          <div class="place-description">
            We've had a few dates here. They do fun and inexpensive improv shows!
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="torchys.png" />
          <div class="party-name">
            Torchy's Tacos
          </div>
          <div class="place-location">
            2801 Guadalupe St. 5-B
          </div>
          <div class="place-description">
            Really, really, good tacos.
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="home-slice.png" />
          <div class="party-name">
            Home Slice Pizza
          </div>
          <div class="place-location">
            1415 S Congress Ave
          </div>
          <div class="place-description">
            We're told this place has amazing pizza, but we've never eaten here because an employee described it to us as "a temple of gluten."
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="cream-whiskers.png" />
          <div class="party-name">
            Cream Whiskers
          </div>
          <div class="place-location">
            2222 Rio Grande St B120
          </div>
          <div class="place-description">
            A really cute place with unique cream puffs and board games.
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="chick-fil-a.png" />
          <div class="party-name">
            Chick-fil-A
          </div>
          <div class="place-location">
            503 W Martin Luther King Jr Blvd
          </div>
          <div class="place-description">
            William loves Chick-fil-A. We met here for lunch a couple of times a week throughout the summer of 2017 while Alicia worked at TxDOT nearby.
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="park.png" />
          <div class="party-name">
            Sir Swante Palm Neighborhood Park
          </div>
          <div class="place-location">
            200 N IH 35 Svrd SB
          </div>
          <div class="place-description">
            We've been here a few times specifically because it's one of the few parks in the area with swings! It also has fun toys that make you very dizzy.
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="tower.jpg" />
          <div class="party-name">
            UT Tower
          </div>
          <div class="place-location">
            110 Inner Campus Drive
          </div>
          <div class="place-description">
            If you want to see any part of the UT campus, the tower is the place to go.
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="menchies.png" />
          <div class="party-name">
            Menchie's Frozen Yogurt
          </div>
          <div class="place-location">
            1000 E 41st St #255
          </div>
          <div class="place-description">
            Alicia's and her sister Emily's favorite dessert! We go here every other week or so.
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="mural.jpg" />
          <div class="party-name" style="text-transform:none">
            "i love you so much" MURAL
          </div>
          <div class="place-location">
            1300 S Congress Ave
          </div>
          <div class="place-description">
            This is a pretty iconic Austin picture spot.
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="hopdoddy.png" />
          <div class="party-name">
            Hopdoddy Burger Bar
          </div>
          <div class="place-location">
            1400 S Congress Ave
          </div>
          <div class="place-description">
            Alicia's favorite burger place! We strongly recommend the parmesan fries.
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="san-jose.png" />
          <div class="party-name">
            San Jose Catholic Church
          </div>
          <div class="place-location">
            2435 Oak Crest Ave
          </div>
          <div class="place-description">
            This church has one of our favorite adoration chapels (and it's open 24 hours!)
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="bennu.png" />
          <div class="party-name">
            Bennu Coffee on Congress
          </div>
          <div class="place-location">
            515 S Congress Ave
          </div>
          <div class="place-description">
            This place makes really good literary-themed mochas. It's one of Alicia's favorite study spots.
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="quacks.png" />
          <div class="party-name">
            Quack's 43rd Street Bakery
          </div>
          <div class="place-location">
            411 E 43rd St
          </div>
          <div class="place-description">
            One of Alicia's favorite study spots. This place has adorable baked treats (including really good brownies) and ample parking.
          </div>
        </div>
      </div>
      
      <div class="party-singleton">
        <div class="party-member">
          <img class="party-photo" src="cafe-monet.png" />
          <div class="party-name">
            Cafe Monet Art Studio
          </div>
          <div class="place-location">
            4700 W Guadalupe St #11
          </div>
          <div class="place-description">
            We've had several dates at this paint-your-own-pottery spot.
          </div>
        </div>
      </div>
    </frag>
  )
  
  page.compile("places-of-interest/index.html", mainContents, stylesheet="/places-of-interest/index.css", title="Places of Interest")