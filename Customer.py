import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv("/Users/umayyentur/Downloads/Customers.csv")
data = data1.copy()
data.info()


data["Gender"].replace("Male", 1, inplace=True)
data["Gender"].replace("Female", 0, inplace=True)


gender_count = data["Gender"].value_counts()
female_percentage = (gender_count[0] / len(data["Gender"])) * 100



def calculate_average_sales_by_age(data, age_column, sales_column):
    average_sales = {}
    unique_ages = data[age_column].unique()

    for age in unique_ages:
        if age < 18:
            continue
        elif 18 <= age <= 24:
            age_group = '18-24'
        elif 25 <= age <= 32:
            age_group = '25-32'
        elif 33 <= age <= 43:
            age_group = '33-43'
        elif 44 <= age <= 55:
            age_group = '44-55'
        elif 56 <= age <= 70:
            age_group = '56-70'
        else:
            age_group = '71-99'

        average_sales[age_group] = data[data[age_column] == age][sales_column].mean()

    return average_sales


average_sales_by_age = calculate_average_sales_by_age(data, 'Age', 'Spending Score (1-100)')


def calculate_average_score_by_income(data, income_col, score_col):
    avg_score = {}
    
    data[income_col] = pd.to_numeric(data[income_col], errors='coerce')
    
    data.dropna(subset=[income_col], inplace=True)

    unique_incomes = data[income_col].unique()

    for income in unique_incomes:
        if 0 < income < 1000:
            continue
        elif 1000 <= income <= 5000:
            income_group = "1000-5000"
        elif 5000 < income <= 10000:
            income_group = "5000-10000"
        elif 10000 < income <= 15000:
            income_group = "10000-15000"
        elif 15000 < income <= 25000:
            income_group = "15000-25000"
        elif 25000 < income <= 35000:
            income_group = "25000-35000"
        elif 35000 < income <= 50000:
            income_group = "35000-50000"
        elif 50000 < income <= 75000:
            income_group = "50000-75000"
        else:
            income_group = "+75000"

        avg_score[income_group] = data[data[income_col] == income][score_col].mean()

    return avg_score


average_score_by_income = calculate_average_score_by_income(data, "Annual Income ($)", "Spending Score (1-100)")


def calculate_average_score_prof(data, prof_col, scor_col):
    avg_score = {}
    
    data[prof_col] = data[prof_col].str.lower()

    
    grouped_data = data.groupby(prof_col)
    for prf, group in grouped_data:
        avg_score[prf] = group[scor_col].mean()
    return avg_score

avg_score_by_prf = calculate_average_score_prof(data, "Profession", "Spending Score (1-100)")




custom_colors = ['#FCAEAE', '#1D5D9B', '#CEE6F3', '#D71313', '#D62732', '#7895CB']

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))


ax1.pie([female_percentage, 100 - female_percentage], labels=["Female", "Male"], colors=custom_colors[:2],
        textprops={'color': 'black', 'fontsize': 14, 'fontweight': 'bold'}, explode=(0, 0.1), autopct="%1.1f%%",
        startangle=90)
ax1.set_title("Gender Distribution of Online Shopping", fontweight="bold")


age_groups = list(average_sales_by_age.keys())
average_sales = list(average_sales_by_age.values())

ax2.bar(age_groups, average_sales, color=custom_colors[2], edgecolor='black')
ax2.set_title('Average Sales by Age Group', color="black", fontweight="bold")
ax2.set_xlabel('Age Group')
ax2.set_ylabel('Average Sales')
ax2.tick_params(axis='x', rotation=45)


sorted_average_score = dict(sorted(average_score_by_income.items(), key=lambda x: x[1]))

income_groups = list(sorted_average_score.keys())
scores = list(sorted_average_score.values())

ax3.bar(income_groups, scores, color=custom_colors[3], edgecolor='black')
ax3.set_title("Average Spending Score by Income Group", fontsize=15, fontweight="bold", color="black")
ax3.set_xlabel("Income Group")
ax3.set_ylabel("Average Spending Score")
ax3.tick_params(axis='x', rotation=45)


sorted_average_prf = dict(sorted(avg_score_by_prf.items(), key=lambda x: x[1]))
prf_groups = list(sorted_average_prf.keys())
scores = list(sorted_average_prf.values())


max_professions = 10
ax4.bar(prf_groups[:max_professions], scores[:max_professions], color=custom_colors[5], edgecolor='black')
ax4.set_title("Average Spending Score by Profession", fontsize=15, fontweight="bold", color="black")
ax4.set_xlabel("Profession")
ax4.set_ylabel("Average Spending Score")
ax4.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()


age_groups = list(average_sales_by_age.keys())
average_sales = list(average_sales_by_age.values())
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:green']
age_range_labels = ['18-24', '25-32', '33-43', '44-55', '56-70','71-99']

plt.bar(age_groups, average_sales, color=bar_colors, edgecolor='black')

plt.title('Average Sales by Age Group', color='black', fontweight='bold')
plt.xlabel('Age Group')
plt.ylabel('Average Sales')
plt.tick_params(axis='x', rotation=45)


plt.legend(labels=age_range_labels, title='Age Range')

plt.tight_layout()
plt.show()
