from kocrawl.editor.base_editor import BaseEditor
import re


class WeatherEditor(BaseEditor):

    def edit_today(self, result: dict) -> dict:
        """
        오늘 날씨 딕셔너리를 수정합니다.

        :param result: 입력 딕셔너리
        :return: 수정된 딕셔너리
        """
       # print('에디터 창의 결과')
       # print(result)
        weather = self.weather[result['today_weather'].split(',')[0].strip()]
        comparison = result['compare_temperature']
        temperature = result['today_temperature']
        percent_morning = result['today_percent_morning']
        percent_afternoon = result['today_percent_afternoon']
        result = {'weather': weather,
                  'comparison': comparison,
                  'temperature': temperature,
                  'percent_morning' : percent_morning,
                  'percent_afternoon': percent_afternoon,
                  }
        #print('result 결과값')
       # print(result)
        return result

    def edit_tomorrow(self, result: dict) -> tuple:
        """
        내일 날씨 딕셔너리를 수정합니다.

        :param result: 입력 딕셔너리
        :return: 수정된 딕셔너리
        """
#맨 위에가 config에서 문장을 바꾸는 것 같다.
        morning_weather = self.weather[result['tomorrow_morning_weather']]
        afternoon_weather = self.weather[result['tomorrow_afternoon_weather']]
        morning_temperature = result['tomorrow_morning_temperature']
        afternoon_temperature = result['tomorrow_afternoon_temperature']
        percent_morning = result['tomorrow_percent_morning']
        percent_afternoon = result['tomorrow_percent_afternoon']
        josa = self.enumerate_josa('는', '도', [morning_weather, afternoon_weather])
        print('조사')
        print(morning_weather)
        print(result['tomorrow_morning_weather'])
        result = {'morning_weather': morning_weather,
                  'afternoon_weather': afternoon_weather,
                  'morning_temperature': morning_temperature,
                  'afternoon_temperature': afternoon_temperature,
                  'percent_morning' : percent_morning,
                  'percent_afternoon': percent_afternoon,
                  }

        return result, josa

    def edit_after(self, result: dict) -> tuple:
        """
        모레 날씨 딕셔너리를 수정합니다.

        :param result: 입력 딕셔너리
        :return: 수정된 딕셔너리
        """

        morning_weather = self.weather[result['after_morning_weather']]
        afternoon_weather = self.weather[result['after_afternoon_weather']]
        morning_temperature = result['after_morning_temperature']
        afternoon_temperature = result['after_afternoon_temperature']
        percent_morning = result['after_percent_morning']
        percent_afternoon = result['after_percent_afternoon']
        josa = self.enumerate_josa('는', '도', [morning_weather, afternoon_weather])

        result = {'morning_weather': morning_weather,
                  'afternoon_weather': afternoon_weather,
                  'morning_temperature': morning_temperature,
                  'afternoon_temperature': afternoon_temperature,
                  'percent_morning' : percent_morning,
                  'percent_afternoon': percent_afternoon,
                  }

        return result, josa

    def edit_specific(self, result: dict) -> dict:
        """
        특정 날짜 딕셔너리를 수정합니다.

        :param result: 입력 딕셔너리
        :return: 수정된 딕셔너리
        """

        weather = self.weather[re.sub(' ', '', result['specific_weather'])]
        temperature = result['specific_temperature']

        result = {'weather': weather,
                  'temperature': temperature}
        print('구글 에디터')
        print(result)
        return result
