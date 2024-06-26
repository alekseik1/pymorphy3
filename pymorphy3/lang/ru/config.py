"""
Constants and configuration for Russian language.
"""
from pymorphy3 import units

# paradigm prefixes used for dictionary compilation
PARADIGM_PREFIXES = ["", "по", "наи"]

# letters initials can start with
INITIAL_LETTERS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ'

# a list of particles which can be attached to a word using a hyphen
PARTICLES_AFTER_HYPHEN = ["-то", "-ка", "-таки", "-де", "-тко", "-тка", "-с", "-ста"]

# "ё" is sometimes written as "е", but not the other way around
CHAR_SUBSTITUTES = {'е': 'ё'}

# Prefixes which don't change the word parse.
KNOWN_PREFIXES = [
    "авиа",
    "авто",
    "аква",
    "анти",
    "анти-",
    "антропо",
    "архи",
    "арт",
    "арт-",
    "астро",
    "аудио",
    "аэро",
    "без",
    "бес",
    "био",
    "вело",
    "взаимо",
    "вне",
    "внутри",
    "видео",
    "вице-",
    "вперед",
    "впереди",
    "гекто",
    "гелио",
    "гео",
    "гетеро",
    "гига",
    "гигро",
    "гипер",
    "гипо",
    "гомо",
    "дву",
    "двух",
    "де",
    "дез",
    "дека",
    "деци",
    "дис",
    "до",
    "евро",
    "за",
    "зоо",
    "интер",
    "инфра",
    "квази",
    "квази-",
    "кило",
    "кино",
    "контр",
    "контр-",
    "космо",
    "космо-",
    "крипто",
    "лейб-",
    "лже",
    "лже-",
    "макро",
    "макси",
    "макси-",
    "мало",
    "меж",
    "медиа",
    "медиа-",
    "мега",
    "мета",
    "мета-",
    "метео",
    "метро",
    "микро",
    "милли",
    "мини",
    "мини-",
    "моно",
    "мото",
    "много",
    "мульти",
    "нано",
    "нарко",
    "не",
    "небез",
    "недо",
    "нейро",
    "нео",
    "низко",
    "обер-",
    "обще",
    "одно",
    "около",
    "орто",
    "палео",
    "пан",
    "пара",
    "пента",
    "пере",
    "пиро",
    "поли",
    "полу",
    "после",
    "пост",
    "пост-",
    "порно",
    "пра",
    "пра-",
    "пред",
    "пресс-",
    "противо",
    "противо-",
    "прото",
    "псевдо",
    "псевдо-",
    "радио",
    "разно",
    "ре",
    "ретро",
    "ретро-",
    "само",
    "санти",
    "сверх",
    "сверх-",
    "спец",
    "суб",
    "супер",
    "супер-",
    "супра",
    "теле",
    "тетра",
    "топ-",
    "транс",
    "транс-",
    "ультра",
    "унтер-",
    "штаб-",
    "экзо",
    "эко",
    "эндо",
    "эконом-",
    "экс",
    "экс-",
    "экстра",
    "экстра-",
    "электро",
    "энерго",
    "этно",
]

# default analyzer units
DEFAULT_UNITS = [
    [
        units.DictionaryAnalyzer(),
        units.AbbreviatedFirstNameAnalyzer(INITIAL_LETTERS),
        units.AbbreviatedPatronymicAnalyzer(INITIAL_LETTERS),
    ],

    units.NumberAnalyzer(),
    units.PunctuationAnalyzer(),
    [
        units.RomanNumberAnalyzer(),
        units.LatinAnalyzer()
    ],

    units.HyphenSeparatedParticleAnalyzer(PARTICLES_AFTER_HYPHEN),
    units.HyphenAdverbAnalyzer(),
    units.HyphenatedWordsAnalyzer(skip_prefixes=KNOWN_PREFIXES),
    units.KnownPrefixAnalyzer(known_prefixes=KNOWN_PREFIXES),
    [
        units.UnknownPrefixAnalyzer(),
        units.KnownSuffixAnalyzer()
    ],
    units.UnknAnalyzer(),
]
