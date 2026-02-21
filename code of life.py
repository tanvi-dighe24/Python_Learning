'''#1 ALARAM DRAMA
time=7
if time <= 6:
    print('Good student')
else:
    print('Snooze master')

#2 Pizza slice
slices= int(input('enter number of pizza slices:'))
if slices >= 8:
    print('party time')
else:
    print('who ate my pizza?')

#3 mobile addition check
screentime= float(input('enter scren time in hours:'))
if screentime > 5:
    print('phone loves you more than people')
else:
    print('healthy human')


#4 sleepy student
hours_slept= float(input('enter hours slept:'))
if hours_slept < 6:
    print('zombie mode')
else:
    print('fresh and active')


#wallet check
money= int(input('enter money in wallet:'))
if money >= 500:
    print('Treat for friends')
else:
    print("Let's  walk and talk")
           

#exam preparation
study_hours= float(input('enter study hours:'))
if study_hours >= 4:
    print('future topper')
else:
     print('netflix topper')

#7 hunger
hunger_level= float(input('enter ur hunger level:'))
if hunger_level > 7:
    print('order food now')
else:
    print('balance life hero')

    
#8 gaming fever
gaming_hours= float(input('enter gaming hours'))
if gaming_hours>3:
    print('game loading...life paused')
else:
    print('balance life hero')


#9 college bus race
time=float(input('enter time of reaching at stop'))
if time< 8.30:
    print('bus caught')
else:
    print('Auto driver becomes best friend')


#10 brain use
question_solved=int(input('enter no. of questions solved'))
if question_solved >= 5:
    print('brain well used')
else:
    print('brain on vacation')

    
#elif
#1 love status checker
status= input('enter relationship status:')
if status=='single':
    print('self love mode')
elif status=='crush':
    print('DayDreaming started')
elif status=='committed':
    print('all hearts')
else:
    print('complicated..like code')


#2 msg reply speed
time= float(input('enter reply time in min.:'))
if time<1:
    print('true love')
elif 1 <= time <= 30:
    print('playing hard to get')
else:
    print('seen and forgotten')
            
#3 Valentine day plan
plan= input('enter your plan (date/movie/gift):')
if plan=='date':
    print('romantic')
elif plan=='movie':
    print('netflix & feelings')
elif plan=='gift':
    print('sweet and surprise')
else:
    print('crying with icecreem')

    
#4 text message count
count=int(input('enter message per day:'))
if count > 100:
    print('love overloaded')
elif 50 <= count <= 100:
    print('strong connection')
elif 10 <= count < 50:
    print('just talking')
else:
    print('dry chat')

    
#5 couple mood detector
mood = input("Enter mood (happy/silent/angry): ")
if mood == 'happy':
    print('Perfect couple')
elif mood == 'silent':
    print('Something is wrong')
elif mood == 'angry':
    print('Run or apologize')
else:
    print('Love needs reboot')

#6 Gift Budget
amount = int(input("Enter gift amount: "))
if amount > 5000:
    print('Royal love')
elif 1000 <= amount <= 5000:
    print('Thoughtful partner')
elif 500 <= amount < 1000:
    print('Cute and sweet')
else:
    print('Love is priceless anyway')

#7 late night calls
duration = float(input("Enter call duration (minutes): "))
if duration > 120:
    print('Soulmates')
elif 60 <= duration <= 120:
    print('Deep bonding')
elif 10 <= duration < 60:
    print('Normal couple')
else:
    print('Good night already')    
    
#8 Breakup Stage
days = int(input('Enter days after breakup: '))
if days < 3:
    print('Shock mode')
elif 3 <= days <= 7:
    print('Sad songs repeat')
elif 7 < days <= 30:
    print('Healing slowly')
else:
    print('Glow-up phase')

#9 Exam Readiness
study_hours = float(input('Enter study hours: '))
if study_hours == 0:
    print('Brave but foolish')
elif 1 <= study_hours <= 2:
    print('Hope is alive')
elif 3 <= study_hours <= 5:
    print('Good student')
else:
    print('Next topper')

#10 Mobile Usage Judge
screen_time = float(input('Enter screen time (hours): '))
if screen_time < 2:
    print('Legend')
elif 2 <= screen_time <= 5:
    print('Normal user')
elif 5 < screen_time <= 8:
    print('Mobile addict')
else:
    print('Phone and you are married')


#11 Online Class Survival
camera_on = input('Is camera on? (yes/no): ')
if camera_on == 'yes':
    teacher_calling = input('Is teacher calling your name? (yes/no): ')
    if teacher_calling == 'yes':
        print('Smiling panic')
    else:
        print('Oscar-level acting')
else:
    print('Ghost student mode')

#12 Traffic Signal Brain Test
signal_color = input('Enter signal color (red/green/yellow): ')
if signal_color == 'red':
    police_present = input('Is police present? (yes/no): ')
    if police_present == 'yes':
        print('Full brake')
    else:
        print('Slow... very slow...')
else:
    print('Drive like hero')

#13 Mobile Battery Drama
battery = int(input('Enter battery percentage: '))
if battery < 20:
    charger_available = input('Is charger available? (yes/no): ')
    if charger_available == 'yes':
        print('Saved by charger')
    else:
        print('Goodbye world')
else:
    print('Scrolling peacefully')

#14 Pizza Decision Tree
is_hungry = input('are you hungry? (yes/no): ')
if is_hungry == 'yes':
    money = int(input('how much money do you have? '))
    if money > 200:
        print('order pizza')
    else:
        print('drink water and sleep')
else:
    print('why are you even here?')

#15 gaming vs Studies
exam_tomorrow = input('Is there an exam tomorrow? (yes/no): ')
if exam_tomorrow == 'yes':
    syllabus_completed = input('Is syllabus completed? (yes/no): ')
    if syllabus_completed == 'yes':
        print('One game is okay')
    else:
        print('book opens automatically')
else:
    print('game marathon')


#1 Stop at 6
for i in range(1, 11):
    if i == 6:
        break
    print(i)

#2 Search with Break
numbers = [3, 7, 10, 5, 8]
for num in numbers:
    if num > 6:
        print('First number greater than 6 is:', num)
        break

#3 Sum Until Condition (Stop at 0)
total = 0
while True:
    val = int(input('Enter a number (0 to stop): '))
    if val == 0:
        break
    total = total + val
print('Total sum is:', total)

#4 Break in Nested Loop
for i in range(1, 6):
    for j in range(1, 11):
        product = i * j
        if product > 15:
            break
        print(product, end=' ')
    print()  

#5 String Search
text = 'hello world'
for char in text:
    if char == 'w':
        break
    print(char)
#break statement
#1 Stop at 6
for i in range(1, 11):
    if i == 6:
        break
    print(i)

#2 Search with Break
numbers = [3, 7, 10, 5, 8]
for num in numbers:
    if num > 6:
        print('First number greater than 6 is:', num)
        break

#3 Sum Until Condition (Stop at 0)
total = 0
while True:
    val = int(input('Enter a number (0 to stop): '))
    if val == 0:
        break
    total = total + val
print('Total sum is:', total)

#4 Break in Nested Loop
for i in range(1, 6):
    for j in range(1, 11):
        product = i * j
        if product > 15:
            break
        print(product, end=' ')
    print()  # Moves to the next row

#5 String Search
text = 'hello world'
for char in text:
    if char == 'w':
        break
    print(char)

#continue statement
#1 Skip Specific Number (5)
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

#2 Even Numbers Only (1 to 20)
for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i)

#3 skip vowels
text = 'python programming'
vowels = 'aeiou'
for char in text:
    if char in vowels:
        continue
    print(char, end='')
print()

#4 Skip negative no.
nums = [3, -1, 7, -5, 2]
for n in nums:
    if n < 0:
        continue
    print(n)
'''
#5 multiples of 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)


    


    
    
    
    
                
                
    
    



    
    
                    

    
    
    
    
                   
                     
    
