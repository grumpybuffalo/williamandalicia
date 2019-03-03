let totalWidth;
let gallery;

const BASE_ROW_HEIGHT = 250;
const SPACING = 3;

function Gallery() {
  this.rowPairs = [];
}
Gallery.prototype.addLargeImage = function(img) {
  
}

function RowPair(largeImage) {
  this.largeImage = largeImage;
  this.rows = [new Row(), new Row()];
  this.curRow = 0;
  
  // For phase 1
  const largeImageWidth = largeImage == null ? 0 : parseFloat(largeImage.dataset.ar) * (2 * BASE_ROW_HEIGHT + SPACING);
  this.rowWidth = totalWidth - largeImageWidth;
}
RowPair.prototype.addSmallImage = function(img) {
  if (this.rows[this.curRow].images.length == 0 || this.rows[this.curRow].canFit(img, this.rowWidth)) {
    this.rows[this.curRow].add(img);
    return true;
  } else {
    if (this.curRow == 0) {
      this.curRow++;
      return this.addSmallImage(img);
    } else {
      return false;
    }
  }
}

// This function implements Phase II
RowPair.prototype.rebalance = function() {
  if (this.rows[1].images.length >= 1) {
    // We're going to change the two rows heights so that their widths come out equal,
    // maintaining height0 + height1 = 2 * BASE_ROW_HEIGHT
    let p0 = this.rows[0].widthParameters();
    let p1 = this.rows[1].widthParameters();
    
    let m0 = p0[0];
    let b0 = p0[1];
    let m1 = p1[0];
    let b1 = p1[1];
    
    let H = 2 * BASE_ROW_HEIGHT;
    
    // We want h0, h1 such that
    // m0 * h0 + b0 == m1 * h1 + b1    and   h0 + h1 == H
    //
    // m0 * h0 - m1 * (H - h0) == b1 - b0
    // (m0 + m1) * h0 == m1 * H + b1 - b0
    
    let h0 = (m1 * H + b1 - b0) / (m0 + m1);
    let h1 = H - h0;
    
    this.rows[0].height = h0;
    this.rows[1].height = h1;
  }
}

// This function implements Phase III
RowPair.prototype.rescale = function() {
  const p0 = this.rows[0].widthParameters();
    
  const m0 = p0[0];
  const b0 = p0[1];
  
  const ar = this.largeImage == null ? 0 : parseFloat(this.largeImage.dataset.ar);
  
  if (this.rows[1].images.length >= 1) {
    // We're going to scale the two row heights (together) so that the total width
    // of the row pair comes out to totalWidth
    
    // Let t be the scale factor, so we'll set h0 := h0 * t and h1 := h1 * t
    // Then the big image will have height 2 * BASE_ROW_HEIGHT * t + SPACING
    // So we want
    //
    // m0 * h0 * t + b0 + (2 * BASE_ROW_HEIGHT * t + SPACING) * ar == totalWidth
    //
    // (m0 * h0 + 2 * BASE_ROW_HEIGHT * ar) * t == totalWidth - b0 - SPACING * ar
    
    const t = (totalWidth - b0 - SPACING * ar) / (m0 * this.rows[0].height + 2 * BASE_ROW_HEIGHT * ar);
    
    this.rows[0].height *= t;
    this.rows[1].height *= t;
  } else {
    // Let h be the height of the one row
    // We want
    //
    // ar * h + m0 * h + b0 == totalWidth
    // (m0 + ar) * h == totalWidth - b0
    
    const h = (totalWidth - b0) / (m0 + ar);
    this.rows[0].height = h;
  }
}

