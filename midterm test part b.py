#Comp SCI test - Ahmed Abdallah

#---PART B---

list = [4,5,9,8,10,17,99,77]
odd = ['1','3','5','7','9']
even = ['2','4','6','8','0']
len = 0
list.sort()

for x in list:
    len +=1
len = str(len)

if (len[-1]) in odd:
    len = int(len)
    len = len//2
    print(list[len])
    
elif (len[-1]) in even:
    len = int(len)
    len = len//2
    tot = list[len] + list[len-1]
    tot /= 2
    print(tot)



# list = []
# odd =  ['1','3','5','7','9']
# even = ['2','4','6','8','0']
# 
# len = int(input('how many numbers do you want to enter? '))
# 
# for x in range(len):
#     num = int(input('enter a number '))
#     list.append(num)
#     
# list.sort()
# len = str(len)
# 
# if len[-1] in odd:
#     len = int(len)
#     len = len//2
#     print('the numbers you entered are', *list,'\nthe median of these numbers is', list[len])
#     
# elif len[-1] in even:
#     len = int(len)
#     len = len//2
#     tot = list[len] + list [len-1]
#     tot /= 2
#     print(f'the numbers you entered are', *list,' \nthe mediean of these numbers is {tot}')
    
    
    
# list = []
# odd =  ['1','3','5','7','9']
# even = ['2','4','6','8','0']
# len = 0
# 
# while True:
#     num = input('enter a number (if youre done click enter) ')
#     if num != '':
#         num = int(num)
#         list.append(num)
#         len += 1
#     else:
#         break
#     
# list.sort()
# len = str(len)
# 
# if len[-1] in odd:
#     len = int(len)
#     len = len//2
#     print('the numbers you entered are', *list,'\nthe median of these numbers is', list[len])
#     
# elif len[-1] in even:
#     len = int(len)
#     len = len//2
#     tot = list[len] + list [len-1]
#     tot /= 2
#     print(f'the numbers you entered are', *list,' \nthe mediean of these numbers is', tot)
