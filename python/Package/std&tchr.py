from college import mod1
from college import mod2

mod1.students(1000)
mod2.teachers(250)

from college.mod1 import sumOf
result=sumOf(1000,250)
print("sum of people now ",result)

