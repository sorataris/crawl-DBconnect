CRAWLER = {
    'kinds': {
        'dust': ['미세먼지', '초미세먼지', '오존']
    },

    'date': {
        'today': ['오늘', '지금', '현재'],
        'tomorrow': ['내일'],
        'after': ['모레', '내일모레'],
        'this_week': ['이번 주', '이번주', '금주', '금 주'],
        'specific': ['월', '월요일', '화', '화요일',
                     '수', '수요일', '목', '목요일',
                     '금', '금요일', '토', '토요일',
                     '일', '일요일','1일','2일','3일','4일','5일','6일','7일',
                     '8일','9일','10일','11일','12일','13일','14일','15일','16일','17일',
                     '18일','19일','20일','21일','22일','23일','24일','25일','26일','27일',
                     '28일','29일','30일','31일']
        #일 단위가 제대로 인식못한다... 한번 1일~31일까지 추가해보자
    }
}

SEARCH = {
    'url': {
        'naver': 'https://search.naver.com/search.naver?ie=utf8&query=',
        'google': 'https://www.google.com/search?q=',
        'naver_map': 'https://map.naver.com/v5/api/search?caller=pcweb&query=',
        'daum_dict': 'https://100.daum.net/',
        'daum_news': 'https://news.daum.net/ranking/popular/'
    },
    'headers': {
        #63.0.3239.132
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'referer': 'http://google.com'
    }
}

