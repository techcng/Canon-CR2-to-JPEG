# author : Chandan Gupta

import rawpy
import imageio
import os

fullpath = "C:/Users/Chandan/Desktop/vinay chauhan/raw/one/" # write your path of folder
path = os.listdir("C:/Users/Chandan/Desktop/vinay chauhan/raw/one/")
for i in path:

    with rawpy.imread(fullpath+i) as raw:
        thumb = raw.extract_thumb()
    if thumb.format == rawpy.ThumbFormat.JPEG:
        # thumb.data is already in JPEG format, save as-is
        a = "IMG_" + str(i) + ".jpeg"
        with open(a, 'wb') as f:
            f.write(thumb.data)
        

    elif thumb.format == rawpy.ThumbFormat.BITMAP:
        # thumb.data is an RGB numpy array, convert with imageio
        b = "IMG_" + str(i) + ".jpeg"
        imageio.imsave(b, thumb.data)
        
    print("done")



