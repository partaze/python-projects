#@Author Cheryl Vadivello
#Function to calculate the final time after a given length of time. It takes an initial
#value in 12 hour format(am/pm), the length of time, and an optional
#argument of a given day. The function returns the correct final time and day if one is 
#initially provided.

def add_time(start, duration, day=None):

  amOrpm = ""
  begin = ""
  count  = 0
  when = ""
  dayNight = False
  newDay = ""
  days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

#Retrieves the digital values of hour and minutes from given strings
  splitIt = start.split()
  begin = splitIt[0].strip()
  begin = begin.replace(":",".")
  h1 = begin.split(".")
  hour1 = int((h1[0]).strip()) #Initial hour
  begin = float(begin)
  amOrpm = splitIt[1].strip()
  duration = float(duration.replace(":","."))

  total = round(begin + duration,2)
  total = str(total)
  
  t1 = total.split(".")
  hour = int(t1[0]) #Number of total hours
  minute = int(t1[1])#Number of total minutes
  
 #Handles 60 minutes to an hour conversion 
  if minute >=60:
    hour = hour + 1
    if hour==12:
      dayNight = True
    minute = minute - 60

#Adds a leading zero so that 1 becomes 01 for display purposes    
  if minute<10:
    minute = str("0" + str(minute).strip())
  else:
    minute = str(minute)

#Handles the number of days that goes by during the given length of time
  if hour >= 24:
    while hour>23:
      hour = hour -24
      count+=1
    if hour==12 :
      dayNight = True
      if amOrpm.upper()=="PM":
        count+=1
    if hour1 + hour > 12 and dayNight==False:
      count+=1
   
  if hour==0:
    hour = hour1
  
  if amOrpm.upper()== "PM" and hour>12 and count==0:
      count+=1  
      
  if hour>12 and hour<24:
    hour = hour - 12
    dayNight = True
  
  if dayNight==True:
    if amOrpm.upper()== "AM":
      amOrpm = "PM"
    else:
      amOrpm = "AM"
    dayNight = False 

  if count!=0 :
    if count == 1:
      when = "(next day)"
    else:
      when = "(" + str(count) + " days later)"
  else:
    pass

  newT = str(hour) + ":" + minute + " " + amOrpm
  new_time = (newT + " " + when.strip()).strip()

#If the optional argument of day is given, calculates the new day
#after x amount of time.  
  if day:
    day = day.lower()
    for item in days:
      item1 = item.lower()
      if item1 == day:
        i = days.index(item)
        if count>=7:
          y = (count//7)*7
          count = count - y
        
        j = count + i
        try:                #handles index errors
          newDay = days[j]
        except:
          y = (j//7)*7
          x = j - y
          newDay = days[x]
          
        if count == 0:
          new_time+= ", " + newDay.strip()
        elif count>0 and count<=len(days):
          new_time = (newT + ", " + newDay.strip() + " " + when.strip()).strip()
             
  return new_time
