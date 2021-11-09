import json

import requests


async def get_current_song():
    url = "https://air.radioulitka.ru:8083/api/live-info/"
    r = requests.get(url)
    aa = json.dumps(r.text, ensure_ascii=False)
    # regexed_json = re.sub(r"^\S+\bulitka_playlist_callback.",'', aa)
    regexed_json = str(aa[26:])
    sliced_json = str(regexed_json[:-2])

    final_json = sliced_json.replace('\\', '')
    print(final_json)

    data = json.loads(final_json)

    current_song = data["current"]["name"]

    print(current_song)
    return current_song
