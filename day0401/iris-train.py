from sklearn import svm,metrics
import random,re

# 붓꽃의 csv 데이터 읽어 들이기
csv = []
with open('iris.csv','r',encoding='utf-8') as fp:
    # 한줄씩 읽어 들이기
    for line in fp:
        line = line.strip() # 줄바꿈 제거
        cols = line.split(',') # 쉼표로 자르기
        # 문자열 데이터를 숫자로 변환하기
        # 람다식 : 함수가 간단한 경우
        fn = lambda n : float(n) if re.match('^[0-9\.]+$',n) else n
                # 매개변수 n을 전달받아서 if 컨디션(re.match(r'^[0-9\.]+$',n)) 이
                # 참이면 float(n) (숫자로 시작하면 실수로 실행) -> float(n)은 실수

        cols = list(map(fn,cols)) # map이라는 함수가 반복문의 역활을 해준다. / map (함수명, 리스트)
        # map이 다시 list에 담아주는 역활을 하는데 우린 파이썬 3이므로 list를 적어줘야 한다.

        # 17번째 코드를 풀어쓰면 21~24번째 줄
        # rlist = []
        # for c in cols:
        #     temp = fn(c)
        #     rlist.append(temp)

        # print(cols) 데이터를 한줄 씩 읽어옴,

        csv.append(cols)
     # print(csv)  데이터를 2차원 배열에 넣어줌.
     # [['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Name'], [5.1, 3.5, 1.4, 0.2, 'Iris-setosa'],

    # 가장 앞 줄의 헤더 제거
    del csv[0]
    # print(csv) : [[5.1, 3.5, 1.4, 0.2, 'Iris-setosa'], [4.9, 3.0, 1.4, 0.2, 'Iris-setosa'],

    # 데이터 셔플하기(섞기) - 붓꽃의 csv 데이터가 중복되어있으닌까 잘 섞어야 한다.
    random.shuffle(csv)
    # print(csv)

    # 학습전용 데이터와 텍스트 전용 데이터 분할하기(2:1 비율)
    total_len = len(csv)
    train_len = int(total_len * 2/3)
    # print(total_len)  150
    # print(train_len)  100
    train_data = []
    train_label = []
    test_data = []
    test_label = []

    for i in range(total_len):
        data = csv[i][:4]
        label = csv[i][4]
        if i < train_len:
            train_data.append(data)
            train_label.append(label)
        else:
            test_data.append(data)
            test_label.append(label)

    # print(train_data) #훈련시킨 문제 : [[5.7, 3.8, 1.7, 0.3], [4.4, 2.9, 1.4, 0.2],
    # print(train_label) # 훈련시킨 답 : ['Iris-setosa', 'Iris-setosa',


    # 데이터를 학습하고 예측하기
    clf = svm.SVC()
    clf.fit(train_data, train_label)
    pre = clf.predict(test_data)
    # print(pre) # 예측
    # print(test_label) # 진짜 답

    # 정답구하기
    ac_score = metrics.accuracy_score(test_label,pre)
    print("정답률 : ",ac_score)  # 정답률 :  0.98