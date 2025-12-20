import logging
import re
from typing import Any, Optional

import unidecode

from config.job_map import JOB_MAP
from config.stopwords import STOPWORDS

import pandas as pd

logger = logging.getLogger(__name__)

NUM_EXPR = r'(\d+(?:\.\d+)?)'
SPACES_EXPR = r'\s*'
UNIT_EXPR = r'(triệu|tr|vnd|vnđ|usd|\$|usd\/month)'

def extract_salary_info(value: Optional[str]) -> dict[str, Any]:
    """
    Normalize salary string into structured numeric data.
    Returns:
        {
            "num": Optional[float],
            "min": Optional[float],
            "max": Optional[float],
            "unit": Optional["VND" | "USD"]
        }
    """
    result: dict[str, Optional[Any]] = {
        "num": None,
        "min": None,
        "max": None,
        "unit": None,
    }

    if not value:
        return result

    try:
        text = value.replace(",", "").lower().strip()

        # ---------- detect unit ----------
        unit = "USD" if ("usd" in text or "$" in text) else "VND"
        result["unit"] = unit

        # ---------- thỏa thuận ----------
        if "thoả thuận" in text or "thỏa thuận" in text:
            return result

        # ---------- range: X - Y ----------
        range_expr = rf'{NUM_EXPR}{SPACES_EXPR}[-~]{SPACES_EXPR}{NUM_EXPR}'
        m = re.search(range_expr, text)
        if m:
            lo, hi = float(m.group(1)), float(m.group(2))
            result.update(
                num=(lo + hi) / 2,
                min=lo,
                max=hi,
            )
            return result

        # ---------- above: trên X ----------
        above_expr = rf'(trên|tren|từ|tu|tối thiểu|toi thieu){SPACES_EXPR}{NUM_EXPR}'
        m = re.search(above_expr, text)
        if m:
            val = float(m.group(2))
            result.update(num=val, min=val)
            return result

        # ---------- to: tới X ----------
        to_expr = rf'(tới|toi){SPACES_EXPR}{NUM_EXPR}'
        m = re.search(to_expr, text)
        if m:
            val = float(m.group(2))
            result.update(num=val, max=val)
            return result

        # ---------- single number ----------
        single_expr = rf'{NUM_EXPR}'
        m = re.search(single_expr, text)
        if m:
            val = float(m.group(1))
            result.update(num=val, min=val, max=val)
            return result

    except Exception as e:
        logger.warning(f"Failed to parse salary '{value}': {e}")

    return result

def parse_address(value):
    if value is None or pd.isna(value):
        logger.warning(f'Address value {value} is empty')
        return {'city': None, 'district': None}

    if not isinstance(value, str):
        logger.warning(f'Address value {value} is not a string')
        return {'city': None, 'district': None}

    address = []
    elems = value.split(': ')

    try:
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
    except Exception as e:
        logger.warning(f'Failed to parse address: {value}')

    return address

def clean_title_vi(title):
    if not isinstance(title, str):
        return ''
    t = title.lower()
    try:
        # remove vi
        t = unidecode.unidecode(t)
        # remove stopwords
        for w in STOPWORDS:
            t = t.replace(w, ' ')

        t = re.sub(r'\s+', ' ', t).strip()
    except Exception as e:
        logger.warning(f'Failed to parse title: {title}')

    return t

def classify_job_group(title: str):
    t = clean_title_vi(title)
    # print(title, ' - ', t)

    for group, keywords in JOB_MAP.items():
        for kw in keywords:
            if kw in t:
                return group

    return 'other'
