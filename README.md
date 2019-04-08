# BBBot

BBBot é um bot que realiza votações no [Big Brother Brasil 19](https://gshow.globo.com/realities/bbb/). Esse projeto faz parte de um estudo pessoal sobre segurança da informação e processamento de imagem.

## Começando

O projeto foi testado no MacOS 10.14.3

### Pré-requisitos

* [Python3](https://www.python.org/)   
* [Selenium](https://www.seleniumhq.org/) para simular a navegação
* [Mozilla Firefox](https://www.mozilla.org/pt-BR/firefox/new/) o navegador que será usado 
* [OpenCV](https://opencv.org/) para o processamento de imagem do captcha

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

Nesse momento, o Firefox abrirá automaticamente na página de votação e será necessário fazer o login no site. Após o login ser realizado, o programa se encarregará de votar na pessoa escolhida e passar pelo captcha.



```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
