text=input('年齢は？')
age=int(text)
if age>=6 and age <=15:
    print('義務教育の対象')

text=input('年齢は？')
age=int(text)
if age<=5 or age >=65:
    print('幼児と高齢者')

text=input('年齢は？')
if not text.isdigit():
    print('数値を入力して')

text=input('年齢は？')
if text.isdigit():
    age=int(text)
    if age<20:
        if age>=6 and age<=15:
            print('未成年(義務教育)')
        else:
            print('未成年')
    elif age<65:
        print('成人')
    else:
        print('高齢者')

text=input('年齢は？')
age=int(text)
if age<6:
    print('幼児')