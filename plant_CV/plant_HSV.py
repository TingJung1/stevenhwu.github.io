# Import Libraries 
from plantcv import plantcv as pcv
import matplotlib

class options:
    def __init__(self):
        self.image = "1.jpg"
        self.debug = "plot"
        self.writeimg = False
        self.result = "vis_tutorial_results.json"
        self.outdir = "." # Store the output to the current directory
        
# Get options
args = options()

# Set debug to the global parameter 
pcv.params.debug = args.debug

img, path, filename = pcv.readimage(filename=args.image)