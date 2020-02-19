# Border Crossing Analysis



## Language and Libraries Used
I used Python3 and I used: csv, operator, itertools, math

## Solution
1. loading the csv file which transfer to list.
2. Using sorted to see the descending data
3. Selecting the feature of border, measure, date and value by using groupby and calculate the sum of value 
4. For rolling average, First, if the measure is different from the previous row of , its average would be 0. Second, if the measure is same as the previous, it will obtain the average.
5. The data is sorted in descending order by date, value, measure, border.
6. output the result


