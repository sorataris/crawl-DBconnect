from kocrawl.editor.base_editor import BaseEditor
from kocrawl.editor.edit_date import Edit_date
import re


class LEDEditor(BaseEditor):


    def edit_LED(self, result: dict) -> dict:
        """
        딕셔너리를 수정합니다.

        :param result: 입력 딕셔너리
        :return: 수정된 딕셔너리
        """
        fix_OP = self.LED[result['OP']]
        fix_object = self.LED[result['object']]
        fix_room = self.room[result['room']]
        fix_date = Edit_date.act_date(result['date'])
        result = {'object': fix_object,
                  'OP': fix_OP,
                  'date': fix_date,
                  'room':fix_room
                  }

        return result
