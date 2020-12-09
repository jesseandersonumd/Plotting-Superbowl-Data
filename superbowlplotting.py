import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

super_bowls = pd.read_csv('datasets/super_bowls.csv')
tv = pd.read_csv('datasets/tv.csv')
halftime_musicians = pd.read_csv('datasets/halftime_musicians.csv')

display(super_bowls.head())
display(tv.head())
display(halftime_musicians.head())

tv.info()
halftime_musicians.info()

# Inspecting significant differences in combined points - outliers

display(super_bowls[super_bowls.difference_pts == 1])
display(super_bowls[super_bowls.difference_pts >= 35])

# Plotting
plt.style.use('seaborn')
plt.hist(super_bowls['combined_pts'])
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()

# Create histogram 
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()

# Create seaborn plot
sns.regplot(x=games_tv["difference_pts"], y=games_tv["share_household"], data=games_tv)

# Creating three line plots to assess trends listed below
plt.subplot(3, 1, 1)
plt.plot(tv['super_bowl'], tv['avg_us_viewers'], color='#648FFF')
plt.title('Average Number of US Viewers')

plt.subplot(3, 1, 2)
plt.plot(tv['super_bowl'], tv['rating_household'], color='#DC267F')
plt.title('Household Rating')

plt.subplot(3, 1, 3)
plt.plot(tv['super_bowl'], tv['ad_cost'], color='#FFB000')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')

# Creating halftime appearances data and modifying - remove marching bands
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# Plotting histograms of songs during performance
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel('Number of Songs Per Halftime Show Performance')
plt.ylabel('Number of Musicians')
plt.show()

# Sorting bands by appearance, descending
no_bands = no_bands.sort_values('num_songs', ascending=False)
display(no_bands.head(15))

patriots = 'New England Patriots'
rams = 'Los Angeles Rams'

# Who will win Super Bowl LIII?
super_bowl_LIII_winner = "rams"
print('The winner of Super Bowl LIII will be the', super_bowl_LIII_winner)