EDIT = {
    'dust': {
        '좋음': '좋은 상태에요.',
        '보통': '보통 수준이에요.',
        '한때나쁨': '한 때 나쁠 수 있어요. 가급적 마스크를 챙기세요.',
        '나쁨': '나쁘네요. 외출시 마스크를 꼭 챙기세요.',
        '매우나쁨': '매우 심각해요. 집에 있는게 좋을 거에요.',
        '데이터없음': '아직 데이터가 없어요.'
    },

    'weather': {
        '흐림': '날씨가 약간 흐릴 수 있어요.',
        '맑음': '아마 하늘이 맑을 것 같아요.',
        '구름': '하늘에 구름이 껴있을 수도 있어요.',
        '구름조금': '구름이 살짝 낄 수도 있어요.',
        '구름많음': '구름이 많이 낀 날씨에요.',
        '구름많고 한때 비': '구름이 많이이 끼고 한때 비가 내릴 수 있어요.',
        '대체로맑음': '대체로 날씨가 맑을 것 같아요.',
        '대체로흐림': '날씨가 대체로 흐릴 것 같아요.',
        '흐리고비': '흐리고 가끔 비가 올 수도 있을 것 같아요.',
        '맑으나때때로구름': '하늘은 맑지만 때때로 구름이 있을 수 있어요.',
        '흐리고한때비': '하늘이 흐리고 때로 비가 올 수도 있어요.',
        '흐리고때때로갬': '하늘이 때때로 흐리지만 금방 갤 수도 있어요.',
        '안개': '안개가 껴서 앞이 잘 안보일 수도 있어요.',
        '소나기': '갑자기 소나기가 내릴 수도 있어요. 주의하세요.',
        '광역성소나기': '넓은 지역에 걸쳐서 광역성 소나기가 내릴 수도 있어요.',
        '국지성소나기': '좁은 지역에 한해서 국지성 소나기가 내릴 수도 있어요.',
        '광역성뇌우': '넓은 지역에 걸쳐서 광역성 뇌우가 있을 수도 있어요.',
        '국지성뇌우': '좁은 지역에 한해서 국지성 뇌우가 있을 수도 있어요.',
        '뇌우': '하늘에서 번개가 칠수도 있어요.',
        '천둥': '하늘에서 천둥이 칠 수도 있습니다.',
        '돌풍': '바람이 매우 심하게 불 수도 있어요.',
        '태풍': '태풍이 올 수도 있습니다. 위험할 수 있으니 조심하세요.',
        '허리케인': '허리케인이 올 수도 있습니다. 위험할 수 있으니 조심하세요.',
        '쓰나미': '쓰나미가 발생할 수도 있어요. 굉장히 위험하니 조심하세요.',
        '비': '비가 내릴 수 있습니다. 나가신다면 우산을 챙기세요.',
        '눈': '하늘에서 눈이 내릴 수 있어요. 따뜻하게 입으세요.',
        '폭설': '하늘에서 눈이 엄청 많이 내릴 수도 있어요. 따뜻하게 입으세요.',
        '비와눈': '비와 눈이 함께 내릴 수 있어요. 우산을 챙기세요.',
        '소낙눈': '갑자기 한번에 많은 눈이 내릴 수 있어요. 따뜻하게 입으세요.',
        '우박': '우박이 떨어질 수도 있어요. 조심하세요.',
        '흐리고 가끔 비': '날씨가 흐리고 가끔 비가 내릴 수도 있어요.',
        '강우(천둥,번개동반)': '천둥,번개를 동반한 비가 내릴 수도 있어요.',
        '흐리고가끔소나기' : '대체로 날씨가 흐리겠지만, 소나기가 올 수 있어요.',
        '흐리고가끔비' : '대체로 흐리겠지만, 소나기가 올 수 있어요.',
        '데이터없음': '아직 데이터가 없어요.'
    }
,
    'window': {
        '문':'창문',
        '창틀':'창문',
        '윈도우':'창문',
        'window':'창문',
        '창문':'창문',
'닫어': 'CLOSE',
'닫아': 'CLOSE',
'닫아봐': 'CLOSE',
'닫아주세요': 'CLOSE',
'닫아주셈': 'CLOSE',
'닫아봐요': 'CLOSE',
'닫아버려': 'CLOSE',
'닫아줄래?': 'CLOSE',
'닫아줄래요?': 'CLOSE',
'닫어라': 'CLOSE',
'닫어줘':'CLOSE',
'닫아줘':'CLOSE',
'닫어봐': 'CLOSE',
'닫어줘': 'CLOSE',
'닫아봐': 'CLOSE',
'닫아라': 'CLOSE',
'닫어라': 'CLOSE',
'닫어버려': 'CLOSE',
'그만': 'CLOSE',
'그만해': 'CLOSE',
'그만해줘': 'CLOSE',
'그만해봐': 'CLOSE',
'그만하라고': 'CLOSE',
'그만해달라니까?': 'CLOSE',
'그만해달라고': 'CLOSE',
'그만해주면': 'CLOSE',
'그만해주라니까': 'CLOSE',
'그만해주세요': 'CLOSE',
'안할래': 'CLOSE',
'안할거야': 'CLOSE',
'안할거임': 'CLOSE',
'안한다': 'CLOSE',
'안할거다': 'CLOSE',
'안할것': 'CLOSE',
'안한다니까?': 'CLOSE',
'안함': 'CLOSE',
'안해': 'CLOSE',
'하지마': 'CLOSE',
'안할': 'CLOSE',

'열어': 'OPEN',
'열아': 'OPEN',
'열아봐': 'OPEN',
'열아주세요': 'OPEN',
'열아주셈': 'OPEN',
'열아봐요': 'OPEN',
'열아버려': 'OPEN',
'열아줄래?': 'OPEN',
'열아줄래요?': 'OPEN',
'열어라': 'OPEN',
'열어봐': 'OPEN',
'열아라': 'OPEN',
'열아줘':'OPEN',
'열어줘':'OPEN',
'열어봐': 'OPEN',
'열아봐': 'OPEN',
'열어버려': 'OPEN',
'시작': 'OPEN',
'시작해': 'OPEN',
'시작해줘': 'OPEN',
'시작해봐': 'OPEN',
'시작하라고': 'OPEN',
'시작해달라니까?': 'OPEN',
'시작해달라고': 'OPEN',
'시작해주면': 'OPEN',
'시작해주라니까': 'OPEN',
'시작해주세요': 'OPEN',
'할래': 'OPEN',
'할거야': 'OPEN',
'할거임': 'OPEN',
'한다': 'OPEN',
'할거다': 'OPEN',
'할것': 'OPEN',
'한다니까?': 'OPEN',
'함': 'OPEN',
'해': 'OPEN',
'지마': 'OPEN',
'할': 'OPEN',
'시켜':'OPEN',
'시켜줘':'OPEN',
'시켜':'OPEN',
'시켜라':'OPEN',
'시켜봐':'OPEN',
'시켜줄래':'OPEN',
'시켜주라':'OPEN'
       
    },
    'LED': {
        '전등': '전등',
        '불': '전등',
        '켜줘': 'ON',
        '켜줄래': 'ON',
        '켜': 'ON',
        '켜봐':'ON',
        '켜줘봐': 'ON',
        '켜주세요': 'ON',
        '켜줄래': 'ON',
        '켜줄래?': 'ON',
        '켜봐라': 'ON',
        '켜주라': 'ON',
        '켜라': 'ON',
        '키라니까': 'ON',
        '켜라니까?': 'ON',
        '켜봐': 'ON',
        '켜주셈': 'ON',
        '켜줘라': 'ON',
        '꺼줘': 'OFF',
        '꺼줄래': 'OFF',
        '꺼': 'OFF',
        '꺼줘봐': 'OFF',
        '꺼주세요': 'OFF',
        '꺼줄래': 'OFF',
        '꺼줄래?': 'OFF',
        '꺼봐라': 'OFF',
        '꺼주라': 'OFF',
        '꺼라': 'OFF',
        '끄라니까': 'OFF',
        '끄라니까?': 'OFF',
        '꺼봐': 'OFF',
        '꺼주셈': 'OFF',
        '꺼줘라': 'OFF',
        '끄줘': 'OFF',
        '끄줄래': 'OFF',
        '끄': 'OFF',
        '끄줘봐': 'OFF',
        '끄주세요': 'OFF',
        '끄줄래': 'OFF',
        '끄줄래?': 'OFF',
        '끄봐라': 'OFF',
        '끄주라': 'OFF',
        '끄라': 'OFF',
        '꺼라니까': 'OFF',
        '꺼라니까?': 'OFF',
        '끄봐': 'OFF',
        '끄주셈': 'OFF',
        '끄줘라': 'OFF',
        '꺼봐':'OFF'
    },

    'PDLC':{
        '꺼줘':'UP',
        '꺼':'UP',
        '꺼봐': 'UP',
        '꺼줘봐': 'UP',
        '꺼라': 'UP',
        '꺼주세요': 'UP',
        '오프': 'UP',
        '꺼봐라': 'UP',
        '꺼줄래?': 'UP',
        '꺼줄래': 'UP',
        '꺼주세요': 'UP',
        '그만': 'UP',
        '그만해': 'UP',
        '하지마': 'UP',
        '꺼도': 'UP',
        '꺼라': 'UP',
        '꺼줘라': 'UP',
        '꺼보셈': 'UP',
        '꺼봐요': 'UP',
        
        '켜줘':'DOWN',
        '켜':'DOWN',
        '켜봐': 'DOWN',
        '켜줘봐': 'DOWN',
        '켜라': 'DOWN',
        '켜주세요': 'DOWN',
        '온': 'DOWN',
        '켜봐라': 'DOWN',
        '켜줄래?': 'DOWN',
        '켜줄래': 'DOWN',
        '켜주세요': 'DOWN',
        '시작': 'DOWN',
        '시작해': 'DOWN',
        '시작해도': 'DOWN',
        '켜도': 'DOWN',
        '켜라': 'DOWN',
        '켜줘라': 'DOWN',
        '켜보셈': 'DOWN',
        '켜봐요': 'DOWN',
        '사생활모드': '사생활 보호모드',
        '사생활보호모드': '사생활 보호모드',
        '사생활': '사생활 보호모드',
        '사생활보호': '사생활 보호모드',
        '피디엘시': '사생활 보호모드',
        '피디엘씨': '사생활 보호모드',
        'pdlc': '사생활 보호모드',
        'PDLC':'사생활 보호모드'

    },

    'room':{
        '장실':'화장실',
        '화장실':'화장실',
        '화실':'화장실',
        '내방':'내방',
        '나의 방':'내방',

    }

}

