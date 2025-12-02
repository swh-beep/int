# 3단계 구조: 공간 -> 스타일 -> 번호 (1-10)
ROOM_STYLES = {
    "Living room": [
        "French-modern",
        "Luxury",
        "Mid-Century",
        "Modern",
        "Natural",
        "Oriental",
        "Scandinavian", # [수정] Scandinavia -> Scandinavian
        "Unique"
    ],
    "Dining room": [
        "French-modern",
        "Luxury",
        "Mid-Century",
        "Modern",
        "Natural",
        "Oriental",
        "Scandinavian", # [수정]
        "Unique"
    ],
    "Bedroom": [
        "French-modern",
        "Luxury",
        "Mid-Century",
        "Modern",
        "Natural",
        "Oriental",
        "Scandinavian", # [수정]
        "Unique"
    ]
}

# 하위 호환성을 위한 기존 STYLES (더 이상 사용하지 않지만 유지)
STYLES = {
    "French-modern": {
        "prompt": "",
        "furniture_specs": {}
    },
    "Luxury": {
        "prompt": "",
        "furniture_specs": {}
    },
    "Mid-Century": {
        "prompt": "",
        "furniture_specs": {}
    },
    "Modern": {
        "prompt": "",
        "furniture_specs": {}
    },
    "Natural": {
        "prompt": "",
        "furniture_specs": {}
    },
    "Oriental": {
        "prompt": "",
        "furniture_specs": {}
    },
    "Scandinavian": { # [수정] 키 값 변경
        "prompt": "",
        "furniture_specs": {}
    },
    "Unique": {
        "prompt": "",
        "furniture_specs": {}
    }
}