
# Implicit data structure that uses multiple arrays to represent
# a singular array of records:
#
# pros:
#   - can save space by avoiding alignment issues
#   - can be uses in languages that support only arrays of primitive types
#
# cons:
#   - bad locality of references
#   - obscure relationship between fields
#
first_names = ['John', 'Rick', 'Rob']
last_names  = ['Doe', 'Marty', 'Zombie']
ages        = [17, 23, 33]


for first_name, last_name, age in zip(first_names, last_names, ages):
    print(first_name, last_name, age)