# Implement all the given functions below according to the docstring.

import random
def generate_student_data(n_students, courses, cities, random_seed=42):
    '''
    Create a list of dict with dictionaries representing each attributes of each student.
    '''
    random.seed(random_seed)
    return [
      {
        "rollno": i, "city": random.choice(cities), 
        **{course: random.randint(1,100) for course in courses} 
      }
      for i in range(1,n_students+1)
    ]

def groupby(data:list, key:callable):
    '''
    Given a list of items, and a key, create a dictionary with the key as key function called 
    on item and the list of items with the same key as the corresponding value. 
    The order of items in the group should be the same order in the original list
    '''
    return {k: list(filter(lambda x: key(x) == k,data))
           for k in dict.fromkeys(map(key, data))}

def apply_to_groups(groups:dict, func:callable):
    '''
    Apply a function to the list of items for each group.
    '''
    return dict(map(lambda kv: (kv[0], func(kv[1])), groups.items()))

def min_course_marks(student_data, course):
    '''Return the min marks on a given course'''
    return min(map(lambda s: s[course], student_data))

def max_course_marks(student_data, course):
    '''Return the max marks on a given course'''
    return max(map(lambda s: s[course], student_data))

def rollno_of_max_marks(student_data, course):
    '''Return the rollno of student with max marks in a course'''
    return max(student_data, key=lambda s: s[course])["rollno"]

def sort_rollno_by_marks(student_data, course1, course2, course3):
    '''
    Return a sorted list of rollno sorted based on their marks on the three course marks. 
    course1 is compared first, then course2, then course3 to break ties.
    Hint: use tuples comparision
    '''
    return list(map(
        lambda s: s["rollno"],
        sorted(
            student_data,
            key=lambda s: (s[course1], s[course2], s[course3])
        )
    ))

def count_students_by_cities(student_data):
    '''
    Create a dictionary with city as key and number of students from each city as value.
    '''
    return apply_to_groups(
        groupby(student_data, lambda s: s["city"]),
        len
    )

def city_with_max_no_of_students(student_data):
    '''
    Find the city with the maximum number of students.
    '''
    return max(
        count_students_by_cities(student_data).items(),
        key=lambda x: x[1]
    )[0]

def group_rollnos_by_cities(student_data):
    '''
    Create a dictionary with city as key and 
    a sorted list of rollno of students that belong to 
    that city as the value.
    '''
    return apply_to_groups(
        groupby(student_data, lambda s: s["city"]),
        lambda lst: sorted(map(lambda s: s["rollno"], lst))
    )

def city_with_max_avg_course_mark(student_data, course):
    '''
    Find the city with the maximum avg course marks.
    '''
    return max(
        groupby(student_data, lambda s: s["city"]).items(),
        key=lambda kv: sum(map(lambda s: s[course], kv[1])) / len(kv[1])
    )[0]
