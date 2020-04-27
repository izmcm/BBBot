# BBBot

O BBBot faz parte de um estudo sobre segurança da informação e processamento de imagem.    
**Quer saber mais sobre?** Leia no Medium:
[BBBot: Robôs podem votar no Big Brother?](https://medium.com/@izmcm/bbbot-rob%C3%B4s-podem-votar-no-big-brother-4b88a9f0176e)

O projeto foi testado no MacOS 10.14.3 e no Ubuntu 18.04

## Começando os trabalhos

### Pré-requisitos

* [Python3](https://www.python.org/)   
```
sudo apt-get install python3
```
* [Selenium](https://www.seleniumhq.org/) para simular a navegação 
```
sudo pip3 install selenium
```
* [OpenCV](https://opencv.org/) para o processamento de imagem do captcha
```
sudo pip3 install opencv-python
```
* [Mozilla Firefox](https://www.mozilla.org/pt-BR/firefox/new/) é o navegador que será usado
* [Geckodriver](https://github.com/mozilla/geckodriver/releases) - verificar releases mais recentes
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-macos.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/
```

### Utilizando o bot
Depois de instalar os pré-requisitos necessários, podemos clonar o repositório na pasta de preferência:

```
git clone https://github.com/izmcm/BBBot.git
```
As variáveis **url** e **nameSearch** devem ser trocadas, respectivamente, para o url de votação do site da Globo e para o nome da pessoa que será votada (da forma como se encontra escrito no site de votação).

Após isso, podemos caminhar até a pasta para rodar o projeto:
```
python3 script.py
```

Nesse momento, o Firefox abrirá automaticamente na página de votação e será necessário fazer o login no site. Após o login ser realizado, o programa se encarregará de votar na pessoa escolhida em **nomeSearch** e passar pelo captcha sozinho.

#### Demo
![demo](demo.gif)


###### Mais sobre processamento de imagem em captchas pode ser visto em [Captcha Break](https://github.com/izmcm/captcha-break)

## Licença

A licença do projeto é MIT License - olhar [LICENSE.md](LICENSE.md) para mais detalhes.

