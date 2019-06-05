# -*- coding: pyxl -*-
from pyxl import html

import page

def compile():
  mainContents = (
    <frag>
      <h2>
        WEDDING PARTY
      </h2>
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="paige-hardy.jpg" />
          <div class="party-name">
            PAIGE HARDY
          </div>
          <div class="party-title">
            MAID OF HONOR
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="nicholas.jpg" />
          <div class="party-name">
            NICHOLAS HOZA
          </div>
          <div class="party-title">
            BEST MAN
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="paige-kubenka.jpg" />
          <div class="party-name">
            PAIGE KUBENKA
          </div>
          <div class="party-title">
            BRIDESMAID
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="jimmy.jpg" />
          <div class="party-name">
            JIMMY "HEINRICH" HOZA
          </div>
          <div class="party-title">
            GROOMSMAN
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="emily-hoza.jpg" />
          <div class="party-name">
            EMILY HOZA
          </div>
          <div class="party-title">
            BRIDESMAID
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="matt.jpg" />
          <div class="party-name">
            MATT MORGAN
          </div>
          <div class="party-title">
            GROOMSMAN
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="cassie.jpg" />
          <div class="party-name">
            CASSIE GUARDIOLA
          </div>
          <div class="party-title">
            BRIDESMAID
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="simon.jpg" />
          <div class="party-name">
            SIMON LUU
          </div>
          <div class="party-title">
            GROOMSMAN
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="jenna.jpg" />
          <div class="party-name">
            JENNA SALAZAR
          </div>
          <div class="party-title">
            BRIDESMAID
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="gehn.jpg" />
          <div class="party-name">
            GEHN FERGUSON
          </div>
          <div class="party-title">
            GROOMSMAN
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="maura.jpg" />
          <div class="party-name">
            MAURA TORRES
          </div>
          <div class="party-title">
            MOTHER OF THE BRIDE
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="roseanne.jpg" />
          <div class="party-name">
            ROSEANNE HOZA
          </div>
          <div class="party-title">
            MOTHER OF THE GROOM
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="alfred.jpg" />
          <div class="party-name">
            ALFRED TORRES
          </div>
          <div class="party-title">
            FATHER OF THE BRIDE
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="bradley.jpg" />
          <div class="party-name">
            BRADLEY HOZA
          </div>
          <div class="party-title">
            FATHER OF THE GROOM
          </div>
        </div>
      </div>
      
      <div class="party-pair">
        <div class="party-member">
          <img class="party-photo" src="emily-torres.jpg" />
          <div class="party-name">
            EMILY TORRES
          </div>
          <div class="party-title">
            FLOWER GIRL
          </div>
        </div>
        <div class="party-member">
          <img class="party-photo" src="katrina.jpg" />
          <div class="party-name">
            KATRINA HOZA
          </div>
          <div class="party-title">
            FLOWER GIRL
          </div>
        </div>
      </div>
      
      <div class="party-singleton">
        <div class="party-member">
          <img class="party-photo" src="carson.jpg" />
          <div class="party-name">
            CARSON HOZA
          </div>
          <div class="party-title">
            RING BEARER
          </div>
        </div>
      </div>
    </frag>
  )
  
  page.compile("wedding-party/index.html", mainContents, stylesheet="/wedding-party/index.css", title="Wedding Party")
