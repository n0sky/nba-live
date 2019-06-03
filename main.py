import zhibo8_api
import argparse

def get_ended_matches():
    matches = zhibo8_api.get_ended_matches()
    for match in matches:
        print(match)
    return

def get_living_matches():
    matches = zhibo8_api.get_living_matches()
    for match in matches:
        print(match)
    return matches


def get_watch_match(matches):
    match_id = input('请输入比赛ID：')
    for match in matches:
        if match.id == match_id:
            return match
    else:
        print('输入的ID不正确')
        return None

def parse_args():
    parser = argparse.ArgumentParser(description='nba_live')
    parser.add_argument('-l', '--list', action='store_true', help='显示已结束比赛')
    args = parser.parse_args()
    return args

def main_loop():
    args = parse_args()
    matches = get_living_matches()

    if args.list:
        get_ended_matches()
        return

    if len(matches) == 0:
        print('当前没有比赛！！！')
        return

    match = get_watch_match(matches)
    if not match:
        print('没去找到该比赛')
        return

    current_match_max_sid = -1
    while True:
        match_max_sid = zhibo8_api.get_match_max_sid(match.id)
        if not match_max_sid:
            print('没有直播数据')
            return
            
        if current_match_max_sid == match_max_sid:
            continue

        current_match_max_sid = match_max_sid
        text_livings = zhibo8_api.get_match_living(match.id, current_match_max_sid)
        for text in text_livings:
            print(text)


if __name__ == '__main__':
    main_loop()
    