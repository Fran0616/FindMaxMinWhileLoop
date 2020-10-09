# FindMaxMinWhileLoop
This code will allow user to enter test score or enter -1 to end the loop. Then the program will display the amount of scored entered by the user, the sum of the score, the average, and finally the minimum and maximum

The code can be viewed [here](https://github.com/Fran0616/FindMaxMinWhileLoop/blob/main/Assigment4.py)

Algorithm 
= 
1. Ask user to enter value and intruct them to enter negative one to get out of the loop
2. Use a while loop to get the user to enter as many score as they desire
3. Inside the while loop the sum mehod will add up all the score the user enter, the count variable count the amount of score they enter. The if staments of the maximum will save the value of the largest number they enter and update it each time that value change. Similar thing will happen to the second if staement but instead will save the result for the lowest number. 
4. When the user enter negative 1 they will exit the loop.
5. the meanScore variable will compute the the average by dividing the sum by the count variable 
6. Finaly the program will display to the user the amount of score they enter, the sum of the score, the mean, the highest and lowest. 


Test Data
= 
Input:
```
Enter students score or enter -1 to stop: 100
Enter students score or enter -1 to stop: 95
Enter students score or enter -1 to stop: 44
Enter students score or enter -1 to stop: 78
Enter students score or enter -1 to stop: 56
Enter students score or enter -1 to stop: 89
Enter students score or enter -1 to stop: -1
```
Output:

```
You entered:  6 score
The sum is:  462
The mean is:  77.0
The highest score is:  100
The lowest score is:  44
```
