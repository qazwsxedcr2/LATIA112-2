import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("112_foreignteacher1.csv", encoding="utf8")
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams.update({'font.size': 5})
#1.各大學雇用多少教授?
df['總教授數量'] = df['教授男'] + df['教授女']
plt.bar(df["學校名稱"], df["總教授數量"], color='b')
plt.xticks(rotation=90)
plt.title('各大學總外籍教授人數')
plt.xlabel('大學')
plt.ylabel('人數')
plt.tight_layout()
plt.show()
#2.各國籍的雇用人數比例?
nationality_counts = df.groupby('國別名稱').sum()
plt.figure(figsize=(8, 8))
plt.pie(nationality_counts['總教授數量'], labels=nationality_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('各國籍雇用人數比例')
plt.axis('equal')
plt.show()
#3.各職位不同雇用人數?
professor_counts = df[['教授男', '教授女']].sum()
associate_professor_counts = df[['副教授男', '副教授女']].sum()
assistant_professor_counts = df[['助理教授男', '助理教授女']].sum()
lecturer_counts = df[['講師男', '講師女']].sum()
positions = ['教授', '副教授', '助理教授', '講師']
counts = [professor_counts.sum(), associate_professor_counts.sum(), assistant_professor_counts.sum(), lecturer_counts.sum()]
plt.bar(positions, counts, color='b')
plt.title('各職位雇用人數')
plt.xlabel('職位')
plt.ylabel('人數')
plt.show()
#教授與副教授間的雇用數量是否有關係?
professor_counts = df[['學校名稱', '教授男', '教授女']].groupby('學校名稱').sum()
associate_professor_counts = df[['學校名稱', '副教授男', '副教授女']].groupby('學校名稱').sum()
x = professor_counts['教授男'] + professor_counts['教授女']
y = associate_professor_counts['副教授男'] + associate_professor_counts['副教授女']
m, b = np.polyfit(x, y, 1)
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='b', alpha=0.5)
plt.plot(x, m*x + b, color='r')
plt.title('教授雇用人數与副教授雇用人數关系')
plt.xlabel('教授雇用人數')
plt.ylabel('副教授雇用人數')
plt.grid(True)
plt.show()
#5.男女的性別比例?
total_prof_male = df[['教授男', '副教授男', '助理教授男', '講師男']].sum().sum()
total_prof_female = df[['教授女', '副教授女', '助理教授女', '講師女']].sum().sum()
total_prof = [total_prof_male, total_prof_female]
labels = ['男性', '女性']
plt.figure(figsize=(8, 6))
plt.pie(total_prof, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('不同職位男女比例')
plt.axis('equal')
plt.show()
#6.不同職務間男女比例的差異?
prof_positions = ['教授', '副教授', '助理教授', '講師']
male_ratios = []
female_ratios = []
for position in prof_positions:
    total_male = df[f"{position}男"].sum()
    total_female = df[f"{position}女"].sum()
    total = total_male + total_female
    male_ratio = total_male / total
    female_ratio = total_female / total
    male_ratios.append(male_ratio)
    female_ratios.append(female_ratio)
plt.figure(figsize=(10, 6))
plt.plot(prof_positions, male_ratios, marker='o', label='男性')
plt.plot(prof_positions, female_ratios, marker='o', label='女性')
plt.title('不同職務男女比例')
plt.xlabel('職務')
plt.ylabel('比例')
plt.legend()
plt.grid(True)
plt.show()
