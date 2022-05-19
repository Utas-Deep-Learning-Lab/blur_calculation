import os.path
import glob
import cv2


def convertjpg(jpgfile, outdir, width=128, height=128):
    src = cv2.imread(jpgfile, cv2.IMREAD_ANYCOLOR)

    try:
        dst = cv2.blur(src,(50,50))
        cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), dst)
    except Exception as e:
        print(e)


for jpgfile in glob.glob(r'C:\Research_data\new\*.jpg'):
    convertjpg(jpgfile, r'C:\Research_data\new')