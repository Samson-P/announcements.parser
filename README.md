# announcements.parser
### Парсер новостей c сайта ByBit

## TODO:
1. Выполнять JS
2. Запрашивать свежие данные 1 раз в секунду (обходить возможные блокировки и кеширование CDN).

## Stack
Python, lib Selenium, CSV markup
<p>
 <img src="https://img.icons8.com/color/48/000000/python.png" alt="Python" width="30" height="30" />
 <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.iconscout.com%2Ficon%2Fpremium%2Fpng-512-thumb%2Fselenium-2-570545.png&f=1&nofb=1&ipt=8709d90bbb41a800775d8f3a814cc2c3a45e2b9dc0b9126ae89eff39bc224f10&ipo=images" alt="Python" width="30" height="30" />
 <img src="https://img.icons8.com/color/48/000000/csv.png" alt="Python" width="30" height="30" />
</p>

## Noties:
1. При использовании chromedriver может появиться блокировака selenium. Это исправляется при помощи selenium-stealth. Но в моем случае, при использовании firefox, никаких блокировок не было.

2. Обход ReCaptcha в selenium возможен только с использованием вручную созданного аккаута. На странице используется капча, которую можно обойти, пользуясь таким алгоритмом

a. Создаем «чистый» профиль браузера
Вручную вводим капчу и логинимся на нужный ресурс

2.3. Копируем необходимый профиль в наш проект

Вот пример написания кода

    # Инициализируем объект драйвера с использованием аккаунта человека
    options = Options()
    firefox_profile = FirefoxProfile(PROFILE_PATH)
    options.profile = firefox_profile
    self.browser = webdriver.Firefox(options=options)

Я не стал добавлять его в проект, т.к. мне он не понадобился, но сильно увеличивал время тестирования.

## 📫 Способы для связи

<div id="header" align="center">
 <p>
 <!--<img src="https://media.giphy.com/media/r3xBH1FXWz0h55CVtj/giphy.gif" width="130"/>-->
  <div>
   <a href="https://web.telegram.org/k/#@samson_pk"><img src="https://img.shields.io/badge/%40samson__pk-tg-blue" /></a>
   <a href="https://vk.com/s.pohilenko"><img src="https://img.shields.io/badge/s.pohilenko-vk-blue" /></a>
   <a href="mailto:samsonpohilenko@gmail.com"><img src="https://img.shields.io/badge/samsonpohilenko-gmail-yellowgreen" /></a>
   <img src="https://img.shields.io/badge/Samson--P%234193-discord-purple" />
  </div>
 </p>
</div>
