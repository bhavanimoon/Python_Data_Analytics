# Section - import
import pandas as pd


#Data Frames
df_col = pd.DataFrame({'col A': ['A', 'B', 'C'], 'col B': [101, 102, 103]})
df_series = pd.Series([1, 2, 3])
df_indexseries = pd.Series([100, 89, 90], index=['Maths', 'Stats', 'ML Models'], name='ML Marksheet')

#Print Statements
print ("Data Frame - df_col")
print (df_col)
print ("\nSeries - df_series")
print (df_series)
print ("\nIndexed Series - df_indexseries")
print (df_indexseries)

# Set max rows for display
pd.set_option('display.max_rows', 5)

#Read csv & set index_col=0
df_winereviews = pd.read_csv("Data/wine_reviews.csv", index_col=0)
print (df_winereviews.shape)
print (df_winereviews.head(5))