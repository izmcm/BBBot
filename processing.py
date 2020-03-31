import cv2
import numpy as np

def processImage(filename):
	img = cv2.imread('BBB20/captchas/' + filename, 0)

	imgBorder = cv2.copyMakeBorder(img, 8, 8, 8, 8, cv2.BORDER_REPLICATE)

	# ret, imgThreshold = cv2.threshold(imgBorder, 127, 255, cv2.THRESH_BINARY)
	
	# kernel = np.ones((1,2), np.uint8)
	# imgDilate = cv2.dilate(imgThreshold, kernel, iterations = 1)
	
	# cv2.imwrite('processedCaptchas/' + filename, imgDilate)
	cv2.imwrite('BBB20/processedCaptchas/' + filename, imgBorder)


def findInCaptcha(filename):
	elementFile = 'BBB20/elementsCaptcha/' + filename
	captchaFile = 'BBB20/processedCaptchas/' + filename

	template = cv2.imread(elementFile,0)
	
	img = cv2.imread(captchaFile,0)
	# print(template)
	
	if template is None:
		cv2.imwrite('BBB20/elementsCaptcha/' + filename, img)

		return []
	else:
		w, h = template.shape[::-1]

		res = cv2.matchTemplate(img,template,cv2.TM_SQDIFF_NORMED)
		
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
		top_left = min_loc

		bottom_right = (top_left[0] + w, top_left[1] + h)
		cv2.rectangle(img,top_left, bottom_right, 0, 2)

		print("salvando")
		cv2.imwrite('BBB20/matchCaptcha/' + filename, img)

		return [top_left[0] + w/2, top_left[1] + h/2]


