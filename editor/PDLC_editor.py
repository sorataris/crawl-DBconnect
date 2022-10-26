from kocrawl.editor.base_editor import BaseEditor
import re
from kocrawl.editor.edit_date import Edit_date

class PDLCEditor(BaseEditor):


    def edit_PDLC(self, result: dict) -> dict:
        """
        딕셔너리를 수정합니다.

        :param result: 입력 딕셔너리
        :return: 수정된 딕셔너리
        """
        fix_OP = self.PDLC[result['OP']]
        fix_object = self.PDLC[result['object']]
        fix_date = Edit_date.act_date(result['date'])

        result = {
                  'date': fix_date,
                  'object': fix_object,
                  'OP': fix_OP
                  }

        return result
