import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from seaborn import FacetGrid
import warnings
warnings.filterwarnings("ignore")


podcasts_df = pd.read_csv('copy_df_podcasts.csv', header=0, sep=',')
podcasts_df2 = podcasts_df[podcasts_df['ListenScore']>=60]
#language of podcast (sum for each podcast) - listen score (avg)
language_listen_score_df = podcasts_df2.groupby(['language']).mean()
language_listen_score_df2=language_listen_score_df.filter(['language', 'ListenScore'])
language_listen_score_df2["language"]=language_listen_score_df2.index
#print(language_listen_score_df2)
#histogram
sns.barplot(x='language', y='ListenScore',data=language_listen_score_df2)
plt.xticks(rotation=90,fontsize=5)
plt.title('Language of podcast (sum for each podcast) - listen score (avg)')
plt.show()

#writer (sum for each podcast) - listen score (avg)
writer_listen_score_df = podcasts_df.groupby(['writer']).mean()
writer_listen_score_df2=writer_listen_score_df .filter(['writer', 'ListenScore'])
writer_listen_score_df2["writer"]=writer_listen_score_df2.index
#pie
df_0_to_30 = writer_listen_score_df2[(writer_listen_score_df2['ListenScore']>=0) & (writer_listen_score_df2['ListenScore']<30)].reset_index(drop=True)
df_30_to_70 = writer_listen_score_df2[(writer_listen_score_df2['ListenScore']>=30) & (writer_listen_score_df2['ListenScore']<70)].reset_index(drop=True)
df_70_to_100 = writer_listen_score_df2[(writer_listen_score_df2['ListenScore']>=70) & (writer_listen_score_df2['ListenScore']<100)].reset_index(drop=True)
sizes = [len(df_0_to_30),len(df_30_to_70),len(df_70_to_100)]
labels = [ '(0-30)','(30-70)','(70-100)']
explode = (0.04, 0.04, 0.04)
fig1, ax1 = plt.subplots()
ax1.pie(sizes,explode=explode, labels=labels, autopct='%1.2f%%',
        shadow=True, startangle=180)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('writers LS avg')
#plt.savefig('pie_chart_magnitude.png', transparent = True)
plt.show()

#countries (sum for each podcast) - listen score (avg)
country_listen_score_df = podcasts_df2.groupby(['country']).mean()
print(country_listen_score_df)
country_listen_score_df2=country_listen_score_df.filter(['country', 'ListenScore'])
country_listen_score_df2["country"]=country_listen_score_df2.index
#line chart
sns.lineplot(data=country_listen_score_df2.drop(['country'], axis=1))
plt.xticks(rotation=90,fontsize=5)
plt.title('#countries (sum for each podcast) - listen score (avg)')
plt.show()

#correlation matrix
# get correlation matrix
corr = podcasts_df.corr()
fig, ax = plt.subplots()
# create heatmap
im = ax.imshow(corr.values)

# set labels
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        text = ax.text(j, i, np.around(corr.iloc[i, j], decimals=2),
                       ha="center", va="center", color="black")
plt.show()


#episodes pie per LS>=60
episodes_df = podcasts_df2.groupby(['episodes']).count()
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
plt.title('Episodes per podcast, LS>=60')
plt.show()

#writer pie per LS >=60
writer_df = podcasts_df2.groupby(['writer']).count()
writer_df["writer"]=writer_df.index
print(writer_df)
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
plt.title('Amount of podcasts per writer, LS>=60')
plt.show()
