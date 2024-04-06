import pandas as pd

employment_and_dev_type = pd.read_csv('survey_results_public.csv')

# გამოიტანთ ცხრილის სასურველ სტრიქონებს და სვეტებს
print(employment_and_dev_type.iloc[2:5, 3:9])

# დაუნიშნეთ ინდექსირება ცხრილის კონკრეტული სვეტის მიმართ
employment_and_dev_type.set_index('Country', inplace=True)
print(employment_and_dev_type.head())

# შექმნით 2 პარამეტრზე დამოკიდებულ ფილტრს. დაბეჭდეთ შესაბამისი ცხრილი.
filter_1 = employment_and_dev_type['Country'] == 'Georgia'
filter_2 = employment_and_dev_type['Age'] == "18-24 years old"
filtered_employment_and_dev_type = employment_and_dev_type.loc[filter_1 & filter_2]
print(filtered_employment_and_dev_type.head())

# დაასორტირეთ ცხრილი 2 პარამეტრის გამოყენებით
sorted_employment_and_dev_type = employment_and_dev_type.sort_values(by=['Country', 'Age'], ascending=[True, False])
print(sorted_employment_and_dev_type[['Country', 'Age']].head())

# გამოიყენეთ კონკრეტული სვეტის მნიშვნელობისთვის სტატისტიკური ფუნქციები (mean, standard
# deviation, median, min, max).
comp_stats = {
    'Mean Converted Compensation (Yearly)': employment_and_dev_type['ConvertedCompYearly'].mean(),
    'Standard Deviation of Converted Compensation (Yearly)': employment_and_dev_type['ConvertedCompYearly'].std(),
    'Median Converted Compensation (Yearly)': employment_and_dev_type['ConvertedCompYearly'].median(),
    'Minimum Converted Compensation (Yearly)': employment_and_dev_type['ConvertedCompYearly'].min(),
    'Maximum Converted Compensation (Yearly)': employment_and_dev_type['ConvertedCompYearly'].max()
}

print("\nConverted Compensation Statistics:")
print(comp_stats)


# Numpy და Matplotlib-ის ბიბლიოთეკების გამოყენებით ააგეთ 2 სხვადასხვა ტიპის გრაფიკი (მაგ. Bar და
# ხაზოვანი დიაგრამები).
import numpy as np
import matplotlib.pyplot as plt

# 5 ყველაზე მცირე საშუალო წლიური ხელფასი ქვეყნების მიხედვით
top_5_countries = employment_and_dev_type.groupby('Country')['ConvertedCompYearly'].mean().sort_values(ascending=True).head(5)
top_5_countries.plot(kind='bar')
plt.title('Top 5 Countries with the Highest Yearly Compensation')
plt.ylabel('Converted Compensation (Yearly)')
plt.xlabel('Country')
plt.show()

# სინუსოიდას ვიზუალიზაცია
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title('Sine Function')
plt.ylabel('y')
plt.xlabel('x')
plt.show()