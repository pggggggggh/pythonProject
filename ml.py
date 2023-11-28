import numpy
import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

# 더미 데이터 생성, 실제로는 CSV 파일로부터 읽어온 데이터를 numpy 배열로 변환하여 사용
data = np.loadtxt('data.csv',delimiter=',')

# 독립 변수와 종속 변수 분리
parameters = data[:, :6]  # krw부터 threshold까지
hpr = data[:, 6]   # hpr
mdd = data[:, 7]   # mdd

# 데이터를 학습 세트와 테스트 세트로 분할
rs = 45
train_input, test_input, train_target, test_target = train_test_split(parameters, hpr, test_size=0.2, random_state=rs)

poly = PolynomialFeatures(degree=6,include_bias=False)
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

model_hpr = Ridge()
model_hpr.fit(train_scaled,train_target)

print(model_hpr.score(test_scaled,test_target))

train_input, test_input, train_target, test_target = train_test_split(parameters, mdd, test_size=0.2, random_state=rs)

poly2 = PolynomialFeatures(degree=5,include_bias=False)
poly2.fit(train_input)
train_poly = poly2.transform(train_input)
test_poly = poly2.transform(test_input)

ss2 = StandardScaler()
ss2.fit(train_poly)
train_scaled = ss2.transform(train_poly)
test_scaled = ss2.transform(test_poly)

model_mdd = Ridge()
model_mdd.fit(train_scaled,train_target)

print(model_mdd.score(test_scaled,test_target))

lst = [x/100 for x in range(101)]
lst_thr = [x/20 for x in range(10)]
mx_val = []
mx_hpr = 0

for threshold in lst_thr:
    for krw in lst:
      for ada in lst:
        for eth in lst:
          for doge in lst:
            btc = 1-(krw+ada+eth+doge)
            if btc<0:
              continue

            now_input = np.array([krw,btc,eth,doge,ada,threshold]).reshape(1,-1)
            now_poly = poly.transform(now_input)
            now_scaled = ss.transform(now_poly)
            hpr = model_hpr.predict(now_scaled)[0]

            now_poly = poly2.transform(now_input)
            now_scaled = ss2.transform(now_poly)
            mdd = model_mdd.predict(now_scaled)[0]

            if mdd > 0.14:
              continue
            if hpr > mx_hpr:
              mx_hpr = hpr
              mx_val = [krw,btc,eth,doge,ada,threshold]
              print(f'HPR={mx_hpr*100:.1f}, MDR={mdd*100:.1f}')
              print(mx_val)