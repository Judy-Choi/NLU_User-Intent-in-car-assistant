# User Intent in Car
## Idea
In-Vehicle Voice User Interface 에서의 사용자 니즈 및 발화 특징 탐색 연구 (서울대 UX랩 논문)   
- 실험으로 수집한 943개 발화를 41개 Intent에 따라 분류   
## Dataset
A New Multi-Turn, Multi-Domain, Task-Oriented Dialogue Dataset   
- https://nlp.stanford.edu/blog/a-new-multi-turn-multi-domain-task-oriented-dialogue-dataset/   
- 3개의 Intent (navigate, schedule, weather) 를 갖는 3,031 개의 multi-turn 대화 데이터셋   
- 1개의 Dialogue 당 1 ~ 4 개의 driver - assistant turn 대화 보유   
   - Download Link : http://nlp.stanford.edu/projects/kvret/kvret_dataset_public.zip

## Preprocessing
1. 각 Intent 별로 Dialogue 의 첫번째 발화만 추출
- driver 의 첫번째 발화가 가장 intent 가 명확하게 드러나므로)
2. Papago 높임말 번역
- 번역 결과 파일
   - dev + train + test set
   - 중복 문장 제거
   
## Intent Dataset
### Domain Intent (Major 3 Intent, 1880 utterances (중복 제거))
<img width="431" alt="image" src="https://user-images.githubusercontent.com/53294075/220805570-87e3a526-7890-438f-b1ac-356bfce87a72.png">

- 길 찾기
   - navigate.csv  (536 utterances)
- 날씨
   - weather.csv (525 utterances)
- 스케줄
   - schedule.csv (819 utterances)

### Sub Intent
- 길 찾기
   - 주소, 위치 찾기
      - sub_navigate_1.csv (322 utterances)
   - 경로 찾기
      - sub_navigate_2.csv (214 utterances)
- 날씨
   - 일기예보 확인 (일기예보 단순 조회, 더울까요/따뜻할까요)
      - sub_weather_1.csv (195 utterances)
   - 날씨 확인 (흐림, 맑음, 비, 눈, 우박, 기온)
      - sub_weather_2.csv (330 utterances)
- 스케줄
   - 일정 추가
      - sub_schedule_1.csv (252 utterances)
   - 알림 설정
      - sub_schedule_2.csv (177 utterances)
   - 일정 확인
      - sub_schedule_3.csv (390 utterances)
      
## SVM Code
- Domain Intent SVM 분류 코드
   - SVM - Domain Intent.ipynb
- Sub Intent SVM 분류 코드
   - sub-intent_navigate.ipynb
   - sub-intent_weather.ipynb
   - sub-intent_schedule.ipynb

## Web Demo Code (Flask)
- intent.py (Domain Intent, Sub Intent 분류하는 코드)
   - Domain Intent - SVM 분류 결과
      - model_domain_pipeline.joblib
   - Sub Intent - SVM 분류 결과
      - model_navigate.joblib
      - model_weather.joblib
      - model_schedule.joblib
   - main.py (Flask code)
   - templates\session.html (웹페이지 html 코드)
