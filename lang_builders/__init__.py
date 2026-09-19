"""Language builder registry."""
from __future__ import annotations

from .de import build as build_de
from .es import build as build_es
from .fr import build as build_fr
from .it import build as build_it
from .ja import build as build_ja
from .ko import build as build_ko
from .pl import build as build_pl
from .pt import build as build_pt
from .ru import build as build_ru
from .tr import build as build_tr
from .zh import build as build_zh

BUILDERS = {
    "ru": build_ru,
    "es": build_es,
    "de": build_de,
    "fr": build_fr,
    "it": build_it,
    "pt": build_pt,
    "pl": build_pl,
    "zh": build_zh,
    "ja": build_ja,
    "ko": build_ko,
    "tr": build_tr,
}
