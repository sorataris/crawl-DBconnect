from kocrawl.editor.base_editor import BaseEditor
import re
import time

now = time

#시간대 별로 스케쥴러를 만들어서 kocrawl에서 스크립트를 연느 방식으로 실행해보자...
def what(date, result_date):  # 10의자리인지 1의자리인지 판별
    try:
        int(date[result_date + 1])
        return True
    except:
        return False

def cal_min(hour,date):
    print('에러난 부분:'+date)
    #오전 오후 마크 제거
    date = date.replace('오후 ','')
    date = date.replace('오전 ', '')
    print('에러난 부분:' + date)
    date_kind = date.split(' ')
    kind = ['1', '2', '3', '4', '5'] #10~50분
    result_date=1
    for i in kind:
        if date_kind[1].find(i) != -1:
            result_date=date_kind[1].find(i)
            print('찾은거 {}'.format(result_date))
            break

    if date_kind[1][result_date]=='1':
        result_min='10'
        result = hour+result_min
        return result

    elif date_kind[1][result_date] == '2':
        result_min = '20'
        result = hour + result_min
        return result
    elif date_kind[1][result_date] == '3':
        result_min = '30'
        result = hour + result_min
        return result
    elif date_kind[1][result_date] == '4':
        result_min = '40'
        result = hour + result_min
        return result
    elif date_kind[1][result_date] == '5':
        result_min = '50'
        result = hour + result_min
        return result
    else:
        result_min='00'
        result = hour + result_min




def date_find(date):
    kind = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    result = ''
    result_ex = ''
    result_date = 1
    for i in kind:
        if date.find(i) != -1:
            result_date = date.find(i)
            break
    # print("무야호")
    # print(result_date)  # 인식한 위치
    if what(date, result_date):  # 정수형이 가능?
        #  print("정수형 가능")
        result_ex = str(date[result_date]) + str(date[result_date + 1])
    # print(result_ex)
    # 문자형으로 합침
    else:
        result_ex = str(date[result_date])
    # print("정수형 불가능")
    #  print(result_ex)
    a='1'
    time_result = int(now.localtime().tm_hour) + int(result_ex)
    #   print("무야호2")
    print(time_result)
    if time_result > 23:
        result_data = str(time_result - 24)

        if int(result_data) < 10: #여기 고칠것 시간 앞에 0을 붙혀야함 뒤에 분 단위도 0분 쳐야함..이건 마지막에 split을 나누고 마지막에 zfill사용하면 될것 같다.
          result_data = str(result_data).zfill(2)
          print('그거:')
          print(str(result_data).zfill(2))

    print(result_data)
    return result_data


def cal_date(date):
    time_result = date_find(date)
    result = time_result + ':' + str(now.localtime().tm_min)
    return result

