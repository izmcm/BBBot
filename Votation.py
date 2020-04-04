from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from binascii import a2b_base64
import processing
from getpass import getpass

class Votation:
	def __init__(self, tipoParedao = 'triplo', buscarLinkParedaoAuto = True):
		self.url = ''
		self.__tipoParedao = tipoParedao
		self.__paginaInicialGshow = "https://gshow.globo.com/realities/bbb/"
		self.__loginUrl = "https://minhaconta.globo.com/"
		self.__login = ''
		self.__password = ''
		self.__browser = None
		self.__setBrowser()
		self.__getLoginAcessGlobo()
		
		if buscarLinkParedaoAuto:
			self.__getUrlVotationGshow()
	
	def __setBrowser(self):
		try:
			caps = DesiredCapabilities().CHROME.copy()
			caps["pageLoadStrategy"] = "eager"  #  interactive
			self.__browser = webdriver.Chrome(capabilities=caps)
			
		except:
			caps = DesiredCapabilities().FIREFOX.copy()
			caps["pageLoadStrategy"] = "eager"  #  interactive
			self.__browser = webdriver.Firefox(capabilities=caps)


	def __getLoginAcessGlobo(self):
		self.__login = input("Digite seu email: ")
		
		print("Digite sua senha: ")
		self.__password = getpass()

		self.__browser.get(self.__loginUrl)

		time.sleep(10)
		print("fazendo o login")

		self.__browser.find_element_by_id('login').send_keys(self.__login)
		self.__browser.find_element_by_id('password').send_keys(self.__password)
		self.__browser.find_elements_by_css_selector('#login-form .button')[0].click()

		print("login finalizado")
		time.sleep(5)

	def __getNamesBigWall(self, titleParts):
		namesAux = titleParts.split(', ')
		names = [namesAux[0].strip()]
		names = names + namesAux[1].split(' ou ')

		return names

	def __votationDoubleBigWall(self, titleParts):
		names = self.__getNamesBigWall(titleParts)

		option = input("Quem você quer eliminar?: \n 1. " + names[0] + "\n 2. " + names[1] + "\nDigite o número da pessoa: ")
		while not option in ["1", "2"]:
			option = input("Quem você quer eliminar?: \n 1. " + names[0] + "\n 2. " + names[1] + "\nDigite o número da pessoa: ")

		nameSearch = names[int(option)-1]
		idxName = names.index(nameSearch)

		return idxName;
	
	def __votationTrippleBigWall(self, titleParts):
		names = self.__getNamesBigWall(titleParts)

		option = input("Quem você quer eliminar?: \n 1. " + names[0] + "\n 2. " + names[1] + "\n 3. " + names[2] + "\nDigite o número da pessoa: ")
		while not option in ["1", "2", "3"]:
			option = input("Quem você quer eliminar?: \n 1. " + names[0] + "\n 2. " + names[1] + "\n 3. " + names[2] + "\nDigite o número da pessoa: ")

		
		nameSearch = names[int(option)-1]
		idxName = names.index(nameSearch)

		return idxName;

	def __executeVotation(self, idxName):
		totalVotes = 0

		while True:
			element = []
			while(1):
				try:
					element = [
						self.__browser.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div[4]/div[1]'),
						self.__browser.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div[4]/div[2]'),
						self.__browser.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div[4]/div[3]'),
					]
					break
				except:
					pass

			elementBtn = element[idxName]

			# scroll down
			self.__browser.execute_script("window.scrollTo(0, 800)") 
		
			ac2 = ActionChains(self.__browser)
			ac2.move_to_element(elementBtn).click().perform()
			time.sleep(3)

			outSideLoop = True
			innerLoop = True

			while outSideLoop:
				ac = ActionChains(self.__browser)
				captchaBox = []

				vote_succeeded = False

				while innerLoop:
					try:
						captchaBox = self.__browser.find_elements_by_class_name('gc__2Qtwp')
						if captchaBox != []:
							if len(captchaBox[0].text) > 2:
								break

						time.sleep(1)

						value = self.__browser.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[3]/div/div/div[1]/div[2]/button')
						if value.text != '':
							vote_succeeded = True
							outSideLoop = False
							innerLoop = False
							break
					except:
						pass

				if vote_succeeded:
					totalVotes += 1
					print(totalVotes, 'votos com sucesso')
					break
				
				imageSearchName = captchaBox[0].text.split('\n')[-1]
				print("\nProcurando por: " + imageSearchName)

				captcha = []
				while(1):
					try:
						captcha = self.__browser.find_elements_by_class_name('gc__3_EfD')[0]
						break
					except:
						pass

				captchaSrc = captcha.get_attribute("src")

				data = captchaSrc.split(';base64,')[1]
				binary_data = a2b_base64(data)

				filename = imageSearchName + '.png'

				fd = open('BBB20/captchas/' + filename, 'wb')
				fd.write(binary_data)
				fd.close()

				processing.processImage(filename)
				points = processing.findInCaptcha(filename)
				

				if points != []:
					posX = points[0] - captcha.size['width']/2
					posY = points[1] - captcha.size['height']/2

					ac.move_to_element(captcha).move_by_offset(posX, posY).click().perform()
					time.sleep(3)
				else:
					print("\nErro: Captcha não encontrado")
				
				time.sleep(1)
			
			self.__browser.refresh()
			time.sleep(1)
	
	def __getUrlVotationGshow(self):
		print("Buscando paredão atual")
		self.__browser.get(self.__paginaInicialGshow)

		time.sleep(10)
		elementBtn = self.__browser.find_element_by_xpath('/html/body/div[2]/main/div[3]/div/div/div/div/div[1]/div/a')
		ac2 = ActionChains(self.__browser)
		ac2.move_to_element(elementBtn).click().perform()
		time.sleep(3)
		print("Paredão atual encontrado")
		self.setUrl(self.__browser.current_url)

	def setUrl(self, url):
		self.url = url
		return self

	def initVotation(self):
		self.__browser.get(self.url)
		print("\nIniciando o bot de votações")

		while(1):
			try:
				title = self.__browser.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div[3]/div/div/div').text
				
				break
			except:
				pass

		print(title)

		time.sleep(5)

		titleParts = title.split('?')[1]

		print(titleParts)

		if self.__tipoParedao == 'triplo':
			idxName = self.__votationTrippleBigWall(titleParts)
		else:
			idxName = self.__votationDoubleBigWall(titleParts)
		
		self.__executeVotation(idxName)