import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 檔案路徑
file_path = 'D:\q\data1.csv'

data = pd.read_csv(file_path, skipinitialspace=True)


data = pd.read_csv(file_path, skipinitialspace=True)

# 成績與家庭關係之間的關聯
# 需要的欄位
grades_and_family = data[['achieve', 'parent1', 'parent2', 'parent3', 'parent4', 'parent5', 'parent6', 'parent7', 'parent8', 'parent9', 'parent10']]

# 計算家庭關係的平均值
mean_family_relations = grades_and_family.mean(axis=1)

# 將成績和家庭關係的平均值合併成一個 DataFrame
combined_data = pd.concat([data['achieve'], mean_family_relations], axis=1)
combined_data.columns = ['Grades', 'Mean Family Relations']

# 繪製盒狀圖
sns.boxplot(x='Grades', y='Mean Family Relations', data=combined_data)
plt.title('Relationship between Grades and Mean Family Relations')
plt.xlabel('Grades')
plt.ylabel('Mean Family Relations')
plt.grid(True)
plt.show()

# 網路使用時數與對老師的看法之間的關聯
# 選擇需要的欄位
internet_hours_and_teacher_opinion = data[['nethour', 'le1', 'id1', 'as2', 'an2', 'id2', 'id3', 'id4', 'id5', 'id6', 'id7', 'id8', 'id9', 'ac13', 'id15', 'id16', 'learn7', 'learn8']]

# 計算對老師的看法的平均值
mean_teacher_opinion = internet_hours_and_teacher_opinion.drop('nethour', axis=1).mean(axis=1)

# 繪製散點圖
plt.scatter(data['nethour'], mean_teacher_opinion, marker='o')
plt.title('Relationship between Internet Hours and Mean Teacher Opinion')
plt.xlabel('Internet Hours')
plt.ylabel('Mean Teacher Opinion')
# 添加回歸線
sns.regplot(x=data['nethour'], y=mean_teacher_opinion, scatter=False)

# 計算相關係數
correlation_coefficient = np.corrcoef(data['nethour'], mean_teacher_opinion)[0, 1]
print("Correlation Coefficient:", correlation_coefficient)

plt.grid(True)
plt.show()