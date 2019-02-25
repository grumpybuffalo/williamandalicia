# -*- coding: pyxl -*-
from pyxl import html
from PIL import Image

class WAImg:
  def __init__(self, num):
    self.num = num
    self.srcImage = Image.open(str(self.num) + ".jpg")
  
  def generateFiles(self):
    self.sizeSet = set()
    (origW, origH) = self.srcImage.size
    w = int(origW)
    while w > 150:
      h = int(w * origH / origW)
      resizedImg = self.srcImage.resize((w, h), Image.BICUBIC)
      resizedImg.save(str(self.num) + "-" + str(w) + ".jpg")
      self.sizeSet.add(w)
      w = int(w / 1.4)
  
  def imgElement(self):
    srcset = ", ".join(["%i-%i.jpg %iw" % (self.num, w, w) for w in self.sizeSet])
    (w, h) = self.srcImage.size
    return <div>test</div>

def main():
  print("egg")

if __name__ == "__main__":
  main()
