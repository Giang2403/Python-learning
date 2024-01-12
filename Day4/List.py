numbers = [1,2,3.5,4,1]

"""""
print(type(numbers))
print(numbers)
print(numbers[0], numbers[-1], numbers[3])
"""
#numbers.append(100)             #them vao cuoi list

#numbers.remove(1)               #remove value 1

#last_value = numbers.pop()         #return and remove last value
#print(last_value)

#numbers.extend([2.5, 5.5, 6.5])     #extend list

#numbers[0]=75                        #modify value

#amount = numbers.count(1)            #count value
#print(amount)

#numbers.clear()                       #clear all value

#amount=len(numbers)                    #number of members
#print(amount)

#numbers.insert(1,20)   #insert value 20 at index 1

#index_of_2 = numbers.index(2)       #return index of value
#print(index_of_2)

#numbers.reverse()   #reverse

#numbers.sort()      #sort
#numbers.sort(reverse=True)      #sort reverse order

del numbers[1]          #delete value at index 1
print(numbers)

