character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기","세게 베기","아주 세게 베기"]
}

for key in character:
    if type(character[key]) == dict:
        for small_key in character[key]:
            print(small_key, ":", character[key][small_key])
    elif type(character[key]) == list:
        for small_key in character[key]:
            print(key, ":", small_key)
    else:
        print(key, ":", character[key])