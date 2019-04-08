from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from binascii import a2b_base64
import processing

url = "https://gshow.globo.com/realities/bbb/bbb19/votacao/paredao-bbb-quem-voce-quer-eliminar-paula-ou-rizia-167d895c-799d-438d-801e-ec09005cd149.ghtml"
nameSearch = "Paula"

firefox = webdriver.Firefox()
firefox.get(url)

singin = firefox.find_elements_by_class_name('barra-botao-entrar')[0].click()

time.sleep(15) # fazer credenciamento

# bbbotvot@gmail.com
# botvot123

print("iniciando o bot")
for _ in range(10):
	while(1):
		try:
			title = firefox.find_elements_by_class_name('glb-poll-question')[0].text
			break
		except:
			pass

	print(title)

	titleParts = title.split('?')[1]

	print(titleParts)

	# paredão triplo
	# namesAux = titleParts.split(', ')
	# names = [namesAux[0].strip()]
	# names = names + namesAux[1].split(' ou ')
	
	# paredão duplo
	namesAux = titleParts.split(' ou ')
	names = [namesAux[0].strip(), namesAux[1]]

	idxName = names.index(nameSearch)

	print(nameSearch + " é o " + str(idxName) + " botao")

	element = []
	while(1):
		try:
			#print("procurando nome")
			element = firefox.find_elements_by_class_name('glb-poll-option-item')
			break
		except:
			pass

	elementBtn = element[idxName]
	ac = ActionChains(firefox)
	ac.move_to_element(elementBtn).move_by_offset(50, 50).click().perform()
	time.sleep(3)

	captchaBox = []
	while(1):
		try:
			#print("procurando o captcha")
			captchaBox = firefox.find_elements_by_class_name('glb-captcha-informations')
			if captchaBox != []:
				if len(captchaBox[0].text) > 20:
					break
		except:
			pass

	print(captchaBox)
	print(captchaBox[0].text)
	imageSearchNameList = (captchaBox[0].text).split(' ')
	print(imageSearchNameList)

	imageSearchName = imageSearchNameList[-1]
	print("procurando por " + imageSearchName)

	captcha = []
	while(1):
		try:
			#print("procurando imagem")
			captcha = firefox.find_element_by_id("glb-challenge-image")
			break
		except:
			pass

	captchaSrc = captcha.get_attribute("src");

	data = captchaSrc.split(';base64,')[1]
	binary_data = a2b_base64(data)

	filename = imageSearchName + '.png'

	fd = open('captchas/' + filename, 'wb')
	fd.write(binary_data)
	fd.close()

	processing.processImage(filename)
	
	points = processing.findInCaptcha(filename)
	if points != []:
		print("return: " + str(points[0]) + " " + str(points[1]))
		print("o tamanho do captcha é " + str(captcha.size['width']) + " X " + str(captcha.size['height']))

		posX = points[0] - captcha.size['width']/2
		posY = points[1] - captcha.size['height']/2

		ac.move_to_element(captcha).move_by_offset(posX, posY).click().perform()
		time.sleep(3)
	else:
		print("erro")
	
	firefox.refresh()
	time.sleep(3)

# firefox.quit()
