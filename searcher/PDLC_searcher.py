from kocrawl.searcher.base_searcher import BaseSearcher
import re


class PDLCSearcher(BaseSearcher):
    # 'naver_weather': '.info_data > .info_list > li > .cast_txt',
    # 'naver_temperature': '.info_temperature > .todaytemp',
    def __init__(self):
        # 셀렉터 정의
        # 따로따로 정의 시도

        self.data_dict = {
            # 데이터를 담을 딕셔너리 구조를 정의합니다.
            'date':None,
            'object': None,
            'OP': None,
        }

    def _make_query(self, location: str, date: str) -> str:
        return ' '.join([location, date, '의미없는 함수'])




    def pass_data(self, date:str,object: str, OP: str) -> dict:

        #정의된 딕셔너리 구조를 만들어, 안에 입력받은 값들을 넣음
        #공백 제거
        self.data_dict['date'] = date
        self.data_dict['object'] = re.sub(' ', '',object)
        self.data_dict['OP'] = re.sub(' ', '',OP)

        return self.data_dict
