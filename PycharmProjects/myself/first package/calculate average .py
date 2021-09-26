#calculate the average Electricity bills

jan_month,feb_month,mar_month=23,26,27
average=((jan_month+feb_month+mar_month)/3)
#convert the answer datatype float into int
total=int(average)
#we cant concatenate the int to str,so change the datatype to str
print("The average Electricity bill for 3 month is "+str(total))
#using string methods format()
print("{},is the average electricity bill for 3 months".format(total))