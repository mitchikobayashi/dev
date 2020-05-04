# def create_mail():
#     print('PT企画の斉藤です。')
#     print('今月の請求書を送ります。')

# create_mail()

# def create_mail(recv):
#     print(recv,'様')
#     print('PT企画の斉藤です。')
#     print('今月の請求書を送ります。')

# create_mail('山本')
# create_mail('吉田')

# def create_mail(recv,bill):
#     tmp='''{}様
# PT企画の斉藤です。
# 今月の請求額は{}円です。
# '''
#     msg=tmp.format(recv,bill)
#     print (msg)

# create_mail('山本','40,000')

def add_charge(bill):
    return int(bill*1.07)

print(add_charge(60000))