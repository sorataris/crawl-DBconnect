from kocrawl.searcher.base_searcher import BaseSearcher
import re


class WeatherSearcher(BaseSearcher):
   # 'naver_weather': '.info_data > .info_list > li > .cast_txt',
    #'naver_temperature': '.info_temperature > .todaytemp',
    def __init__(self):
        #셀렉터 정의
        #따로따로 정의 시도
        self.CSS = {
            # div > li.week_item > div > div.cell_temperature > span
            # 검색에 사용할 CSS 셀렉터들을 정의합니다.
            'naver_weather': 'div > div.cell_weather > span > i > span.blind',
            'naver_temperature_low': 'div > div.cell_temperature > span > span.lowest',
            'naver_temperature_high': 'div > div.cell_temperature > span > span.highest',
            'naver_temperature_today_up': 'div > div.weather_info > div > div._today > div.temperature_info > p > span.temperature',
            'naver_temperature_today_up_text': 'div > div.weather_info > div > div._today > div.temperature_info > p > span.temperature > span',
            'naver_percent': 'div > div.cell_weather > span > span > span',
            'google_weather': '#wob_dcp > #wob_dc',
            'google_temperature': '#wob_tm'
        }
# 'today_weather': None,
  #          'tomorrow_morning_weather': None,
  #          'tomorrow_afternoon_weather': None,
    #        'after_morning_weather': None,
     #       'after_afternoon_weather': None,
      #      'specific_weather': None,
       #     'today_temperature': None,
        #    'tomorrow_morning_temperature': None,
         #   'tomorrow_afternoon_temperature': None,
          #  'after_morning_temperature': None,
           # 'after_afternoon_temperature': None,
          #  'specific_temperature': None,


        self.data_dict = {
            # 데이터를 담을 딕셔너리 구조를 정의합니다.
            'today_weather': None,
            'tomorrow_morning_weather': None,
            'tomorrow_afternoon_weather': None,
            'after_morning_weather': None,
            'after_afternoon_weather': None,
            'specific_weather': None,
            'today_temperature': None,
            'tomorrow_morning_temperature': None,
            'tomorrow_afternoon_temperature': None,
            'after_morning_temperature': None,
            'after_afternoon_temperature': None,
            'compare_temperature': None, #비교문
            'specific_temperature': None,
            'today_percent_morning': None,
            'today_percent_afternoon': None,
            'tomorrow_percent_morning': None,
            'tomorrow_percent_afternoon': None,
            'after_percent_morning' : None,
            'after_percent_afternoon': None,

        }

    def _make_query(self, location: str, date: str) -> str:
        """
        검색할 쿼리를 만듭니다.
        
        :param location: 지역
        :param date: 날짜
        :return: "지역 날짜 날씨"로 만들어진 쿼리
        """

        return ' '.join([location, date, '날씨'])

#오늘 내일 검색시 사용
    def naver_search(self, location: str) -> dict:
        """
        네이버를 이용해 날씨를 검색합니다.

        :param location: 지역
        :return: 크롤링된 내용
        """
#result에서 에러가나는 것 같음
        query = self._make_query('오늘', location)  # 한번 서치에 전부 가져옴
        #content는 base_searcher에서 정의되어있음
        #셀렉터 정의부분
        result = self._bs4_contents(self.url['naver'],
                                    selectors=[
                                               self.CSS['naver_temperature_today_up'],
                                               self.CSS['naver_temperature_today_up_text'],
                                               self.CSS['naver_weather'],
                                               self.CSS['naver_temperature_low'],
                                               self.CSS['naver_temperature_high'],
                                               self.CSS['naver_percent']
                                               ],
                                    query=query)

        #[[<span class="blind">최고기온</span>, '27°'], [<span class="blind">최고기온</span>, '31°'], [<span class="blind">최고기온</span>, '31°'],
       # print('네이버')
       # print(query)
        #print(result0)
      #  result = [[result0[0][0]],[result0[1][1]]]
       # print(result)
        #print(result)

        # 리스트 선언
        resultk=[]
        
        for i in range(17):
            resultk.append([])
            for j in range(1):
                resultk[i].append(0)

