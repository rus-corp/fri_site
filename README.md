## Установка и запуск приложения
- Скачать скрипт и распаковать архив
- Создать и активировать виртуальное окружение
- Установить зависимости: `pip install -r requirements.txt`
- Установить фикстуры (там важные для работы приложения данные): `python manage.py loaddata fixtures/db.json`


Вход в админку с правами суперпользователя:
- **логин:** andryplekhanov@rambler.ru
- **Пароль:** Aa25662566!

## Деплойт
При деплойте вы столкнётесь с парой ошибок связанных с работой ‘django.contrib.sites'.
Вы должны войти в шелл (python manage.py shell) и написать следующие команды:
- `from django.contrib.sites.models import Site`
- `site = Site.objects.create(domain='http://ваш_домен.ru/', name=''http://ваш_домен.ru/)`
- `site.save()`

### Приложения:
   1 'app_users.apps.AppUsersConfig',                        -целиковый аккаунт пользователя
   2 'app_ads.apps.AppAdsConfig',                            -объявления
   3 'app_static_pages.apps.AppStaticPagesConfig',           -загрузка доков в бд для редактирования
   4 'app_settings.apps.AppSettingsConfig',                  - добавление соцсетей и компаний
   5 'app_survey.apps.AppSurveyConfig',                      - голосование
   6 'app_news.apps.AppNewsConfig',                          - раздел новости
   7 'app_personal_account.apps.AppPersonalAccountConfig',   - пополнение лиц.счета
   8 'app_referral_program.apps.AppReferralProgramConfig',   - рефералка
   9 'app_tickets.apps.AppTicketsConfig',
   10 'app_portfolio.apps.AppPortfolioConfig',

1- описана полная модель юзера, со всеми полями, данными 
3- для загрузки доков в бд и их редактирования в админке
7- пополнение лицевого счета фрилансера или заказчика для дальнейшего распределния этих денег между участниками
8- описана логика распределения средств по разным счетам
