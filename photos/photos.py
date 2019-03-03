# -*- coding: pyxl -*-
from pyxl import html
from PIL import Image
from tqdm import tqdm
import os

class WAImg:
  def __init__(self, num):
    self.num = num
    self.srcImage = Image.open(str(self.num) + ".jpg")
    self.sizes = set()
    
  def generateFiles(self):
    (origW, origH) = self.srcImage.size
    w = origW
    while w > 300:
      self.sizes.add(w)
      if not os.path.isfile("%i-%i.jpg"):
        h = int(origH * w / origW)
        resizedImage = self.srcImage.resize((w, h), Image.BICUBIC)
        resizedImage.save("%i-%i.jpg" % (self.num, w))
      w = int(w / 1.4)
      
  def imgElement(self):
    (origW, origH) = self.srcImage.size
    srcset = ", ".join(["%i-%i.jpg %iw" % (self.num, w, w) for w in self.sizes])
    return <img data-srcset="{srcset}" data-ar="{origW / origH}" />

def main():
  # TODO: Hand pick these lists
  small = list(range(1, 65))
  large = list(range(65, 76))
  
  smallWAImages = [WAImg(n) for n in small]
  largeWAImages = [WAImg(n) for n in large]
  
  smallImgElements = <frag></frag>
  largeImgElements = <frag></frag>
  
  for img in tqdm(smallWAImages, desc="Compiling small images"):
    img.generateFiles()
    smallImgElements.append(img.imgElement())
    
  for img in largeWAImages:
    img.generateFiles()
    largeImgElements.append(img.imgElement())
    
  gaScript1 = <script src="https://www.googletagmanager.com/gtag/js?id=UA-123337994-2"></script>
  gaScript2 = <script>{html.rawhtml("""window.dataLayer = window.dataLayer || []; function gtag(){dataLayer.push(arguments);} gtag('js', new Date()); gtag('config', 'UA-123337994-2');""")}</script>
  
  gaScript1.set_attr("async", "") # async is a Python keyword, so we have to set this attribute manually  
  
  doc = (
    <html lang="en">
      <head>
        <meta charset="utf-8" />
        {gaScript1}
        {gaScript2}
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>
          Photos | Alicia Torres and William Hoza's Wedding Website
        </title>
        <link href="https://fonts.googleapis.com/css?family=PT+Sans" rel="stylesheet" />
        <link rel="stylesheet" href="/assets/index.css" />
        <link rel="stylesheet" href="index.css" />
      </head>
      <body>
        <div id="flow">
          <header>
            <div id="header-event-basics">
              <time datetime="2019-11-09" style="margin-right:20px;">November 9, 2019</time>
              Austin, TX
              <span style="float:right;">
                &num;cavemanandwife
              </span>
            </div>
            <div id="h1-line">
              <h1>
                ALICIA &amp; WILLIAM
              </h1>
              <button id="nav-show-button" onclick="showNav();">Menu</button>
            </div>
            <nav>
              <div><button id="nav-hide-button" onclick="hideNav();">Hide</button></div>
              <div><a href="/">HOME</a></div>
              <div><a href="/wedding-party/">WEDDING PARTY</a></div>
            </nav>
          </header>
          <main>
            <h2>
              PHOTOS
            </h2>
            <div id="small-images">
              {smallImgElements}
            </div>
            <div id="large-images">
              {largeImgElements}
            </div>
          </main>
        </div>
        
        <script src="index.js"></script>
        <script src="/assets/index.js"></script>
      </body>
    </html>
  )
  
  file = open("index.html", "w")
  file.write("<!DOCTYPE html>" + str(doc))

if __name__ == "__main__":
  main()
