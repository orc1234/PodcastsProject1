import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import warnings
from collections import Counter
import ast
warnings.filterwarnings("ignore")



podcasts_df = pd.read_csv('copy_df_podcasts.csv', header=0, sep=',')

#categories tbl
podcasts_df.category = podcasts_df.category.apply(ast.literal_eval)
plot= pd.DataFrame(podcasts_df.category.values.tolist())
category_list=plot.to_numpy().flatten()
categories =Counter(category_list)
df_categories = pd.DataFrame.from_dict(categories, orient='index').reset_index()
print(df_categories.columns)

#episodes pie
episodes_df = podcasts_df.groupby(['episodes']).count()
episodes_df["episodes"]=episodes_df.index
df_under_100 = episodes_df[(episodes_df['episodes']>=0) & (episodes_df['episodes']<100)].reset_index(drop=True)
df_100_to_500 = episodes_df[(episodes_df['episodes']>=100) & (episodes_df['episodes']<500)].reset_index(drop=True)
df_500_to_1000 = episodes_df[(episodes_df['episodes']>=500) & (episodes_df['episodes']<1000)].reset_index(drop=True)
df_1000_to_5000 = episodes_df[(episodes_df['episodes']>=1000) & (episodes_df['episodes']<5000)].reset_index(drop=True)
df_over_5000 = episodes_df[(episodes_df['episodes']>=5000)].reset_index(drop=True)
sizes = [len(df_under_100)/len(episodes_df)*100,len(df_100_to_500)/len(episodes_df)*100,len(df_500_to_1000)/len(episodes_df)*100,len(df_1000_to_5000)/len(episodes_df)*100,len(df_over_5000)/len(episodes_df)*100]
labels = [ '(0-100)','(100-500)','(500-1000)', '(1000-5000)','(5000+)']
explode = (0.04, 0.04, 0.04,0.04,0.04)
fig1, ax1 = plt.subplots()
ax1.pie(sizes,explode=explode, labels=labels, autopct='%1.2f%%',
        shadow=True, startangle=180)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Episodes per podcast')
plt.show()



#categories barplot
#plt=sns.factorplot(x='category', y ='count', data = df_categories2, kind='bar')
sns.barplot(x='index', y=0,data=df_categories)
plt.xticks(rotation=90,fontsize=5)
plt.title('Amount of podcasts per category')
plt.show()

#writer pie
writer_df = podcasts_df.groupby(['writer']).count()
writer_df["writer"]=writer_df.index
df_1_to_5 = writer_df[(writer_df["podcast_name"]>=1) & (writer_df["podcast_name"]<5)].reset_index(drop=True)
df_5_to_10 = writer_df[(writer_df["podcast_name"]>=5) & (writer_df['podcast_name']<10)].reset_index(drop=True)
df_10_to_50 = writer_df[(writer_df['podcast_name']>=10) & (writer_df['podcast_name']<50)].reset_index(drop=True)
df_50_to_150 = writer_df[(writer_df['podcast_name']>=50) & (writer_df['podcast_name']<100)].reset_index(drop=True)
#df_over_100 = episodes_df[(episodes_df['count']>=100)].reset_index(drop=True)
sizes = [len(df_1_to_5)/len(writer_df)*100,len(df_5_to_10)/len(writer_df)*100,len(df_10_to_50)/len(writer_df)*100,len(df_50_to_150)/len(writer_df)*100]
labels = [ '(1-5)','(5-10)','(10-50)', '(50-150)']
explode = (0.04, 0.04, 0.04,0.04)
fig1, ax1 = plt.subplots()
ax1.pie(sizes,explode=explode, labels=labels, autopct='%1.2f%%',
        shadow=True, startangle=180)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Amount of podcasts per writer')
plt.show()

#country histogram
country_df = podcasts_df.groupby(['country']).count()
country_df["country"]=country_df.index
print(country_df)
country_data = country_df["country"]
count_data = country_df["podcast_name"]
plt.bar(country_data, count_data)
plt.title('countries')
plt.xlabel('country')
plt.ylabel("podcast_name")
plt.xticks(rotation=90)
plt.xticks(rotation=90)
plt.title('Amount of podcasts per country')
plt.show()

#language histogram
languages_df = podcasts_df.groupby(['language']).count()
languages_df["language"]=languages_df.index
language_data = languages_df["language"]
count_data = languages_df["podcast_name"]
plt.bar(language_data, count_data)
plt.title('languages')
plt.xlabel('language')
plt.ylabel('podcast_name')
plt.xticks(rotation=90)
plt.title('Amount of podcasts per language')
plt.show()

#since year scatterplot
# get correlation matrix
publish_df = podcasts_df.groupby(['publish_date']).count()
publish_df["publish_date"]=publish_df.index
publish_df["count"]=publish_df["podcast_name"]
sns.scatterplot(x='publish_date', y='count', data=publish_df)

plt.title('Amount of podcasts per publish year')
plt.show()
