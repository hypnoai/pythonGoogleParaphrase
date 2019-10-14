from googletrans import Translator
import random

languages = [
    'af',
    'sq',
    'am',
    'ar',
    'hy',
    'az',
    'eu',
    'bn',
    'bs',
    'bg',
    'ca',
    'ceb',
    'zh-CN',
    'zh-TW',
    'co',
    'hr',
    'cs',
    'da',
    'nl',
    'eo',
    'et',
    'fi',
    'fr',
    'fy',
    'gl',
    'ka',
    'de',
    'el',
    'gu',
    'ht',
    'ha',
    'haw',
    'iw',
    'hi',
    'hmn',
    'hu',
    'is',
    'ig',
    'id',
    'ga',
    'it',
    'ja',
    'jw',
    'kn',
    'kk',
    'km',
    'ko',
    'ku',
    'lo',
    'lv',
    'lt',
    'lb',
    'mk',
    'mg',
    'ms',
    'ml',
    'mt',
    'mi',
    'mr',
    'mn',
    'ne',
    'no',
    'ny',
    'ps',
    'fa',
    'pl',
    'pt',
    'pa',
    'ro',
    'ru',
    'sm',
    'gd',
    'sr',
    'st',
    'sn',
    'sd',
    'si',
    'sk',
    'sl',
    'so',
    'es',
    'sw',
    'sv',
    'tl',
    'tg',
    'ta',
    'te',
    'th',
    'tr',
    'uk',
    'ur',
    'uz',
    'vi',
    'cy',
    'xh',
    'yi',
    'yo',
    'zu',
  ]


def textSpinUsingTranslate(text='Type in anything that you want. Then click the button on the right to paraphrase your input.', spinTimes=10, arrayTexts=None):
  translator = Translator()
  random.shuffle(languages) # shuffle langs
  Langs = languages[0:spinTimes]
  newInputTxt = text
  
  inputTexts = [newInputTxt]
  
  if arrayTexts != None:
    inputTexts = arrayTexts # allows arrays also
    
  for i in range(len(Langs)):
    destLang = Langs[i]
    if i == len(Langs) - 1:
      destLang = 'en'
      
    translations = translator.translate(inputTexts, dest=destLang)      
    for x in range(len(translations)):
      translation = translations[x]
      if x == 0:
        inputTexts = [] # clear array
      inputTexts.append(translation.text)
    if i == len(Langs) - 1:
      return inputTexts
        

result = textSpinUsingTranslate(spinTimes=5)
print(result)
