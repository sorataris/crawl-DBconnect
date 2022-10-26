from kocrawl.answerer.LED_answerer import LEDAnswerer
from kocrawl.base import BaseCrawler
from kocrawl.editor.LED_editor import LEDEditor
from kocrawl.searcher.LED_searcher import LEDSearcher


class LEDCrawler(BaseCrawler):

    def request(self,room:str, date:str, object: str, do: str):
        """

        (try-catch로 에러가 나지 않는 함수)

        :param location: 지역
        :param date: 날짜
        :return: 만들어진진 문장
       """

        try:
          #  print(self.request_debug(object, do))
            return self.request_debug(room,date,object, do)
        except Exception as e:
            print(e)
            return LEDAnswerer().sorry(
                '그 장치 상태는 알 수가 없어요.'
            )

    def request_dict(self,room:str, date:str, object: str, do: str):
        """

        (try-catch로 에러가 나지 않는 함수)

        :param location: 지역
        :param date: 날짜
        :return: 만들어진진 문장
       """

        try:
            return self.request_debug(room,date,object, do)
        except Exception as e :
            print(e)
            return LEDAnswerer().sorry(
                '그 장치는 알 수가 없어요.'
            )

    def request_debug(self,room:str, date:str, object: str, do: str):
        """

        (에러가 나는 디버깅용 함수)

        :param location: 지역
        :param date: 날짜
        :return: 만들어진진 문장
        """



        return self.LED_specific(room,date,object, do)


#__Specific == window
    def LED_specific(self,room:str, date:str,object: str, do: str) -> tuple:
        """
        특정 날짜 (e.g. 수요일, 이번주, 다음주 등)의
        날씨를 검색하고 조합합니다.

        :param location: 지역
        :return: 오늘 날씨
        """
       # print(date)
        result_dict = LEDSearcher().pass_data(room,date,object, do)
       # print(result_dict)
        result = LEDEditor().edit_LED(result_dict)
       # print('마지막 값:'+LEDAnswerer().LED_form(result))
        return LEDAnswerer().LED_form(result)
