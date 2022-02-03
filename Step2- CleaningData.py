import pandas as pd
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")

podcasts_df = pd.read_csv('podcasts.csv', header=0, sep=',')
podcasts_df.info()


#Handel missing data.
podcasts_df2=podcasts_df.dropna(axis=0).copy()
podcasts_df2.info()

#Remove duplicates or irrelevant observations.
podcasts_df2.drop_duplicates(subset ="podcast_name", keep = "first" , inplace = True)
podcasts_df2.info()
#Fix structual errors.
podcasts_df2['publish_date']=podcasts_df2.publish_date.str[-4:]
podcasts_df2['top_rank']=podcasts_df2.top_rank.str.replace('%?', '').astype(float)
podcasts_df2['episodes']=podcasts_df2.episodes.str.replace('episodes?', '').astype(int)


#Filter unwanted outliers.
podcasts_df2.describe(include='all')
plt.hist(podcasts_df2.top_rank, bins= 100)
plt.xlabel("top_rank")
plt.ylabel("Frequence")
plt.show()
print(sum(podcasts_df2['top_rank']>100))
print(sum(podcasts_df2['top_rank']<0))

plt.hist(podcasts_df2.ListenScore, bins= 100)
plt.xlabel("ListenScore")
plt.ylabel("Frequence")
plt.show()
print(sum(podcasts_df2['ListenScore']>100))
print(sum(podcasts_df2['ListenScore']<0))

plt.hist(podcasts_df2.episodes, bins= 200)
plt.axis([0,3500,0,2000])
plt.xlabel("episodes")
plt.ylabel("Frequence")
plt.show()
print(sum(podcasts_df2['ListenScore']<=0))

podcasts_df2.to_csv('copy_df_podcasts.csv')

