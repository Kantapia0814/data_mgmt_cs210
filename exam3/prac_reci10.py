import pandas as pd
import numpy as np

diabetes = pd.read_csv("pimaIndiansDiabetes.csv")

# 1 - BMI를 기준으로 4개 그룹으로 나누기 (0~3)
bins = [0, 18.5, 25, 30, np.inf]
labels = [0, 1, 2, 3]
diabetes['BMI_Group'] = pd.cut(diabetes['BMI'], bins=bins, labels=labels).astype(int)

# 2 - Age를 3개 그룹으로 나누기 (0~2)
q1 = np.percentile(diabetes['Age'], 40)
q2 = np.percentile(diabetes['Age'], 90)

def group_age(age):
    if age <= q1:
        return 0
    elif age <= q2:
        return 1
    else:
        return 2

diabetes['Age_Group'] = diabetes['Age'].apply(group_age)

# 3 - 이상치(outliers) 제거
def remove_outliers(df, col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    return df[(df[col] >= Q1 - 1.5 * IQR) & (df[col] <= Q3 + 1.5 * IQR)]

for col in ['Glucose', 'SkinThickness', 'Insulin']:
    diabetes = remove_outliers(diabetes, col)

# 4 - Insulin 컬럼에 Min-Max 정규화 적용
insulin_min = diabetes['Insulin'].min()
insulin_max = diabetes['Insulin'].max()

diabetes['Insulin_Scaled'] = (diabetes['Insulin'] - insulin_min) / (insulin_max - insulin_min)

# 5 - BloodPressure의 NaN 값을 그룹별 평균으로 채우기
diabetes['BloodPressure'] = diabetes.groupby('Age_Group')['BloodPressure'].transform(
    lambda x: x.fillna(x.mean())
)