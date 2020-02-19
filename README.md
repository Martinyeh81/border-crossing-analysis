# Border Crossing Analysis



## Language and Libraries Used
I used Python3 and I used: csv, operator, itertools, math

## Solution
1. loading the csv file which transfer to list.
2. Using sorted to see the descending data
3. Selecting the feature of border, measure, date and value by using groupby and calculate the sum of value 
4. For the rolling average, first, we choosed border, measure and date as the key of the dictionary. Also, we created the fifth feature is average and the sixth feature is counter. Second, we changed the type of date time from string to datetime, which is easy to calculate. Third, if date is begger than previous one and measure is the same, we sum the value and count the number. Final, we change data from dictionary to list.  
5. The data is sorted in descending order by date, value, measure, border.
6. output the result


