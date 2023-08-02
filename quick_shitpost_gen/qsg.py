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
        self.img_src = cv2.cvtColor(self.img_src, cv2.COLOR_BGR2HSV)
        greenMask = cv2.inRange(self.img_src, (128, 110, 30), (97, 100, 255))
        self.img_src[:,:,1] = greenMask
        self.img_src = cv2.cvtColor(self.img_src, cv2.COLOR_HSV2BGR)
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
