import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from kocrawl.decorators import answerer
import time
import threading
import  schedule
from kocrawl.answerer.base_answerer import BaseAnswerer
import os
# firebae연동
cred = credentials.Certificate("firebase db json파일 주소")
firebase_admin.initialize_app(cred, {
    #db 주소
})
ref = db.reference('')  # db user 경로
window_ref = db.reference('')  # 창문 경로
PDLC_ref = db.reference('')  # PDLC 경로
LED_ref = db.reference('')  # 전등 경로
BATH_LED_ref = db.reference('')
BATH_ref = db.reference('')
sch=("") #스케쥴러 파일 경로

#프로그램안에 스케쥴러로 실행하자니...멀티 프로세스로 스케쥴러가 while문 때문에 실행이 되지않는다. 파이썬 스크립트를 따로 만들어서 실행시키는 방식으로 해보자...


class firebase_cred(BaseAnswerer) :


    def called_firebase(key: str):

        if '창문' == key:
            result = window_ref.get()
            return result
        elif '전등' == key:
            result= LED_ref.get()
            return  result

        elif '사생활 보호모드' == key:
            result= PDLC_ref.get()
            return  result

        msg='해당 데이터가 없습니다!. firebase.py().called_firebase'

        return msg

    def called_LED(key: str):

        if '화장실' == key:

            result = BATH_LED_ref.get()
            print("bath lED값")
            print(result)
            return result
        elif '전등' == key:
            result = LED_ref.get()
            return  result

        msg='해당 데이터가 없습니다!. firebase.py().called_firebase'

        return msg



    def change_db(self,date: str,object: str, OP: str):
        print("change db에 들어온값:")
        print(date)

        if date == 'Now': #예약 x일때
            print("debugging="+object+OP)
            if '창문' == object:
                if 'OPEN' == OP:
                    ref.update({'Window': "OPEN"})
                    return
                elif 'CLOSE' == OP:
                    ref.update({'Window': "CLOSE"})
                    return
            elif '전등' == object:
                if 'ON' == OP:
                    ref.update({'LED': "ON"})
                    return
                elif 'OFF' == OP:
                    ref.update({'LED': "OFF"})
                    return
            elif '사생활 보호모드' == object:
                if 'UP' == OP:
                    ref.update({'Blind': "UP"})
                    print("UPping")
                    return
                elif 'DOWN' == OP:
                    ref.update({'Blind': "DOWN"})
                    print("Downning")
                    return

        else: #예약일때
            print("예약 실행")
            #실행 할 파일(-time,-object,-do)
           # result_data="/home/pi/.pyenv/versions/3.7.13/lib/python3.7/site-packages/kocrawl/answerer/take_act.py -time "+time+" -object "+objects+" -do "+do
          #  os.system(result_data)
            
            #대답 생성
            re_OP = self.change[OP]
           # print(re_OP)
            if ':00' in date:
                new_date = self.change[date] #11:00->11시
                result = new_date + "에 "+object+" "+re_OP+"드릴게요"
            else:
                new_date = date.replace(':','시')
                result = new_date + "분에 "+object+" "+re_OP+"드릴게요"
           # print(result)
            return result


    def change_db_for_bath(self, date: str, object: str, OP: str):
        print("change db에 들어온값:")
        print(date)

        if date == 'Now':  # 예약 x일때

            if '전등' == object:
                if 'ON' == OP:
                    BATH_ref.update({'LED': "ON"})
                    return
                elif 'OFF' == OP:
                    BATH_ref.update({'LED': "OFF"})
                    return

        else:  # 예약일때
            print("예약 실행")
            # 실행 할 파일(-time,-object,-do)
            #화장실 전용으로 경로
            # 대답 생성
            re_OP = self.change[OP]
            # print(re_OP)
            if ':00' in date:
                new_date = self.change[date]  # 11:00->11시
                result = new_date + "에 " + "화장실"+object + " " + re_OP + "드릴게요"
            else:
                new_date = date.replace(':', '시')
                result = new_date + "분에 " + "화장실"+object + " " + re_OP + "드릴게요"
            # print(result)
            return result

    def msg(msg: str):
        ref.update({'response':msg}) #대답 저장
        return