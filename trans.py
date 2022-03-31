import csv
from googletrans import Translator
TRANSLATE_FROM_PATH = 'D:\\webScraber\\finished.csv'
TRANSLATE_TO_PATH = 'D:\\webScraber\\final\\translate.csv'
translator = Translator()

with open(TRANSLATE_TO_PATH, 'a',newline="", encoding='utf-8') as t, open(TRANSLATE_FROM_PATH, 'r', encoding='utf-8') as f:
    fileWriter = csv.writer(t)
    fileReader = csv.reader(f)
    afterTr = []
    for line in fileReader:
        if len(line) == 0 : continue
        toTranslate = [line[0],line[3],line[4]]
        print(toTranslate)
        afterTr = [tr.text for tr in translator.translate(toTranslate, dest='en')]
        print(afterTr)
        afterTr.insert(1,line[1])
        afterTr.insert(2,line[2])
        fileWriter.writerow(afterTr)
        # afterTr.append(translator.translate(line[0], dest='en').text)
        # afterTr.append(line[1])
        # afterTr.append(line[2])
        # afterTr.append(translator.translate(line[3], dest='en').text)
        # afterTr.append(translator.translate(line[4], dest='en').text)
        # print(line)
        # print(line[0],"\n" ,line[3],"\n",line[4])
        # fileWriter.writerow(afterTr)
        afterTr = []
    f.close()
    t.close()
            
    

# translatedText = translator.translate('3 Zimmer Wohnung Usingen', dest='en').text
# print(translatedText)



