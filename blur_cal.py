import cv2
import numpy as np


src = cv2.imread('9_58.773541.png')
img2gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
imageVar = cv2.Laplacian(img2gray, cv2.CV_64F).var()
print(imageVar)
text = 'The fuzzy is: {:.2f}'.format(imageVar)
AddText = src.copy()
img = cv2.putText(AddText, text, (40, 400), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 5, cv2.LINE_AA, False)

# 将原图片和添加文字后的图片拼接起来
res = np.hstack([src, AddText])

filename = 'savedImage4.jpg'

# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, img)

# 显示拼接后的图片
# cv2.imshow('text', res)
cv2.waitKey()
cv2.destroyAllWindows()