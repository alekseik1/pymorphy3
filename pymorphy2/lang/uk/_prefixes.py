# -*- coding: utf-8 -*-
from __future__ import absolute_import

# Prefixes which don't change the word parse.
# The list is from
# https://github.com/languagetool-org/languagetool/blob/master/languagetool-language-modules/uk/src/main/resources/org/languagetool/resource/uk/dash_prefixes.txt
_DASH_PREFIXES = """
2D
2G
3D
3G
4D
4G
CAD
call
CD
CDMA
CFI
CNG
DDoS
DNS
DoS
DSL
dvd
e
fashion
FM
ftp
G
GMP
GPRS
GPS
grid
GSM
HD
HR
HSDPA
ID
IMEA
IP
IT
led
LCD
LNG
live
MLM
MTV
mp3
n
OSB
pdf
PhD
PIN
POS
pr
QR
R'n'B
R'N'B
R&B
R&D
s
sim
SOS
SPA
sms
TV
UMTS
USB
VIN
vip
VoIP
WAP
web
X
Y
аль
альфа
анти
АРВ
арт
аудіо
байк
байкер
бард
бас
бета
бізнес
бліц
блог
блок
блюз
бомж
бонус
ботокс
боулінг
брейк
бренд
бундес
вакуум
веб
велнес
ВІЛ
віп
віце
гала
гамма
гей
гейм
генерал
гештальт
ГМ
ГМО
гольф
гоп
горе
готик
гранд
ґранд
графіті
грид
грумінг
дайв
дайвінг
данс
даун
дельта
денс
дзен
джаз
диво
дизайн
дизель
долбі
допінг
ДОТС
драг
дрес
дубль
дурман
е
екіпаж
економ
експерт
екс
експрес
екстра
екстрим
екшн
еліт
ерзац
ескорт
євро
жлоб
зіц
зомбі
ЗПГ
івент
імідж
інвест
інді
інсентив
інтернет
інтим
інформ
історико
ІТ
ІЧ
йога
камер
кантрі
караоке
кастинг
квазі
кемпінг
кваліфайн
кібер
кітч
козак
коктейль
колл
комік
комікс
майстер
конгрес
консалтинг
контент
контр
конференц
концепт
кредит
кремль
крос
КСВ
лайт
лаунж
лейб
лесбі
лгбт
лже
ліберал
лор
люкс
люмпен
максі
маркетинг
мас
мега
медіа
менеджмент
метал
міді
мікс
мілітарі
міні
МММ
модерн
мульт
мультимедіа
напів
націонал
нація
НВЧ
нокаут
ностальжі
нью
обер
онлайн
офіс
ОУН
панк
ПВХ
ПЕТ
піар
пін
плейбек
ПЛР
покер
поп
пост
поттер
постпродакшн
прайм
прайс
прем'єр
преміум
прес
приват
продакшн
профі
псевдо
реаліті
реггі
резус
рейв
рентген
рейтинг
реп
ретро
референс
референц
ритм
РК
рок
ротарі
РХБ
салон
саунд
своп
секонд
секс
сексі
сервіс
скейт
скінхед
скретч
слем
смарт
смс
СНІД
соціал
СОС
соул
софт
спа
спам
спаринг
СПГ
спорт
спрей
стартап
стоп
стрес
стрип
стриптиз
супер
тайм
талант
тандем
танц
тату
ТБ
телеком
тест
топ
топлес
торент
тренд
тренінг
треш
триб'ют
трофі
тур
тюнинг
УЗД
ура
УФ
фан
фест
фешн
фітнес
флеш
ФМ
фолк
фольк
хеш
цар
чудо
хайтек
хард
хіпі
хостел
чіп
шейпінг
шенген
шеф
шопінг
шоу
штаб
юніор
"""

# TODO: prefixes without a hyphen?
KNOWN_PREFIXES = [
    line.strip()+"-"
    for line in _DASH_PREFIXES.split("\n")
    if line.strip()
]
