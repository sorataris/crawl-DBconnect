from kocrawl.searcher.base_searcher import BaseSearcher
import re


class WindowSearcher(BaseSearcher):
    # 'naver_weather': '.info_data > .info_list > li > .cast_txt',
    # 'naver_temperature': '.info_temperature > .todaytemp',
    def __init__(self):
        # 셀렉터 정의
        # 따로따로 정의 시도

        self.data_dict = {
            # 데이터를 담을 딕셔너리 구조를 정의합니다.
            'date': None,
            'object': None,
            'OP': None,
        }

    def _make_query(self, location: str, date: str) -> str:
        """
        검색할 쿼리를 만듭니다.

        :param location: 지역
        :param date: 날짜
        :return: "지역 날짜 날씨"로 만들어진 쿼리
        """

        return ' '.join([location, date, '날씨'])


    def pass_data(self, date:str,object: str, OP: str) -> dict:

        #정의된 딕셔너리 구조를 만들어, 안에 입력받은 값들을 넣음
        self.data_dict['date'] = date
        self.data_dict['object'] = re.sub(' ', '',object)
        self.data_dict['OP'] = re.sub(' ', '',OP)

        return self.data_dict
