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



#==============================================================================================================================================
#How to bin a numeric series to 10 groups of equal size?
#Bin the series ser into 10 equal deciles and replace the values with the bin name.
ser = pd.Series(np.random.random(20))#random returns float between 0.0 to 1.0
print(ser)
re = pd.qcut(ser, q=[0, .10, .20, .3, .4, .5, .6, .7, .8, .9, 1],
              labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th'])
print(re)



#================================================================================================================================================
# How to convert a numpy array to a dataframe of given shape? (L1)
# Reshape the series ser into a dataframe with 7 rows and 5 columns
ser = pd.Series(np.random.randint(1, 10, 35))#return a random integer randint(low, high, size)
df = pd.DataFrame(ser.values.reshape(7,5))

#================================================================================================================================================
# How to find the positions of numbers that are multiples of 3 from a series?
# Find the positions of numbers that are multiples of 3 from ser
ser = pd.Series(np.random.randint(1, 20, 7))
ind = np.argwhere(ser % 3==0)


#=============================================================================================================================================
#How to extract items at given positions from a series
#From ser, extract the items at positions in list pos.
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
ser.take(pos)


#===============================================================================================================================================
#How to stack two series vertically and horizontally ?
# Get the positions of items of ser2 in ser1 as a list.
ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])

ser3 = [np.where(i==ser1)[0].tolist() for i in ser2]
print(ser3)


#===============================================================================================================================================
#How to compute the mean squared error on a truth and predicted series?
#Compute the mean squared error of truth and pred series
truth = pd.Series(range(10))
pred = pd.Series(range(10) + np.random.random(10))

np.mean((truth-pred)**2)



#===============================================================================================================================================
#How to convert the first character of each element in a series to uppercase?
#Change the first character of each word to upper case in each word of ser.
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
# Solution 1
ser.map(lambda x: x.title())

# Solution 2
ser.map(lambda x: x[0].upper() + x[1:])

# Solution 3
pd.Series([i.title() for i in ser])



#===============================================================================================================================================
#How to calculate the number of characters in each word in a series?
ser = pd.Series(['how', 'to', 'kick', 'ass?'])
# Solution 1
ser.map(lambda x: len(x))

#===============================================================================================================================================
#How to compute difference of differences between consequtive numbers of a series?
#Difference of differences between the consequtive numbers of ser.
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
dif = ser.diff().tolist()
diff = ser.diff().diff().tolist()






