#fsnq2
import datetime

user_symbol = input("Enter user_symbol: ") # Ask user for input 

if user_symbol.isalpha() == True and len(user_symbol) == 7 and user_symbol.isupper() == True: # Check for vaildity
  print("This is a Valid Symbol!") # Print Message
else:
  print("This is an Invalid Symbol! Please try again.") # Print Message

try:
  #Ask user for input
  chart = int(input("Please Enter Chart Type: "))
  #Check for vaildity
  if chart == 1 or chart == 2:
      # Print Message
    print("This is a Valid Chart Type")
  else:
    print("This is an Invaild Chart Type! Please try again.")
except ValueError:
  print("This is an Invaild Chart Type! Please try again.")

try:
 #Ask user for input of ts
  ts = int(input("Enter The Time Series: "))
 #Check validity of ts
  if ts > 0 and ts < 5:
      #Print Message
    print("This is a Valid Time Series.")
  else:
    print("This is an Invaild Time Series! Please try again.")
except ValueError:
  print("This is an Invaild Time Series! Please try again.")
#Ask user for input of date
ds = input("Enter start date in this format YYYY-MM-DD: ")
df = '%Y-%m-%d'
try:
#Check for vaildity of data time
  #str to time
  date = datetime.datetime.strptime(ds, df)
  print("Thank you, this is a Vaild date format.")
except ValueError:
  print("Invaild date format, please enter in this format: YYYY-MM-DD")
#Ask user for input of date
ds = input("Enter end date in this format YYYY-MM-DD: ") 
df = '%Y-%m-%d'
try:
    #Check vaildity ds df
  date = datetime.datetime.strptime(ds, df)
  print("Vaild date format")
except ValueError:
  print("Invaild date format, please enter in YYYY-MM-DD format only.")
