<html>
<body>
<p>Проект представляет собой 
сервис ответов на вопросы. Пользователь сервиса имеет возможность 
зарегистрироваться, задать вопрос, ответить на вопросы других 
пользователей. Так же пользователь может отметить вопросы с помощь 
кнопки "лайк", изменяя их рейтинг. Прототип-образц - <a rel="nofollow" href="http://stackoverflow.com/">http://stackoverflow.com/</a><br></p><h2>Основные сущности проекта</h2><p></p><ol><li>Пользователь - email, имя, пароль, аватарка<br></li><li>Вопрос - заголовок, текст, автор, рейтинг вопроса</li><li>Ответ - текст, вопрос, автор, флаг "правильности"</li><li>Лайк - вопрос,&nbsp;пользователь</li></ol><h2>Формы и страницы проекта<br></h2><p>Главная страница</p><p>URL: &nbsp;/</p><p>Назначение:
 представляет из себя список "популярных" вопросов. В списке выводятся 
вопросы за последнюю неделю в порядке убывания рейтинга.</p><p>Список новых вопросов</p><p>URL: /new/<br></p><p>Назначение: список вопросов по дате их добавления начиная с самого свежего.</p><p>Страница одного вопроса<br></p><p>URL: /question/123/<br></p><p>Назначение:
 на этой странице можно прочитать текст вопрос и список ответов к нему. 
Авторизованные пользователи могут добавить свой ответ.<br></p><p>Страница регистрации<br></p><p>URL: /signup/</p><p>Назначение: пользователь может ввести свой email, пароль, имя, выбрать аватарку и зарегистрироваться в проекте<br></p><p>Страница авторизации</p><p>URL: /login/<br></p><p>Назначение: пользователь может ввести email и пароль и авторизоваться (войти) в проекте.</p><p>Страница добавления вопроса<br></p><p>URL: /ask/</p><p>Назначение: авторизованный пользователь может задать вопрос, после чего перейдет на страницу этого вопроса.<br></p><h2>Примерный дизайн</h2><h2><b><span class="image-wrapper"><img alt="mainpng" src="img/1.png" height="673" width="624"></span></b></h2><h2><b><span class="image-wrapper"><img alt="askpng" src="img/2.png" height="680" width="624"></span></b><br><b><span class="image-wrapper"><img alt="singlepng" src="img/3.png" height="787" width="624"></span></b><br></h2><p><b><span class="image-wrapper"><img alt="settingspng" src="img/4.png" height="677" width="624"></span></b></p><h2>AJAX&nbsp;запросы</h2><p>﻿</p><p>URL: /like/123/<br></p><p>Назначение:
 пользователь может нажать&nbsp;кнопку&nbsp;"Лайк" 
у&nbsp;вопроса&nbsp;и&nbsp;это&nbsp;увеличит&nbsp;рейтинг&nbsp;вопроса. 
Пользователь&nbsp;может&nbsp;ставить&nbsp;"лайк" не&nbsp;более 
&nbsp;1&nbsp;раза&nbsp;для&nbsp;1&nbsp;вопроса.</p>
</body></html>
