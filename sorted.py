def sort_by_age(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

people = [("Steve", 67), ("John", 95), ("Kevin", 235)]
sorted_people = sort_by_age(people)
print(sorted_people)
