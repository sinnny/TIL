
# 다차원 척도법(MDS)
# - 개체들 사이의 유사성, 비유사성을 거리로 측정하여 2차원/3차원 공간상에
#   점으로 표현하는 기법
# - 개체들 사이의 집단화를 시각적으로 표현하는 분석방법
# - 차원 축소과정에서 발생하는 오차(stress) 정의 
# - stress 크기로 차원 축소에 대한 적합도 판단
# - stress(0: 완벽, 5: 좋음, 10: 보통, 20: 나쁨)



from sklearn.manifold import MDS 

# 1. data loading 
from sklearn.datasets import load_iris
iris_x=load_iris()['data']
iris_y=load_iris()['target']

iris_x  # 변수가 4개 -->> 4차원 

# 2. Scailing 정규화
from sklearn.preprocessing import StandardScaler as standard
m_sc=standard()
m_sc.fit_transform(iris_x)
iris_x_sc=m_sc.fit_transform(iris_x)
# PCA 적용 전 스케일링 변환 

m_mds2 = MDS(n_components=2)
m_mds3 = MDS(n_components=3)


#3. 데이터 변환
iris_X_mds1 = m_mds2.fit_transform(iris_x_sc)
iris_X_mds2 = m_mds3.fit_transform(iris_x_sc)


# 4. 유도된 인공변수 확인

m_mds2.stress_  # 235.36041253663842 --> 접합도 평가(.stress_)
m_mds2.embedding_  # 변환된 데이터셋 


# 변환된 데이터 셋 값 --> points 변수에 담기
points = m_mds2.embedding_

# 5. 크루스칼 스트레스 계산

import numpy as np
from sklearn.metrics import euclidean_distances

DE = euclidean_distances(points)
DA = euclidean_distances(iris_x)         #  실제 거

stress = 0.5*np.sum((DE-DA)**2)
stress1 = np.sqrt(stress/(0.5*np.sum(DA**2)))
stress1


m_mds3.stress_
points = m_mds3.embedding_



# 크루스탈 스트레스 개선
import numpy as np
from sklearn.metrics import euclidean_distances

DE = euclidean_distances(points)
DA = euclidean_distances(iris_x)         #  실제 거

stress = 0.5*np.sum((DE-DA)**2)
stress2 = np.sqrt(stress/(0.5*np.sum(DA**2)))
stress2     #  0.1856225180251546



m_mds3







