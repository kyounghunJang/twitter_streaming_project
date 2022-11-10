
# ELK Stack을 사용한 twitter 실시간 데이터 감정분석 Keyword:날씨
------------
## 프로젝트 계획이유

#### 『엘라스틱 스택 개발부터 운영까지』 책을 통해서 알게 된 ELK stack에 대한 개념과 책에 있던 실습내용들을 종합해서 파이프라인을 만들어보면서 나의 ELK stack에 대한 이해와 활용 능력을 향상시키고 싶어서 프로젝트를 시작하게 되었다. 

------------
## 데이터 파이프라인 구성

![파이프라인 구성 이미지](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2Fcoz0RT%2FbtrQPeHYcp9%2Fc4GC0Y0Ymk8gKcvzN87vKk%2Fimg.png)

#### 위의 그림과 같이 twitter streaming을 python을 통해 filebeat로 보낸 후 logstash에서 전처리를 한 후 elasticsearch에 저장하고 kibana로 시각화를 하는 파이프라인을 구성했다.

-------------

## 실행 방법

1. docker compose up 명령어로 컨테이너를 생성  
2. python 컨테이너에서 deploy_model script를 실행시켜 머신러닝 모델을 적용시켜준다 (script 파일 위치는 /usr/share/script/deploy_model.py)  
3. elasticsearch/config/ingest_pipeline_processors.json에 있는 process를 kibana console ingest pipeline에 적용시켜 준다
4. python 컨테이너에 있는 send_data.py 스크립트를 실행시킨다 (twitter api bearer key 입력 필요)  
5. dashboard 제작