RowPair.prototype.activate = function() {
  rowPairContainer = document.createElement("div");
  
  if (this.largeImage == null) {
    rowPairContainer.classList.add("no-large");
  } else {
    const largeImageHeight = this.rows[1].images.length >= 1 ? this.rows[0].height + this.rows[1].height + SPACING : this.rows[0].height;
    const ar = parseFloat(this.largeImage.dataset.ar);
    const largeImageWidth = ar * largeImageHeight;
    
    const galleryLargeImageA = document.createElement("a");
    galleryLargeImageA.classList.add("large");
    galleryLargeImageA.href = this.largeImage.dataset.src;
    galleryLargeImageA.style.width = largeImageWidth + "px";
    galleryLargeImageA.style.height = largeImageHeight + "px";
    
    const galleryLargeImage = document.createElement("img");
    galleryLargeImage.style.width = "100%";
    galleryLargeImage.style.height = "100%";
    galleryLargeImage.sizes = largeImageWidth + "px";
    galleryLargeImage.srcset = this.largeImage.dataset.srcset;
    
    galleryLargeImageA.appendChild(galleryLargeImage);
    rowPairContainer.appendChild(galleryLargeImageA);
  }
  
  for (let r = 0; r < 2; r++) {
    rowContainer = document.createElement("div");
    for (let i = 0; i < this.rows[r].images.length; i++) {
      const img = this.rows[r].images[i];
      const galleryImg = document.createElement("img");
      const galleryImgA = document.createElement("a");
      
      const width = parseFloat(img.dataset.ar) * (this.rows[r].height);
      
      galleryImgA.classList.add("small");
      galleryImgA.style.width = width + "px";
      galleryImgA.style.height = this.rows[r].height + "px";
      galleryImgA.href = img.dataset.src;
      
      galleryImg.sizes = width + "px";
      galleryImg.style.width = "100%";
      galleryImg.style.height = "100%";
      galleryImg.srcset = img.dataset.srcset;
      
      galleryImgA.appendChild(galleryImg);
      rowContainer.appendChild(galleryImgA);
    }
    rowPairContainer.appendChild(rowContainer);
  }
  
  gallery.appendChild(rowPairContainer);
}

function Row() {
  this.height = BASE_ROW_HEIGHT;
  this.images = [];
}
Row.prototype.widthParameters = function() { // Returns a pair [m, b] s.t. width = m * height + b
  let m = 0;
  for (let i = 0; i < this.images.length; i++) {
    m += parseFloat(this.images[i].dataset.ar);
  }
  
  const b = this.largeImage == null ? SPACING * (this.images.length - 1) : SPACING * this.images.length;
  
  return [m, b];
}
Row.prototype.canFit = function(img, maxWidth) {
  const p = this.widthParameters();
  const totalNewWidth = p[0] * this.height + p[1] + SPACING + parseFloat(img.dataset.ar) * this.height;
  return totalNewWidth <= maxWidth;
}
Row.prototype.add = function(img) {
  this.images.push(img);
}

function layout() {
  const images = document.querySelector("#image-data").childNodes;
  gallery = clearContents("#gallery");
  totalWidth = Math.min(2000, document.body.clientWidth);
  
  if (totalWidth < 1000) {
    // Justified grid
    let li = 0;
    let ri = images.length - 1;
    
    while (ri > li) {
      let rowPair = new RowPair(null);
      let cont = true;
      let i = 0;
      while (cont && ri > li) {
        if (i % 3 == 0) {
          cont = rowPair.addSmallImage(images[li]);
          if (cont) li++;
        } else {
          cont = rowPair.addSmallImage(images[ri]);
          if (cont) ri--;
        }
        i++;
      }
      rowPair.rebalance();
      rowPair.rescale();
      rowPair.activate();
    }
  } else {
    // Justified grid with big images
    let li = 0;
    let ri = images.length - 1;
    
    while (ri > li) {
      let rowPair = new RowPair(images[li]);
      let cont = true;
      while (cont && ri > li) {
        cont = rowPair.addSmallImage(images[ri]);
        if (cont) ri--;
      }
      rowPair.rebalance();
      rowPair.rescale();
      rowPair.activate();
      li++;
    }
  }
}

function clearContents(s) {
  const o = document.querySelector(s);
  const n = o.cloneNode(false);
  o.parentNode.replaceChild(n, o);
  return n;
}

window.addEventListener("resize", function() {
  if (Math.min(2000, document.body.clientWidth) != totalWidth) {
    layout();
  }
});
layout();
