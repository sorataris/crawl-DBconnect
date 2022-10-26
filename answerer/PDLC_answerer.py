from kocrawl.answerer.base_answerer import BaseAnswerer
from kocrawl.answerer.firebase import firebase_cred #firebase 함수
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# firebae연동
"""
cred = credentials.Certificate("C:/Users/user/Desktop/reko/kochat-master/mydb1.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://graduation-project-1-f9ef1-default-rtdb.firebaseio.com/'
})
# db경로설정
ref = db.reference()  # root 경로
window_ref = db.reference('/window')  # 창문 경로
PDLC_ref = db.reference('/blind')  # PDLC 겨오
LED_ref = db.reference('/LED')  # 전등 경로
"""

class PDLCAnswerer(BaseAnswerer):

    def PDLC_form(self, result: dict) -> str:
        """
        특정 날짜 (오전/오후 구분 없는) 출력 포맷


        :param result: 데이터 딕셔너리
        :return: 출력 메시지
        """
        msg = ''  # 사용자 메시지

        # 블라인드 켜 달라하면
        check = firebase_cred.called_firebase(result['object'])  # firebase에서 PDLC 상태값을 받아옴
        print('result op의 값')
        print(result['OP'])

        if result['date']!='Now': #예약
            if 'DOWN' == result['OP']:
                # firebase에서 데이터를 받아와 확인후 적용하는 부분
                # firebase에서 LED태그값을 받아옴

                if 'DOWN' == check:  # 불이 이미 켜있을시
                    msg = '예약하려는 사생활 보호모드는 이미 작동되고 있습니다.'
                    print(msg)
                    return msg
                elif 'UP' == check:  # 블라인드 작동 X시
                    # OFF 상태면 db값을 ON으로 갱신
                    msg=firebase_cred.change_db(self,result['date'],result['object'], result['OP'])  # TTS를 사용하기 위해 response에 값 대입
                    return msg
                else:
                    msg = 'error PDLC_answerer.py== db 상태값이 config값과 다릅니다'
                    # 값을 몰?루기 떄문에 예외처리를 함
                    print('db값 형태가 잘못되었습니다!')
                    print('open/close,ON/OFF,DOWN/UP 형태로만 가능합니다.')
                    print('현재 db에 저장된 값:')
                    print(check)
                    return msg

            # 블라인드 x 하면
            elif 'UP' == result['OP']:
                # firebase에서 데이터를 받아와 확인후 적용하는 부분
                # firebase에서 window태그값을 받아옴
                print('db저장값')
                print(check)
                if 'UP' == check:  # 블라인드가 이미 꺼져있을시
                    msg = '예약하려는 사생활 보호모드는 이미 꺼져 있습니다.'
                    print(msg)
                    return msg
                elif 'DOWN' == check:  # 창문이 열려있는 상태일 시
                    # close 상태면 db값을 close으로 갱신
                    msg=firebase_cred.change_db(self,result['date'],result['object'], result['OP'])  # TTS를 사용하기 위해 response에 값 대입
                    return msg
                else:
                    msg = 'error PDLC_answerer.py== db 상태값이 config값과 다릅니다'
                    # 값을 몰?루기 떄문에 예외처리를 함
                    print('db값 형태가 잘못되었습니다!')
                    print('open/close,ON/OFF,UP/DOWN 형태로만 가능합니다!.')
                    print('현재 db에 저장된 값:')
                    print(check)
                    return msg


        else: #예약 x
            if 'DOWN' == result['OP']:
                # firebase에서 데이터를 받아와 확인후 적용하는 부분
                # firebase에서 LED태그값을 받아옴

                if 'DOWN' == check:  # 불이 이미 켜있을시
                    msg = '사생활 보호모드는 이미 작동되고 있습니다.'
                    print(msg)
                    return msg
                elif 'UP' == check:  # 블라인드 작동 X시
                    # OFF 상태면 db값을 ON으로 갱신
                    firebase_cred.change_db(self,result['date'],result['object'], result['OP'])  # TTS를 사용하기 위해 response에 값 대입
                else:
                    msg = 'error PDLC_answerer.py== db 상태값이 config값과 다릅니다'
                    # 값을 몰?루기 떄문에 예외처리를 함
                    print('db값 형태가 잘못되었습니다!')
                    print('open/close,ON/OFF,DOWN/UP 형태로만 가능합니다.')
                    print('현재 db에 저장된 값:')
                    print(check)
                    return msg

            # 블라인드 x 하면
            elif 'UP' == result['OP']:
                # firebase에서 데이터를 받아와 확인후 적용하는 부분
                # firebase에서 window태그값을 받아옴
                print('db저장값')
                print(check)
                if 'UP' == check:  # 블라인드가 이미 꺼져있을시
                    msg = '사생활 보호모드는 이미 꺼져 있습니다.'
                    print(msg)
                    return msg
                elif 'DOWN' == check:  # 창문이 열려있는 상태일 시
                    # close 상태면 db값을 close으로 갱신
                    firebase_cred.change_db(self,result['date'],result['object'], result['OP'])  # TTS를 사용하기 위해 response에 값 대입
                else:
                    msg = 'error PDLC_answerer.py== db 상태값이 config값과 다릅니다'
                    # 값을 몰?루기 떄문에 예외처리를 함
                    print('db값 형태가 잘못되었습니다!')
                    print('open/close,ON/OFF,UP/DOWN 형태로만 가능합니다!.')
                    print('현재 db에 저장된 값:')
                    print(check)
                    return msg
        # 다시 한글화를 시킴
        OP_change = self.change[result['OP']]

        # msg = self.window_init.format(object=object)
        msg = '{object}를 {OP}할게요.' \
            .format(object=result['object'],
                    OP=OP_change)
        firebase_cred.msg(msg) #대답 저장
        print('대답')
        print(msg)
        return msg
