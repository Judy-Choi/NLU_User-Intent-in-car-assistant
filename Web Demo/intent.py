from sklearn.externals import joblib

def intent(str):

    intent_major = joblib.load('model_domain_pipeline.joblib')
    intent = intent_major.predict([str])

    if intent == 1:

        print("Intent : Navigate")
        intent_navigate = joblib.load('model_navigate.joblib')
        sub_intent = intent_navigate.predict([str])
        if sub_intent == 1:
            print("sub intent : 주소/위치 찾기")
            return "주소/위치를 탐색합니다."
        else:
            print("sub intent : 경로 찾기")
            return "경로를 탐색합니다."

    elif intent == 2:

        print("Intent : Weather")
        intent_weather = joblib.load('model_weather.joblib')
        sub_intent = intent_weather.predict([str])
        if sub_intent == 1:
            # 1. 일기예보 확인 (일기예보 단순 조회, 더울까요/따뜻할까요)
            print("sub intent : 일기예보 조회")
            return "일기예보를 조회합니다."
        else:
            # 2. 날씨 확인 (흐림, 맑음, 비, 눈, 우박, 기온)
            print("sub intent : 날씨 확인")
            return "날씨를 확인합니다."

    else:
        print("Intent : Schedule")
        intent_schedule = joblib.load('model_schedule.joblib')
        sub_intent = intent_schedule.predict([str])
        if sub_intent == 1:
            # 1. 일정 추가
            print("sub intent : 일정 추가")
            return "지정한 일정을 추가합니다."
        elif sub_intent == 2:
            # 2. 알림 설정
            print("sub intent : 알림 설정")
            return "일정에 대한 알림을 설정합니다."
        else:
            # 3. 일정 확인
            print("sub intent : 일정 확인")
            return "일정을 확인합니다."