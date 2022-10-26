import json
import urllib
from abc import ABCMeta, abstractmethod
from urllib.request import urlopen, Request

import bs4
import requests

from kocrawl.base import BaseCrawler
from kocrawl.decorators import searcher


@searcher
class BaseSearcher(BaseCrawler, metaclass=ABCMeta):

    @abstractmethod
    def _make_query(self, *args, **kwargs):
        raise NotImplementedError

    def __bs4(self, url: str, query: str) -> bs4.BeautifulSoup:
        """
        beautiful soup 4를 이용하여 정적 웹페이지에 대한 크롤링을 시도합니다.

        :param url: 베이스 url
        :param query: 검색할 쿼리
        :return: parsing된 html
        """

        if query:
            url += urllib.parse.quote(query)
       # print(url)
        #url은 이상한 영어지만 연결시 제대로 동작함
        out = bs4.BeautifulSoup(urlopen(Request(url, headers=self.headers)).read(), 'html.parser')

        return out

#wheater_seacher에서 호출
    def _bs4_contents(self, url: str, selectors: list, query: str = ""):
        """
        beautiful soup 4를 이용하여 정적 웹페이지에 대한 크롤링을 시도합니다.
        셀렉터를 적용하여 입력한 셀렉터에 해당하는 태그 안의 contents를 로드합니다.

        :param url: 베이스 url
        :param selectors: 검색할 셀렉터
        :param query: 검색할 쿼리
        :return: 크롤링된 콘텐츠
        """
        #맨위에 있는 함수로 전체 데이터를 받아옴
        out = self.__bs4(url, query)
       # print('bs4에서의 crwaed값')
        #print(out) html이다.
        #실질적인 크롤링 부분
       # print(selectors)
        try:
            crawled = []
            for selector in selectors:
                for s in out.select(selector):
                    crawled.append(s.contents)

            return crawled
        except Exception:
            return None

    def _bs4_documents(self, url: str, selectors: list, query: str = ""):
        """
        beautiful soup 4를 이용하여 정적 웹페이지에 대한 크롤링을 시도합니다.
        셀렉터를 적용하여 입력한 셀렉터에 해당하는 태그를 포함한 모든 document 구조를 로드합니다.

        :param url: 베이스 url
        :param selectors: 검색할 셀렉터
        :param query: 검색할 쿼리
        :return: 크롤링된 콘텐츠
        """

        out = self.__bs4(url, query)
        try:
            crawled = []
            for selector in selectors:
                for s in out.select(selector):
                    crawled.append(s)
            return crawled
        except Exception:
            return None

    def _json(self, url: str, query: str):
        """
        json을 이용하여 동적 웹페이지에 대한 크롤링을 시도합니다.

        :param url: 베이스 url
        :param query: 검색할 쿼리
        :return: 크롤링된 json 파일
        """

        if query:
            url += urllib.parse.quote(query)

        req = requests.get(url, headers=self.headers)
        if req.status_code == requests.codes.ok:
            loaded_data = json.loads(req.text)
            return loaded_data
        else:
            return None
