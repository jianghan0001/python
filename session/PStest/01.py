def get_stats(class_list):
	new_stats=[]
	for lte in class_list:
		new_stats.append([lte[0], lte[1], avg(lte[1])])
	return new_stats
def avg(grades):
    try:
	    return sum(grades)/len(grades)
    except ZeroDivisionError:
        return 0.0
test_grade=[[['peter','parker'],[10.0, 5.0, 85.0]],
			[['bruce', 'wayne'], [10.0, 8.0, 74.0]],
			[['captain', 'america'], [8.0, 10.0, 74.0]],
			[['deadpool'], []]]
print(get_stats(test_grade))