class Edit_date(BaseEditor):


    def act_date(date):
        new_word=''
        if date == '지금' or date=='': #예약이 아니라면
            return 'Now'

        if '시간' in date and ('후' in date or '있다' in date): #시간후
            pritn("시간 인식")
            new_word= cal_date(date)
            return new_word
        
        if '오후' in date:
            if '12시' in date:  # 오후
                if '반' in date or '30분' in date:  # 30분 단위
                    new_word = '12:30'
                    return new_word

                elif '분' in date:
                    new_word=cal_min('12:',date)
                    return new_word
                else:
                    new_word = '12:00'
                    return new_word

            if '10시' in date:  # 오후
                if '반' in date or '30분' in date:
                    new_word = '22:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('22:',date)
                    return new_word
                else:
                    new_word = '22:00'
                    return new_word

            if '11시' in date :  # 오후
                if '반' in date or '30분' in date:
                    new_word = '23:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('23:',date)
                    return new_word
                else:
                    new_word = '23:00'
                    return new_word
            if '1시' in date:  # 오후
                if '반' in date or '30분' in date:  # 30분 단위
                    new_word = '13:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('13:',date)
                    return new_word
                else:
                    new_word = '13:00'
                    return new_word

            if '2시' in date:  # 오후
                if '반' in date or '30분' in date:
                    new_word = '14:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('14:',date)
                    return new_word
                else:
                    new_word = '14:00'
                    return new_word

            if '3시' in date:  # 오후
                if '반' in date or '30분' in date:
                    new_word = '15:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('15:',date)
                    return new_word
                else:
                    new_word = '15:00'
                    return new_word

            if '4시' in date:  # 오후
                if '반' in date or '30분' in date:
                    new_word = '16:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('16:',date)
                    return new_word
                else:
                    new_word = '16:00'
                    return new_word

            if '5시' in date:  # 오후
                if '반' in date or '30분' in date:
                    new_word = '17:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('17:',date)
                    return new_word
                else:
                    new_word = '17:00'
                    return new_word

            if '6시' in date:  # 오후
                if '반' in date or '30분' in date:
                    new_word = '18:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('18:',date)
                    return new_word
                else:
                    new_word = '18:00'
                    return new_word

            if '7시' in date:  # 오후
                if '반' in date or '30분' in date:
                    new_word = '19:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('19:',date)
                    return new_word
                else:
                    new_word = '19:00'
                    return new_word

            if '8시' in date:  # 오후
                if '반' in date or '30분' in date:
                    new_word = '20:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('20:',date)
                    return new_word
                else:
                    new_word = '20:00'
                    return new_word

            if '9시' in date:  # 오후
                if '반' in date or '30분' in date:
                    new_word = '21:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('21:',date)
                    return new_word
                else:
                    new_word = '21:00'
                    return new_word


        else :
            if '12시' in date:  # 오전
                if '반' in date or '30분' in date:
                    new_word = '00:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('00:',date)
                    return new_word
                else:
                    new_word = '00:00'
                    return new_word

            if '1시' in date :
                if '반' in date or '30분' in date:
                    new_word = '01:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('01:',date)
                    return new_word
                else:
                    new_word = '01:00'
                    return new_word

            if '2시' in date:
                if '반' in date or '30분' in date:
                    new_word = '02:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('02:',date)
                    return new_word
                else:
                    new_word = '02:00'
                    return new_word

            if '3시' in date:
                if '반' in date or '30분' in date:
                    new_word = '03:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('03:',date)
                    return new_word
                else:
                    new_word = '03:00'
                    return new_word
            if '4시' in date:
                if '반' in date or '30분' in date:
                    new_word = '04:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('04:',date)
                    return new_word
                else:
                    new_word = '04:00'
                    return new_word

            if '5시' in date:
                if '반' in date or '30분' in date:
                    new_word = '05:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('05:',date)
                    return new_word
                else:
                    new_word = '05:00'
                    return new_word

            if '6시' in date:
                if '반' in date or '30분' in date:
                    new_word = '06:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('06:',date)
                    return new_word
                else:
                    new_word = '06:00'
                    return new_word

            if '7시' in date:
                if '반' in date or '30분' in date:
                    new_word = '07:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('07:',date)
                    return new_word
                else:
                    new_word = '07:00'
                    return new_word

            if '8시' in date:
                if '반' in date or '30분' in date:
                    new_word = '08:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('08:',date)
                    return new_word
                else:
                    new_word = '08:00'
                    return new_word

            if '9시' in date:
                if '반' in date or '30분' in date:
                    new_word = '09:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('09:',date)
                    return new_word
                else:
                    new_word = '09:00'
                    return new_word
            if '10시' in date:
                if '반' in date or '30분' in date:
                    new_word = '10:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('10:',date)
                    return new_word
                else:
                    new_word = '10:00'
                    return new_word

            if '11시' in date:
                if '반' in date or '30분' in date:
                    new_word = '11:30'
                    return new_word
                elif '분' in date:
                    new_word=cal_min('11:',date)
                    return new_word
                else:
                    new_word = '11:00'
                    return new_word




