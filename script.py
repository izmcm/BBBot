from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from binascii import a2b_base64
import processing

loginUrl = "https://minhaconta.globo.com/"
login = "email@provedor.com.br"
password = "senhadoemail"

url = "https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-felipe-manu-ou-mari-a9f49f90-84e2-4c12-a9af-b262e2dd5be4.ghtml"
nameSearch = "Felipe"

firefox = webdriver.Firefox()

firefox.get(loginUrl)
firefox.find_element_by_id('login').send_keys(login)
firefox.find_element_by_id('password').send_keys(password)
firefox.find_elements_by_css_selector('#login-form .button')[0].click()

firefox.get(url)

print("iniciando o bot")
while(1):
	try:
		title = firefox.find_elements_by_class_name('_1QJO-RxRXUUbq_pPU1oVZK')[0].text
		break
	except:
		pass

print(title)

titleParts = title.split('?')[1]

print(titleParts)

##### paredão triplo #####
namesAux = titleParts.split(', ')
names = [namesAux[0].strip()]
names = names + namesAux[1].split(' ou ')

##### paredão duplo #####
#namesAux = titleParts.split(' ou ')
#names = [namesAux[0].strip(), namesAux[1]]

idxName = names.index(nameSearch)

for _ in range(30):
	print(nameSearch + " é o botao " + str(idxName))

	element = []
	while(1):
		try:
			#print("procurando nome")
			element = firefox.find_elements_by_class_name('_1Y7EGDbQkmzYnNZcD4tztg')
			break
		except:
			pass

	elementBtn = element[idxName]
	
	ac = ActionChains(firefox)
	ac.move_to_element(elementBtn).click().perform()
	time.sleep(3)

	captchaBox = []
	while(1):
		try:
			# print("procurando o captcha")
			captchaBox = firefox.find_elements_by_class_name('gc__2Qtwp')
			if captchaBox != []:
				if len(captchaBox[0].text) > 5:
					break
		except:
			pass

	imageSearchName = captchaBox[0].text.split('\n')[-1]
	print("procurando por " + imageSearchName)

	captcha = []
	while(1):
		try:
			# print("procurando imagem")
			captcha = firefox.find_elements_by_class_name('gc__3_EfD')[0]
			break
		except:
			pass

	captchaSrc = captcha.get_attribute("src");

	data = captchaSrc.split(';base64,')[1]
	binary_data = a2b_base64(data)

	filename = imageSearchName + '.png'

	fd = open('BBB20/captchas/' + filename, 'wb')
	fd.write(binary_data)
	fd.close()

	processing.processImage(filename)
	points = processing.findInCaptcha(filename)

	if points != []:
		print("a imagem se encontra nos pontos: " + str(points[0]) + " X " + str(points[1]))
		print("o tamanho do captcha é " + str(captcha.size['width']) + " X " + str(captcha.size['height']))

		posX = points[0] - captcha.size['width']/2
		posY = points[1] - captcha.size['height']/2

		ac.move_to_element(captcha).move_by_offset(posX, posY).click().perform()
		time.sleep(10)
	else:
		print("erro - captcha não encontrado")
	
	firefox.refresh()
	time.sleep(3)

# firefox.quit()
