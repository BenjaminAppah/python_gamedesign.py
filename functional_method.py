# python functional methods are map( filter9 reduce

# map is used to transform and manipulate a collectionc of data
# example of map : add_two = list(map(lamboda a + 2,list_item))
# filter is used to filter a collection of data 
 
list_data = [2,3,4,5,6,7,8]

# map exaples

def add_two(data):
    new_list = []
    for number in data:
        number += 2 
        new_list.append(number)
    return new_list

#second approach using python list comprehension 
def add_two2(data):
    return [number + 2 for number in data]

# third approach

add_Two2 = list(map(lambda number:number + 2,list_data))


print(add_two(list_data))
print(add_two2(list_data))


# python filter 

items = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda a: a % 2 == 0,items))
odd_numbers = list(filter(lambda a: a % 2  == 0,items))
print("even numbers",even_numbers)
print("even numbers",odd_numbers)


# list comprehension
evenNumbers = [number for number in items if number % 2 == 0]
print("even number using list comprehension ",evenNumbers)
