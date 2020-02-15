
def desk_in_class(a, b, c):
  desk = 0
  desk = round(a/2+b/2+c/2, 0)
  
  print(f"So we need {int(desk)} desks in total")

desk_in_class(20, 21, 33)







# A school decided to replace the desks in three classrooms. Each desk sits two
# students. Given the number of students in each class, print the smallest
# possible number of desks that can be purchased.
# - The program should read three integers: the number of students in each of
# the three classes, a, b and c respectively.
# - In the first test there are three groups. The first group has 20 students and
# thus needs 10 desks. The second group has 21 students, so they can get by
# with no fewer than 11 desks. 11 desks is also enough for the third group of
# 22 students. So we need 32 desks in total.