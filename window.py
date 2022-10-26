from kocrawl.answerer.window_answerer import WindowAnswerer
from kocrawl.base import BaseCrawler
from kocrawl.editor.window_editor import WindowEditor
from kocrawl.searcher.window_searcher import WindowSearcher


class WindowCrawler(BaseCrawler):

    def request(self,date:str, object: str, do: str):
        """
        날씨를 크롤링합니다.
        (try-catch로 에러가 나지 않는 함수)

        :param object: IoT 기기
        :param date: 날짜
        :param do : On/Off?
        :return: 만들어진진 문장
       """

        try:
            #print(self.request_debug(object, do))
            return self.request_debug(date,object, do)

        except Exception:
            return WindowAnswerer().sorry(
                '그 장치 상태는 알 수가 없어요.'
            )

    def request_dict(self,date:str, object: str, do: str):
        """
        날씨를 크롤링합니다.
        (try-catch로 에러가 나지 않는 함수)

        :param location: 지역
        :param date: 날짜
        :return: 만들어진진 문장
       """

        try:
            return self.request_debug(date,object, do)
        except Exception:
            return WindowAnswerer().sorry(
                '그 장치는 알 수가 없어요.'
            )

    def request_debug(self, date:str,object: str, do: str):
        """
        날씨를 크롤링합니다.
        (에러가 나는 디버깅용 함수)

        :param location: 지역
        :param date: 날짜
        :return: 만들어진진 문장
        """



        return self.Window_specific(date,object, do)


#__Specific == window
    def Window_specific(self,date:str,object: str, do: str) -> tuple:
        """
        특정 날짜 (e.g. 수요일, 이번주, 다음주 등)의
        날씨를 검색하고 조합합니다.

        :param location: 지역
        :return: 오늘 날씨
        """

        result_dict = WindowSearcher().pass_data(date,object, do) #딕셔너리 화
        result = WindowEditor().edit_window(result_dict) #open/close 인식을 위해 문장 수정
        print('result결과값')
        #print(WindowAnswerer().window_form(result))
        return WindowAnswerer().window_form(result)  #최종적으로 결과 출력후 db에 업데이트
