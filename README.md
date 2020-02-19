# Border Crossing Analysis


## Problem
The Bureau of Transportation Statistics regularly makes available data on the number of vehicles, equipment, passengers and pedestrians crossing into the United States by land.

**For this challenge, I will calculate the total number of times vehicles, equipment, passengers and pedestrians cross the U.S.-Canadian and U.S.-Mexican borders each month. In addition, I will find the running monthly average of total number of crossings for that type of crossing and border from the input dataset provided to me.**

[Insight Data Science Border Crossing Analysis Challenge](https://github.com/InsightDataScience/border-crossing-analysis)

## Language and Libraries Used
I used Python3 and I used: csv, operator, itertools, math

## Solution
1. loading the csv file which transfer to list.
2. Using sorted to see the descending data
3. Selecting the feature of border, measure, date and value by using groupby and calculate the sum of value 
4. For rolling average, First, if the measure is different from the previous row of , its average would be 0. Second, if the measure is same as the previous, then calulate the average.
5. The data is sorted in descending order by date, value, measure, border.
6. output the result


