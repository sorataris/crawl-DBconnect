from kocrawl.answerer.base_answerer import BaseAnswerer
from kocrawl.answerer.firebase import firebase_cred
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# db경로설정

class LEDAnswerer(BaseAnswerer):


    def LED_form(self, result: dict) -> str:

        msg = ''  # 사용자 메시지
        # 불 켜 달라하면
        print('result op의 값')
        print(result['OP'])
        print("예약 날짜")
        print(result['date'])
        #화장실인가?

        check = firebase_cred.called_firebase(result['object'])
        check_BATH_LED = firebase_cred.called_LED(result['room'])

        if result['date']!='Now': #예약이 있으면
            print('안녕')
            if result['room']=='화장실':
                if 'ON' == result['OP']:
                    # firebase에서 데이터를 받아와 확인후 적용하는 부분
                    # firebase에서 LED태그값을 받아옴
                    # firebase에서 창문 상태값을 받아옴
                    print('firebase값 화장실')
                    print(check_BATH_LED)

                    if 'ON' == check_BATH_LED:  # 불이 이미 켜있을시
                        msg = '예약된 전등이 이미 켜져있습니다.'
                        print(msg)
                        return msg
                    elif 'OFF' == check_BATH_LED:  # 창문이 닫혀있는 상태일 시
                        # OFF 상태면 db값을 ON으로 갱신
                        # ref.update({'LED': "ON"})  # TTS를 사용하기 위해 response에 값 대입
                        msg = firebase_cred.change_db_for_bath(self, result['date'], result['object'], result['OP'])
                        print('함수 호출후 불러온 값:' + msg)
                        return msg
                    else:
                        msg = 'error LED_answerer.py== db 상태값이 config값과 다릅니다'
                        # 값을 몰?루기 떄문에 예외처리를 함
                        print('db값 형태가 잘못되었습니다!')
                        print('open/close,ON/OFF 형태로만 가능합니다.')
                        print('현재 db에 저장된 값:')
                        print(check)
                        return msg

                # 전등 꺼 하면
                elif 'OFF' == result['OP']:
                    # firebase에서 데이터를 받아와 확인후 적용하는 부분
                    # firebase에서 window태그값을 받아옴

                    print('db저장된 화장실 전등 값')
                    print(check_BATH_LED)
                    if 'OFF' == check_BATH_LED:  # 창문이 이미 닫혀있을시
                        msg = '예약된 전등은 이미 꺼져있습니다.'
                        print(msg)
                        return msg
                    elif 'ON' == check_BATH_LED:  # 창문이 열려있는 상태일 시
                        # close 상태면 db값을 close으로 갱신
                        # ref.update({'LED': "OFF"})  # TTS를 사용하기 위해 response에 값 대입
                        msg = firebase_cred.change_db_for_bath(self, result['date'], result['object'], result['OP'])
                        print('함수 호출후 불러온 값:' + msg)
                        return msg
                    else:
                        msg = 'error LED_answerer.py== db 상태값이 config값과 다릅니다'
                        # 값을 몰?루기 떄문에 예외처리를 함
                        print('db값 형태가 잘못되었습니다!')
                        print('open/close,ON/OFF 형태로만 가능합니다!.')
                        print('현재 db에 저장된 값:')
                        print(check_BATH_LED)
                        return msg


            else: #내방이라면
                if 'ON' == result['OP']:
                    # firebase에서 데이터를 받아와 확인후 적용하는 부분
                    # firebase에서 LED태그값을 받아옴
                    # firebase에서 창문 상태값을 받아옴
                    print('firebase값')
                    print(check)

                    if 'ON' == check:  # 불이 이미 켜있을시
                        msg = '예약된 전등이 이미 켜져있습니다.'
                        print(msg)
                        return msg
                    elif 'OFF' == check:  # 창문이 닫혀있는 상태일 시
                        # OFF 상태면 db값을 ON으로 갱신
                        # ref.update({'LED': "ON"})  # TTS를 사용하기 위해 response에 값 대입
                        msg = firebase_cred.change_db(self, result['date'], result['object'], result['OP'])
                        print('함수 호출후 불러온 값:' + msg)
                        return msg
                    else:
                        msg = 'error LED_answerer.py== db 상태값이 config값과 다릅니다'
                        # 값을 몰?루기 떄문에 예외처리를 함
                        print('db값 형태가 잘못되었습니다!')
                        print('open/close,ON/OFF 형태로만 가능합니다.')
                        print('현재 db에 저장된 값:')
                        print(check)
                        return msg

                # 전등 꺼 하면
                elif 'OFF' == result['OP']:
                    # firebase에서 데이터를 받아와 확인후 적용하는 부분
                    # firebase에서 window태그값을 받아옴

                    print('db저장값')
                    print(check)
                    if 'OFF' == check:  # 창문이 이미 닫혀있을시
                        msg = '예약된 전등은 이미 꺼져있습니다.'
                        print(msg)
                        return msg
                    elif 'ON' == check:  # 창문이 열려있는 상태일 시
                        # close 상태면 db값을 close으로 갱신
                        # ref.update({'LED': "OFF"})  # TTS를 사용하기 위해 response에 값 대입
                        msg = firebase_cred.change_db(self, result['date'], result['object'], result['OP'])
                        print('함수 호출후 불러온 값:' + msg)
                        return msg
                    else:
                        msg = 'error LED_answerer.py== db 상태값이 config값과 다릅니다'
                        # 값을 몰?루기 떄문에 예외처리를 함
                        print('db값 형태가 잘못되었습니다!')
                        print('open/close,ON/OFF 형태로만 가능합니다!.')
                        print('현재 db에 저장된 값:')
                        print(check)
                        return msg


        else : #예약이 없으면
            if result['room']=='화장실':
                if 'ON' == result['OP']:
                    # firebase에서 데이터를 받아와 확인후 적용하는 부분
                    # firebase에서 LED태그값을 받아옴
                    # firebase에서 창문 상태값을 받아옴
                    print('firebase값 화장실')
                    print(check_BATH_LED)

                    if 'ON' == check_BATH_LED:  # 불이 이미 켜있을시
                        msg = '화장실 전등이 이미 켜져있습니다.'
                        print(msg)
                        return msg
                    elif 'OFF' == check_BATH_LED:  # 창문이 닫혀있는 상태일 시
                        # OFF 상태면 db값을 ON으로 갱신
                        # ref.update({'LED': "ON"})  # TTS를 사용하기 위해 response에 값 대입
                        msg = firebase_cred.change_db_for_bath(self, result['date'], result['object'], result['OP'])

                    else:
                        msg = 'error LED_answerer.py== db 상태값이 config값과 다릅니다'
                        # 값을 몰?루기 떄문에 예외처리를 함
                        print('db값 형태가 잘못되었습니다!')
                        print('open/close,ON/OFF 형태로만 가능합니다.')
                        print('현재 db에 저장된 값:')
                        print(check)
                        return msg

                # 전등 꺼 하면
                elif 'OFF' == result['OP']:
                    # firebase에서 데이터를 받아와 확인후 적용하는 부분
                    # firebase에서 window태그값을 받아옴

                    print('db저장된 화장실 전등 값')
                    print(check_BATH_LED)
                    if 'OFF' == check_BATH_LED:  # 창문이 이미 닫혀있을시
                        msg = '화장실 전등은 이미 꺼져있습니다.'
                        print(msg)
                        return msg
                    elif 'ON' == check_BATH_LED:  # 창문이 열려있는 상태일 시
                        # close 상태면 db값을 close으로 갱신
                        # ref.update({'LED': "OFF"})  # TTS를 사용하기 위해 response에 값 대입
                        msg = firebase_cred.change_db_for_bath(self, result['date'], result['object'], result['OP'])

                    else:
                        msg = 'error LED_answerer.py== db 상태값이 config값과 다릅니다'
                        # 값을 몰?루기 떄문에 예외처리를 함
                        print('db값 형태가 잘못되었습니다!')
                        print('open/close,ON/OFF 형태로만 가능합니다!.')
                        print('현재 db에 저장된 값:')
                        print(check)
                        return msg


            else: #내방이라면
                if 'ON' == result['OP']:
                    # firebase에서 데이터를 받아와 확인후 적용하는 부분
                    # firebase에서 LED태그값을 받아옴
                    # firebase에서 창문 상태값을 받아옴
                    print('firebase값')
                    print(check)

                    if 'ON' == check:  # 불이 이미 켜있을시
                        msg = '내방 전등이 이미 켜져있습니다.'
                        print(msg)
                        return msg
                    elif 'OFF' == check:  # 창문이 닫혀있는 상태일 시
                        # OFF 상태면 db값을 ON으로 갱신
                        # ref.update({'LED': "ON"})  # TTS를 사용하기 위해 response에 값 대입
                        msg = firebase_cred.change_db(self, result['date'], result['object'], result['OP'])

                    else:
                        msg = 'error LED_answerer.py== db 상태값이 config값과 다릅니다'
                        # 값을 몰?루기 떄문에 예외처리를 함
                        print('db값 형태가 잘못되었습니다!')
                        print('open/close,ON/OFF 형태로만 가능합니다.')
                        print('현재 db에 저장된 값:')
                        print(check)
                        return msg

                # 전등 꺼 하면
                elif 'OFF' == result['OP']:
                    # firebase에서 데이터를 받아와 확인후 적용하는 부분
                    # firebase에서 window태그값을 받아옴

                    print('db저장값')
                    print(check)
                    if 'OFF' == check:  # 창문이 이미 닫혀있을시
                        msg = '내방 전등은 이미 꺼져있습니다.'
                        print(msg)
                        return msg
                    elif 'ON' == check:  # 창문이 열려있는 상태일 시
                        # close 상태면 db값을 close으로 갱신
                        # ref.update({'LED': "OFF"})  # TTS를 사용하기 위해 response에 값 대입
                        msg = firebase_cred.change_db(self, result['date'], result['object'], result['OP'])

                    else:
                        msg = 'error LED_answerer.py== db 상태값이 config값과 다릅니다'
                        # 값을 몰?루기 떄문에 예외처리를 함
                        print('db값 형태가 잘못되었습니다!')
                        print('open/close,ON/OFF 형태로만 가능합니다!.')
                        print('현재 db에 저장된 값:')
                        print(check)
                        return msg




        OP_change = self.change[result['OP']]
        msg = '{room} {object} {OP}드릴게요.' \
           .format(room=result['room'],object=result['object'],
                  OP=OP_change)
        firebase_cred.msg(msg)  # 대답 저장
        print('대답')
        print(msg)
        return msg

        # 다시 한글화를 시킴

