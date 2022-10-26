import os,sys,pickle
import argparse,sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import threading
import  schedule
from kocrawl.answerer.firebase import firebase_cred
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

parser = argparse.ArgumentParser()
parser.add_argument('-time',help=':please set the time')  #시간
parser.add_argument('-object',help=':please set the object') #창문,LED,블라인드
parser.add_argument('-do',help=':please set the do') #ON OFF로 통일
args = parser.parse_args()
window_ref = db.reference()  # 창문 경로
PDLC_ref = db.reference()  # PDLC 경로
LED_ref = db.reference()  # 전등 경로

count=0
def window(do:str, date:str):
    check = firebase_cred.called_firebase('창문')
    if do=='OPEN':
        print("창문 실행 OPEN")
        window_ref.update({'window': "OPEN"})
        print("완료")
    elif do=='CLOSE':
        print("창문 실행 Close")
        window_ref.update({'window': "CLOSE"})
        
    return  sys.exit()
 #힌반민 실행하고 종료, 끝나고 화면이 안닫히니, os.exit비스무리한걸로 명령하자. & > /dev/null 파이썬 뒤에 이리 붙히면 백그라운드가 가능하다곤 한다.

def LED(do:str, date:str):
    check = firebase_cred.called_firebase('전등')
    if do=='ON':
        print("LED 실행 OPEN")
        LED_ref.update({'LED': "ON"})
    elif do=='OFF':
        print("LED 실행 CLOSE")
        LED_ref.update({'LED': "OFF"})
    return  sys.exit()

def PDLC(do:str, date:str):
    check = firebase_cred.called_firebase('사생활 보호모드')
    if do=='DOWN':
        PDLC_ref.update({'blind': "DOWN"})
    elif do=='UP':
        PDLC_ref.update({'blind': "UP"})
    return  sys.exit()


def main(argv,args):
    print('\n')
    print("입력된 인자의 이름값:")
    print(f'입력된 것:',args.object)

    if args.object == 'window':

            #여기서 부터 예약기능을 넣으면 댐
        schedule.every().day.at(args.time).do(window,args.do,args.time) #시간과 행위를 받아 스케쥴러를 처리함
        while True:
            schedule.run_pending()
            print("스케쥴 실행중...")

            time.sleep(10)
           # if flag_pdlc == '0': #한번하고 종
              #  break
       # ref.update({'window': "OPEN"})


    elif args.object == 'LED':
        schedule.every().day.at(args.time).do(LED,args.do, args.time)  # 시간과 행위를 받아 스케쥴러를 처리함
        while True:
            schedule.run_pending()
            print("스케쥴 실행중...")

            time.sleep(10)

    elif args.object == 'PDLC':
        schedule.every().day.at(args.time).do(PDLC, args.do, args.time)  # 시간과 행위를 받아 스케쥴러를 처리함
        while True:
            schedule.run_pending()
            print("스케쥴 실행중...")

            time.sleep(10)

    else:
        print("object가 잘못입력된 값!!")

if __name__ == '__main__':
    argv = sys.argv
    main(argv,args)