ANSWER = {
    'dust_init': '{location}의 다양한 대기오염 정보를 전해드릴게요.\n',
    'weather_init': '{location}의 날씨 정보를 전해드릴게요.\n',
    'map_init': '{location}의 {place}에 대한 정보를 전해드릴게요!.\n',
    'window_init': '{object}, {OP}드릴게요!.',
    'fallback': "죄송해요.. 말씀하신 정보는 저도 잘 모르겠네요.",
    'change' : {
        'OPEN':'열어', #Window
        'CLOSE':'닫어', #Window
        'ON':'켜', #LED
        'OFF':'꺼', #LED
        'DOWN':'시작', #PDLC
        'UP':'종료', #PDLC
        '00:00':'오전 12시',
        '01:00':'오전 1시',
        '02:00':'오전 2시',
        '03:00':'오전 3시',
        '04:00': '오전 4시',
        '05:00': '오전 5시',
        '06:00': '오전 6시',
        '07:00': '오전 7시',
        '08:00': '오전 8시',
        '09:00': '오전 9시',
        '10:00': '오전 10시',
        '11:00': '오전 11시',
        '12:00': '오후 12시',
        '13:00': '오후 1시',
        '14:00': '오후 2시',
        '15:00': '오후 3시',
        '16:00': '오후 4시',
        '17:00': '오후 5시',
        '18:00': '오후 6시',
        '19:00': '오후 7시',
        '20:00': '오후 8시',
        '21:00': '오후 9시',
        '22:00': '오후 10시',
        '23:00': '오후 11시'

}


}
