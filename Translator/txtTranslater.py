from translate import Translator
translator = Translator(to_lang='ko')

try:
    with open('test.txt',mode='r') as my_file:

        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open("test-ja.txt",mode='r+',encoding ='utf-8') as my_trnsFile:
            my_trnsFile.write(translation)
except FileNotFoundError as err:
    print("Some error")
    raise err
