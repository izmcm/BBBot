import cv2
import numpy as np

def remove_lines(image):
    gray = cv2.bitwise_not(image)
    # Remove horizontal
    v_image = gray.copy()
    vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,2))
    v_image_eroded = cv2.erode(v_image, vertical_kernel)
    v_image_dilated = cv2.dilate(v_image_eroded, vertical_kernel)
    return v_image_dilated

def checkBlackCol(gray, col):
    for p in range(gray.shape[0]):
        if gray[p][col] > 50:
            return False
    return True

def checkBlackRow(gray, row):
    for p in range(gray.shape[1]):
        if gray[row][p] > 50:
            return False
    return True

def extract_basic_image(path):
    image = cv2.imread(path, 0)
    elements = remove_lines(image)
    return elements

def processImage(filename):
	img = cv2.imread('BBB20/captchas/' + filename, 0)

	imgBorder = cv2.copyMakeBorder(img, 8, 8, 8, 8, cv2.BORDER_REPLICATE)

	# ret, imgThreshold = cv2.threshold(imgBorder, 127, 255, cv2.THRESH_BINARY)
	
	# kernel = np.ones((1,2), np.uint8)
	# imgDilate = cv2.dilate(imgThreshold, kernel, iterations = 1)
	
	# cv2.imwrite('processedCaptchas/' + filename, imgDilate)
	cv2.imwrite('BBB20/processedCaptchas/' + filename, imgBorder)

def findInCaptcha(filename):
	processImage(filename)
	elementFile = 'BBB20/elementsCaptcha/' + filename
	captchaFile = 'BBB20/processedCaptchas/' + filename

	template = cv2.imread(elementFile,0)
	img = cv2.imread(captchaFile,0)
	# print(template)
	
	if template is None:
		cv2.imwrite('BBB20/elementsCaptcha/' + filename, img)

		return []
	else:
		# TODO: find out if we should just load the image from the dataset or not
		# remove the lines to make the detection easier
		template = extract_basic_image(elementFile)
		img = extract_basic_image(captchaFile)
		
		w, h = template.shape[::-1]

		res = cv2.matchTemplate(img,template,cv2.TM_SQDIFF_NORMED)
		
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
		top_left = min_loc

		bottom_right = (top_left[0] + w, top_left[1] + h)
		cv2.rectangle(img,top_left, bottom_right, 0, 2)

		# print("salvando")
		found = img[top_left[1]:top_left[1]+h, top_left[0]:top_left[0]+w]
		cv2.imwrite('BBB20/matchCaptcha/' + filename, found)

		return [top_left[0] + w/2, top_left[1] + h/2]


