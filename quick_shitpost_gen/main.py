import argparse
from qsg import shitpost

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-t", "--title", required=True, help="title of your shitpost")
ap.add_argument("-c", "--caption", action='store_true' ,required=False, help="caption (add)")
ap.add_argument("-tt", "--toptext", required=False, help="top text")
ap.add_argument("-bt", "--bottomtext", required=False, help="bottom text")
ap.add_argument("-df", "--deepfry",action='store_true', help="deep fries your image")
args = vars(ap.parse_args())
sp = shitpost(args["title"], args["image"])
if args["deepfry"]:
    sp.deep_fry()
if args["caption"]:
    sp.top_text(args["toptext"])
    sp.bottom_text(args["bottomtext"])
    sp.write_caption()
    
