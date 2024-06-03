import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 設置Matplotlib顯示中文字體
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 使用微軟正黑體
plt.rcParams['axes.unicode_minus'] = False  # 解決負號顯示問題

# 檔案路徑
file_path = 'D:\q\data1.csv'

data = pd.read_csv(file_path, skipinitialspace=True)

# 成績與家庭關係之間的關聯
# 需要的欄位
grades_and_family = data[['achieve', 'parent1', 'parent2',
'parent3', 'parent4', 'parent5', 'parent6', 'parent7',
'parent8', 'parent9', 'parent10']]

# 計算家庭關係的平均值
mean_family_relations = grades_and_family.mean(axis=1)

# 將成績和家庭關係的平均值合併成一個 DataFrame
combined_data = pd.concat([data['achieve'], mean_family_relations], axis=1)
combined_data.columns = ['成績', '家庭關係平均值']

# 繪製盒狀圖
sns.boxplot(x='成績', y='家庭關係平均值', data=combined_data)
plt.title('成績與家庭關係平均值之間的關聯')
plt.xlabel('成績')
plt.ylabel('家庭關係平均值')
plt.grid(True)
plt.show()

# 網路使用時數與對老師的看法之間的關聯
# 選擇需要的欄位
internet_hours_and_teacher_opinion = data[['nethour', 'le1', 'id1', 'as2', 
'an2', 'id2', 'id3', 'id4', 'id5', 'id6', 'id7', 'id8', 'id9', 'ac13', 
'id15', 'id16', 'learn7', 'learn8']]

# 計算對老師的看法的平均值
mean_teacher_opinion = internet_hours_and_teacher_opinion.drop('nethour', axis=1).mean(axis=1)

# 繪製散點圖
plt.scatter(data['nethour'], mean_teacher_opinion, marker='o')
plt.title('網路使用時數與對老師的看法之間的關聯')
plt.xlabel('網路使用時數')
plt.ylabel('對老師的看法平均值')
# 添加回歸線
sns.regplot(x=data['nethour'], y=mean_teacher_opinion, scatter=False)

plt.xlabel('網路使用時數')
plt.ylabel('對老師的看法平均值')

# 計算相關係數
correlation_coefficient = np.corrcoef(data['nethour'], mean_teacher_opinion)[0, 1]
print("相關係數:", correlation_coefficient)

plt.grid(True)
plt.show()