#How to import pandas and check the version?
import pandas as pd
print("pandas version is " ,pd.__version__)

#==============================================================================================================================================
#How to create a series from a list, numpy array and dict?
import numpy as np
mylist = list('abcdefghigklmnopqrstuvwxyz')
my_arr = np.arange(26)
mydict = dict(zip(mylist, my_arr))


serie1 = pd.Series(mylist)
serie2 = pd.Series(my_arr)
serie3 = pd.Series(mydict)
print(
    """Serie 1 is {},
========================

       Serie 2 is {},
========================

       Serie 3 is {},""".format(serie1, serie2, serie3)
)


#==============================================================================================================================================
#How to convert the index of a series into a column of a dataframe?
mylist = list('abcdefghigklmnopqrstuvwxyz')
my_arr = np.arange(26)
mydict = dict(zip(mylist, my_arr))
serie = pd.Series(mydict)
df = serie.to_frame().reset_index()
print(df.head(4))

#==============================================================================================================================================
#How to combine many series to form a dataframe?
#Combine ser1 and ser2 to form a dataframe.
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
combien = pd.DataFrame({'col1':ser1, 'col2':ser2})
print(combien)


#==============================================================================================================================================
#How to assign name to the series’ index?
#Give a name to the series ser calling it ‘alphabets’.
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser1.name = 'alphabets'
print(ser1)

#==============================================================================================================================================
#How to get the items of series A not present in series B?
# From ser1 remove items present in ser2.
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser1[~ser1.isin(ser2)]


#==============================================================================================================================================
#How to get the items not common to both series A and series B?
#Get all items of ser1 and ser2 not common to both.
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ser_u = pd.Series(np.union1d(ser1, ser2))#union=> combining ser1 and ser2
ser_i = pd.Series(np.intersect1d(ser1, ser2))#intersect => taking duplicated dataset
print("serie union ", ser_u)
print("serie intersection", ser_i)

ser_u[~ser_u.isin(ser_i)]


#==============================================================================================================================================
#How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
#Compute the minimum, 25th percentile, median, 75th, and maximum of ser.
state = np.random.RandomState(100)
ser = pd.Series(state.normal(10, 5, 25))
np.percentile(ser, q=[0, 25, 50, 75, 100])


#==============================================================================================================================================
#How to get frequency counts of unique items of a series?
#Calculte the frequency counts of each unique value ser.
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
ser.value_counts()



#==============================================================================================================================================
#How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?
#From ser, keep the top 2 most frequent items as it is and replace everything else as ‘Other’.
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
print("Top 2 Freq:", ser.value_counts())
ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'
print(ser)