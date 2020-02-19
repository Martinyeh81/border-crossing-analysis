# Border Crossing Analysis



## Language and Libraries Used
I used Python3 and Libraries are csv, operator, itertools, math, datetime

## Solution
1. Loading the csv file which transfer to list.
2. Using sorted to see the descending data
3. Selecting the feature of border, measure, date and value by using groupby and calculate the sum of value 
4. For the rolling average, first, we created the fifth feature is average and the sixth feature is counter. Second, we changed the type of date time from string to datetime, which is easy to calculate. Final, if date is begger than previous one and measure is the same, we summed the value and counted the number.  
5. The data was sorted in descending order by date, value, measure, border.
6. output the result


