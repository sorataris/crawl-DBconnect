from kocrawl.searcher.base_searcher import BaseSearcher
import re


class LEDSearcher(BaseSearcher):
    # 'naver_weather': '.info_data > .info_list > li > .cast_txt',
    # 'naver_temperature': '.info_temperature > .todaytemp',
    def __init__(self):
        # 셀렉터 정의
        # 따로따로 정의 시도

        self.data_dict = {
            # 데이터를 담을 딕셔너리 구조를 정의합니다.
            'room':None,
            'object': None,
            'OP': None,
            'date':None
        }

    def _make_query(self, location: str, date: str) -> str:
        """
        안쓰는 함수
        """

        return ' '.join([location, date, '날씨'])


    def pass_data(self, room:str,date: str,object: str, OP: str) -> dict:

        #정의된 딕셔너리 구조를 만들어, 안에 입력받은 값들을 넣음
        self.data_dict['room'] = room
        self.data_dict['object'] = re.sub(' ', '',object)
        self.data_dict['OP'] = re.sub(' ', '',OP)
        self.data_dict['date'] = date
        return self.data_dict
