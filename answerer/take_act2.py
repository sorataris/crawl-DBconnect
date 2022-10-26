import os, sys, pickle
import argparse, sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import threading
import schedule
from kocrawl.answerer.firebase import firebase_cred
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

parser = argparse.ArgumentParser()
parser.add_argument('-time', help=':please set the time')  # 시간
parser.add_argument('-do', help=':please set the do')  # ON OFF로 통일
args = parser.parse_args()

LED_ref = db.reference('/BATH')  # 전등 경로




# 힌반민 실행하고 종료, 끝나고 화면이 안닫히니, os.exit비스무리한걸로 명령하자. & > /dev/null 파이썬 뒤에 이리 붙히면 백그라운드가 가능하다곤 한다.

def LED(do: str, date: str):
    check = firebase_cred.called_LED('화장실')
    if do == 'ON':
        print("LED 실행 OPEN")
        LED_ref.update({'LED': "ON"})
    elif do == 'OFF':
        print("LED 실행 CLOSE")
        LED_ref.update({'LED': "OFF"})
    return sys.exit()


def main(argv, args):
    print('\n')


    if args.object == 'BATH_LED':
        schedule.every().day.at(args.time).do(LED, args.do, args.time)  # 시간과 행위를 받아 스케쥴러를 처리함
        while True:
            schedule.run_pending()
            print("스케쥴 실행중...")

            time.sleep(10)

    else:
        print("object가 잘못입력된 값!!")


if __name__ == '__main__':
    argv = sys.argv
    main(argv, args)