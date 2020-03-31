from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from binascii import a2b_base64
import processing

login = ""
password = ""
login = input("digite seu email:")
password = input("digite sua senha:")

loginUrl = "https://minhaconta.globo.com/"
# login = "bbbotvot@gmail.com"
# password = "botvot123"

url = "https://gshow.globo.com/realities/bbb/bbb20/votacao/paredao-bbb20-quem-voce-quer-eliminar-felipe-manu-ou-mari-a9f49f90-84e2-4c12-a9af-b262e2dd5be4.ghtml"
nameSearch = "Felipe"

browser = None
try:
	caps = DesiredCapabilities().CHROME
	caps["pageLoadStrategy"] = "eager"  #  interactive
	browser = webdriver.Chrome(capabilities=caps)
	# browser = webdriver.Chrome()
except:
	caps = DesiredCapabilities().FIREFOX
	caps["pageLoadStrategy"] = "eager"  #  interactive
	browser = webdriver.Firefox(capabilities=caps)
	# browser = webdriver.Firefox()
browser.get(loginUrl)

time.sleep(10)
print("starting login")
browser.find_element_by_id('login').send_keys(login)
browser.find_element_by_id('password').send_keys(password)
browser.find_elements_by_css_selector('#login-form .button')[0].click()

print("finished login")

time.sleep(5)
browser.get(url)

print("iniciando o bot")
while(1):
	try:
		# title = browser.find_elements_by_class_name('_1QJO-RxRXUUbq_pPU1oVZK')[0].text
		# title = browser.find_element_by_xpath('//*[@id="roulette-root"]/div/div[1]/div[3]/div/div/div')
		title = browser.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div[3]/div/div/div').text
		
		break
	except:
		pass

print(title)

time.sleep(5)

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
			# element = browser.find_elements_by_class_name('_1Y7EGDbQkmzYnNZcD4tztg')
			element = [
				browser.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div[4]/div[1]'),
				browser.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div[4]/div[2]'),
				browser.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div[4]/div[3]'),
			]
			break
		except:
			pass

	print(idxName)
	print(element)
	elementBtn = element[idxName]

	print('elementBtn:', elementBtn)
	
	ac = ActionChains(browser)
	ac.move_to_element(elementBtn).perform()
	ac.click().perform()
	time.sleep(3)

	captchaBox = []
	while(1):
		try:
			# print("procurando o captcha")
			captchaBox = browser.find_elements_by_class_name('gc__2Qtwp')
			if captchaBox != []:
				if len(captchaBox[0].text) > 2:
					break
		except:
			pass

	imageSearchName = captchaBox[0].text.split('\n')[-1]
	print("procurando por " + imageSearchName)

	captcha = []
	while(1):
		try:
			# print("procurando imagem")
			captcha = browser.find_elements_by_class_name('gc__3_EfD')[0]
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
	
	browser.refresh()
	time.sleep(3)

# firefox.quit()
