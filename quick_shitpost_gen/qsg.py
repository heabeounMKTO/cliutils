import cv2 
import os 
from pathlib import Path
import numpy as np

class shitpost():
    def __init__(self, title: str, img_src: str):
        self.title = title
        self.img_src = cv2.imread(img_src)

    def top_text(self, top_text):
        self.top_text = top_text

    def bottom_text(self, bottom_text):
        self.bottom_text = bottom_text

    def deep_fry(self):
        clipLimit = 20
        tileGridSize = (8,8)
        self.img_src = cv2.cvtColor(self.img_src, cv2.COLOR_BGR2HSV)
        lab = cv2.cvtColor(self.img_src, cv2.COLOR_BGR2LAB)
        lChan,aChan,bChan = cv2.split(lab)            #split channels
        clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize) #create CLAHE or Contrast Limited Auto Histogram Equalization object 
        cl=clahe.apply(lChan) #apply CLAHE
        limg = cv2.merge((cl,aChan,bChan))   #merge channgles back
        self.img_src = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)   #convert back to BGR for opencv
        self.write_shitpost2file()

    def compute_textPos(self):
        print(self.img_src.shape)

    def write_caption(self):
        ty, tx = int(self.img_src.shape[0]/8), int(self.img_src.shape[1]/2)
        colorwhite = (255,255,255)
        colorblack = (0,0,0)
        #top text
        self.imgsrc = cv2.putText(self.img_src,f'{self.top_text}', 
                    (tx,ty), cv2.FONT_HERSHEY_SIMPLEX, 2.0,
                    colorblack,
                    15)
        #bottom text
        self.imgsrc = cv2.putText(self.img_src,f'{self.bottom_text}', 
                    (tx,ty*7), cv2.FONT_HERSHEY_SIMPLEX, 2.0,
                    colorblack,
                    15)

        #top text
        self.imgsrc = cv2.putText(self.img_src,f'{self.top_text}', 
                    (tx,ty), cv2.FONT_HERSHEY_SIMPLEX, 2.0,
                    colorwhite,
                    8)
        #bottom text
        self.imgsrc = cv2.putText(self.img_src,f'{self.bottom_text}', 
                    (tx,ty*7), cv2.FONT_HERSHEY_SIMPLEX, 2.0,
                    colorwhite,
                    8)
        cv2.imwrite(f"output/{self.title}.png", self.img_src)

    def write_shitpost2file(self):
        cv2.imwrite(f"output/{self.title}.png", self.img_src) 
