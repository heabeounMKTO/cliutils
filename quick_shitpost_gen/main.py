import argparse
from qsg import shitpost

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-t", "--title", required=True, help="title of your shitpost")
ap.add_argument("-tt", "--toptext", required=False, help="top text")
ap.add_argument("-bt", "--bottomtext", required=False, help="bottom text")
ap.add_argument("-df", "--deep-fry", required=False, help="deep fries your image")
args = vars(ap.parse_args())

sp = shitpost(args["title"], args["image"])
sp.calculate_textPos()
