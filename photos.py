# -*- coding: pyxl -*-
from pyxl import html
from PIL import Image
from tqdm import tqdm
import os

import page

class WAImg:
  def __init__(self, num):
    self.num = num
    self.srcImage = Image.open("photos/%i.jpg" % self.num)
    self.sizes = set()
    
  def generateFiles(self):
    (origW, origH) = self.srcImage.size
    w = origW
    while w > 300:
      self.sizes.add(w)
      if not os.path.isfile("photos/%i-%i.jpg" % (self.num, w)):
        h = int(origH * w / origW)
        resizedImage = self.srcImage.resize((w, h), Image.BICUBIC)
        resizedImage.save("photos/%i-%i.jpg" % (self.num, w))
      w = int(w / 1.4)
      
  def imgElement(self):
    (origW, origH) = self.srcImage.size
    srcset = ", ".join(["/photos/%i-%i.jpg %iw" % (self.num, w, w) for w in self.sizes])
    src = "/photos/%i.jpg" % self.num
    return <img data-srcset="{srcset}" data-ar="{origW / origH}" data-src="{src}" />

def compile():
  # Intentionally omitted: 31, 33, 3, 50, 72
  nums = [13, 83, 103, 64, 91, 56, 21, 100, 95, 85, 45, 104, 8, 77, 92, 61, 88, 57, 84, 71, 51, 73, 26, 12, 68, 1, 99, 70, 9, 35, 80, 96, 38, 62, 36, 5, 59, 78, 60, 82, 52, 53, 40, 2, 97, 7, 41, 49, 43, 106, 44, 46, 6, 48, 81, 69, 47, 90, 37, 107, 39, 34, 86, 67, 55, 32, 108, 75, 30, 29, 76, 20, 87, 28, 66, 27, 25, 79, 23, 24, 109, 22, 58, 19, 65, 74, 94, 105, 11, 93, 54, 17, 98, 63, 16, 110, 15, 102, 14, 101, 18, 89, 10, 42, 4]
  WAImages = [WAImg(n) for n in nums]
  imgElements = <frag></frag>
  
  for img in tqdm(WAImages, desc="Images"):
    img.generateFiles()
    imgElements.append(img.imgElement())
  
  mainContents = (
    <frag>
      <h2>
        PHOTOS
      </h2>
      <div id="image-data">
        {imgElements}
      </div>
      <div id="gallery">
      </div>
    </frag>
  )
  
  page.compile("photos/index.html", mainContents, title="Photos", stylesheet="/photos/index.css", scripts=["/photos/index.js"])
