import re
from typing import Any

import unidecode

from config.job_map import JOB_MAP
from config.stopwords import STOPWORDS

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

def parse_address(value):
    if not value:
        return []

    address = []
    elems = value.split(': ')

    for special_loc in ['Nước Ngoài', 'Toàn Quốc' ]:
        if special_loc in elems:
            address.append({'city': special_loc})
            elems.remove(special_loc)

    for i in range(0, len(elems), 2):
        # If district may exist
        if (len(elems) - i) > 1:
            address.append({'city': elems[i],
                            'district': elems[i + 1]})
        else:
            address.append({'city': elems[i]})

    return address

def clean_title_vi(title):
    if not isinstance(title, str):
        return ''
    t = title.lower()

    # remove vi
    t = unidecode.unidecode(t)
    # remove stopwords
    for w in STOPWORDS:
        t = t.replace(w, ' ')

    t = re.sub(r'\s+', ' ', t).strip()
    return t

def classify_job_group(title):
    t = clean_title_vi(title)
    # print(title, ' - ', t)

    for group, keywords in JOB_MAP.items():
        for kw in keywords:
            if kw in t:
                return group

    return 'other'
