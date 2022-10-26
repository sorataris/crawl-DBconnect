from kocrawl.answerer.PDLC_answerer import PDLCAnswerer
from kocrawl.base import BaseCrawler
from kocrawl.editor.PDLC_editor import PDLCEditor
from kocrawl.searcher.PDLC_searcher import PDLCSearcher


class PDLCCrawler(BaseCrawler):

    def request(self, date:str,object: str, do: str):
        """

        (try-catch로 에러가 나지 않는 함수)

        :param location: 지역
        :param date: 날짜
        :return: 만들어진진 문장
       """

        try:
           # print(self.request_debug(object, do))
            return self.request_debug(date,object, do)

        except Exception:
            return PDLCAnswerer().sorry(
                '그 장치 상태는 알 수가 없어요.'
            )

    def request_dict(self,date:str, object: str, do: str):
        """

        (try-catch로 에러가 나지 않는 함수)

        :param location: 지역
        :param date: 날짜
        :return: 만들어진진 문장
       """

        try:
            return self.request_debug(date,object, do)
        except Exception:
            return PDLCAnswerer().sorry(
                '그 장치는 알 수가 없어요.'
            )

    def request_debug(self,date:str, object: str, do: str):
        """

        (에러가 나는 디버깅용 함수)

        :param location: 지역
        :param date: 날짜
        :return: 만들어진진 문장
        """



        return self.PDLC_specific(date,object, do)


#__Specific == window
    def PDLC_specific(self, date:str,object: str, do: str) -> tuple:
        """

        :param object: 장치
        :do: on/OFF ...
        :return: edit된 dict
        """

        result_dict = PDLCSearcher().pass_data(date,object, do)
        print(result_dict)
        result = PDLCEditor().edit_PDLC(result_dict)
        return PDLCAnswerer().PDLC_form(result)
