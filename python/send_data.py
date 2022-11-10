import requests
import os
import json
import logging



def bearer_oauth(r): #twitter api bearer key값 정보
    r.headers["Authorization"] = f"Bearer input your twitter api_v2 bearer key"
    r.headers["User-Agent"] = "v2FilteredStreamPython"
    return r


def get_rules(): #현재 적용되어 있는 rule확인하는 코드
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))
    return response.json()


def delete_all_rules(rules): #모든 Rule을 삭제하여 초기화
    if rules is None or "data" not in rules:
        return None

    ids = list(map(lambda rule: rule["id"], rules["data"]))
    payload = {"delete": {"ids": ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot delete rules (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    print(json.dumps(response.json()))


def set_rules(delete):#새로운 rule 적용 keyword도 적용 
    # You can adjust the rules if needed
    sample_rules = [
        {"value": "날씨 lang:ko"},
    ]
    payload = {"add": sample_rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=payload,
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
        )
    print(json.dumps(response.json()))


def get_stream(set): #twitter api 스트리밍 시작 및 python logger을 사용한 데이터 저장
    mylogger= logging.getLogger()
    mylogger.setLevel(logging.DEBUG)
    myhandler = logging.FileHandler('/usr/share/mylog/data.log',encoding='utf-8')
    mylogger.addHandler(myhandler)
    
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(response.status_code) 
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    while True:
        try:
            for response_line in response.iter_lines():
                if response_line:
                    json_response = json.loads(response_line)
                    par_text=json_response['data']['text'].replace("\n", ' ')
                    mylogger.info(par_text)
                    
        except ChunkedEncodingError:
            continue

def main(): #모든 작업 실행 

    rules = get_rules()
    delete = delete_all_rules(rules)
    set = set_rules(delete)
    get_stream(set)


if __name__ == "__main__":
    main()