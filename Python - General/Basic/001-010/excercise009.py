"""
Write a Python program to display the examination schedule.
(extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""

"""
SOLUTION:
"""

exam_st_date = (11, 12, 2014)
theDay = exam_st_date[0]
theMonth = exam_st_date[1]
theYear = exam_st_date[2]

print("The examination will start from : %d / %d / %d" % (theDay, theMonth, theYear))
#albo:
print("The examination will start from : %d / %d / %d" % (exam_st_date))