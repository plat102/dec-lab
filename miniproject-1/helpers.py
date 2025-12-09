import re
from typing import Any

def extract_salary_info(value: str) -> dict[str, Any]:
    if value is None:
        return {}

    # ----- Clean -----
    text_clean = value.replace(',', '').strip().lower()

    # ----- Detect currency -----
    unit = 'USD' if ('usd' in text_clean or '$' in text_clean) \
                else 'VND'

    # ----- Match specific cases -----
    num_expr = r'(\d+(?:\.\d+)?)'
    char_expr = r'(\d+)'
    spaces_expr = r'\s*'
    unit_expr = r'(?:\s*(triệu|vnđ|vnd|usd|$|usd\/month))?'

    # "thoa thuan"
    if 'thỏa thuận' in text_clean or "thoả thuận" in text_clean:
        return {
            'num': None
        }

    # above: "tren X trieu"
    above_expr = rf'(?:trên|tren|từ|tu|toi thieu|tối thiểu){spaces_expr}{num_expr}'
    above_match = re.findall(above_expr, text_clean)
    if len(above_match) > 0:
        return {
            'num': float(above_match[0]),
            'min': float(above_match[0]),
            'max': None,
            'unit': unit,
        }

    # range: "X-Y trieu"
    range_expr = rf'.*?{num_expr}{spaces_expr}[-~]{spaces_expr}{num_expr}{unit_expr}'
    range_match = re.findall(range_expr, text_clean)
    # print(range_match)
    if range_match:
        lo, hi, _ = range_match[0]
        return {
            'num': (float(lo) + float(hi))/ 2,
            'min': float(lo),
            'max': float(hi),
            'unit': unit,
        }

    # to:"toi X trieu"
    to_expr = rf'(?:tới){spaces_expr}{num_expr}'
    to_match = re.findall(to_expr, text_clean)
    if len(to_match) > 0:
        return {
            'num': float(to_match[0]),
            'min': None,
            'max': float(to_match[0]),
            'unit': unit,
        }

    # one num: "X trieu"
    one_num = re.findall(rf'{num_expr}{unit_expr}', text_clean)
    if len(one_num) > 0:
        num, unit = one_num[0]
        return {
            'num': float(num),
            'min': float(num),
            'max': float(num),
            'unit': unit,
        }

    return {'num': None, "min": None, "max": None, "unit": None}

