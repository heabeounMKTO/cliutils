import cv2 
import os 
from pathlib import Path


class shitpost():
    def __init__(self, title: str, img_src: str):
        self.title = title
        self.img_src = cv2.imread(img_src)

    def top_text(self, top_text):
        self.top_text = top_text

    def bottom_text(self, bottom_text):
        self.bottom_text = bottom_text

    def deep_fry(self):
       pass
    
    def calculate_textPos(self):
        print(self.img_src.shape)