#오늘 온도, 내일 오전 온도,내일 오후 온도, 모레 오전 온도 , 모레 오후 온도 , 특정요일 온도
        #날씨후 온도
#[['흐리고 가끔 소나기'], ['흐림'], ['흐리고 비'], ['흐리고 한때 비'], ['맑음'], ['none'], ['25°'], ['27°'], ['25°'], ['23°'], ['23°'], ['none']]
        resultk[0][0] = result[2][0] #오늘 오후 날씨
        resultk[1][0] = result[4][0] #내일 오전 날씨
        resultk[2][0] = result[5][0] #내일 오후 날씨
        resultk[3][0] = result[6][0] #모레 오전 날씨
        resultk[4][0] = result[7][0] #모레 오후 날씨
        #resultk[5][0] = 'none' #특정 요일은 none
#42부터 습도
        resultk[5][0] = result[32][1]  # 오늘 최고온도
        resultk[6][0] = result[23][1]  # 내일 최저온도
        resultk[7][0] = result[33][1]  # 내일 최고온도
        resultk[8][0] = result[24][1]  # 모레 최저온도
        resultk[9][0] = result[34][1]  # 모레 최고온도
        resultk[10][0] = result[0][0] + result[1][0]  # 비교된 문
        resultk[11][0] = result[42][0] #오늘 오전 강수확률
        resultk[12][0] = result[43][0]  # 오늘 오후 강수확률
        resultk[13][0] = result[44][0] #내일  오전 강수확률
        resultk[14][0] = result[45][0]  # 내일  오후 강수확률
        resultk[15][0] = result[46][0] # 모레 오전 강수확률
        resultk[16][0] = result[47][0]  # 모레 오후 강수확률
       # resultk[10][0] = 'none'  # 특정요일 none

        #print(resultk)

        i = 0

      #  print(self.data_dict.keys())
#'today_weather', 'tomorrow_morning_weather', 'tomorrow_afternoon_weather', 'after_morning_weather', 'after_afternoon_weather',
 #'specific_weather', 'today_temperature', 'tomorrow_morning_temperature', 'tomorrow_afternoon_temperature',
 #'after_morning_temperature', 'after_afternoon_temperature', 'specific_temperature'])
#대충 오늘,내일 날씨나 온도같다
#K는 대강 12개다
        #NOT SPECIFIC
        # 'today_weather', 'tomorrow_morning_weather', 'tomorrow_afternoon_weather', 'after_morning_weather', 'after_afternoon_weather',
        # 'today_temperature', 'tomorrow_morning_temperature', 'tomorrow_afternoon_temperature', 'after_morning_temperature', 'after_afternoon_temperature'])
#오늘 내일(오전)(오후) 모레(오전)(오후) 데이터를 받음 따라서 총 10개

        #specific을 제외하면 10번 반복
        #아마 하나의 날씨가 아니라 주간날씨로 들여보내나 보다...주간 날씨로 크롤링해보자
        for k in self.data_dict.keys():
            if 'specific' not in k:
                # specific(요일) 빼고 전부 담음
                self.data_dict[k] = re.sub(' ', '', resultk[i][0])
                i += 1

        return self.data_dict

    def google_search(self, location: str, date: str) -> dict:
        """
        구글을 이용해 날씨를 검색합니다.

        :param location: 지역
        :param date: 날짜
        :return: 크롤링된 내용
        """

        query = self._make_query(location, date)  # 날짜마다 따로 가져와야함
        result = self._bs4_contents(self.url['google'],
                                    selectors=[self.CSS['google_weather'],
                                               self.CSS['google_temperature']],
                                    query=query)
      #  print('구글')
       # print('쿼리문'+query)
      #  print('결과문')
        print(result)
        #[['강우(천둥, 번개 동반)'], ['30']] 디버깅 결과 상태 이차원 배열 리스트로 출력됨.
        self.data_dict['specific_weather'] = re.sub(' ', '', result[0][0])
        self.data_dict['specific_temperature'] = re.sub(' ', '', result[1][0])
        # specific만 담음

        return self.data_dict
