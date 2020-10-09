#Francisco 
#Write a program that asks the user repeatedly to enter a student's score or enter -1 to stop.
#When finished entering all the scores, the program should display the number of scores entered, 
#the sum of the scores, the mean, the lowest and the highest score.''''

#variables that will be use to compute the sum,  
count = 0
score = 0
sum = 0 
maximum = 0 
minimum = 0 

#Get user to enter a score and tell them to enter -1 to stop 
score = int(input("Enter students score or enter -1 to stop: "))
maximum = score
minimum = score
#While score is not negative the loop will continue
while score >= 0: 
    sum+=score #compute for the sum 
    count+=1 #Count variable for finding the amount of score user enter  
    
    #reset value for maximum after each loop if condition is met 
    if score > maximum:
        maximum = score
    #reset value for min after each loop if condition is met     
    if score < minimum:
        minimum = score
    score = int(input("Enter students score or enter -1 to stop: "))#continue loop 
#end of loop if user enter a negative number 
#compute average 
meanScore = sum/count
#print the number of scored enter, the sum of score, the mean, the lowesst, and highest 
print ("You entered: ", count, "score")
print ("The sum is: ", sum)
print ("The mean is: ", meanScore)
print ("The highest score is: ", maximum)
print ("The lowest score is: ", minimum)
