# So you can sort an array by using a custom function
# This function can be provided to the sort method of array.sort()
# For example:

items = [
    {'sortable_value': 1},
    {'sortable_value': 2},
    {'sortable_value': 3},
    {'sortable_value': 4},
    {'sortable_value': 5},
    {'sortable_value': 9}
]

def sorting_func(item):
    return item.get('sortable_value') # NOTE: you have to return an INTEGER value which will be used for the comparison

# To sort you would simply do this: 
items.sort(key=sorting_func, reversed=True)
print(items) # [{'sortable_value': 9}, {'sortable_value': 5}, {'sortable_value': 4}, {'sortable_value': 3}, {'sortable_value': 2}, {'sortable_value': 1}]

# Take a different example: 

diff_items = [
    ('Jonathan De Guzman', 90),
    ('Max Kilman', 12), 
    ('Ruud Gullit', 100),
]

def sorting_func(item):
  return item[1]

diff_items.sort()
print(diff_items) # [('Max Kilman', 12), ('Jonathan De Guzman', 90), ('Ruud Gullit', 100)]

# You can pass in a lambda function as well which is really a more concise way to write the code

diff_items.sort(key=lambda item: item[1]) 
# or for the previous example 

items.sort(key=lambda item: item.get('sortable_value'))


    
