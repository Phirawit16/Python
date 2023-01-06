number_question = int(input())
solution = input()[:number_question]
lst_solution = []

for letter in solution:
	lst_solution.append(letter)

adrian_point = 0
bruno_point = 0
goran_point = 0

adrian_answer = ["A", "B", "C"] * number_question
bruno_answer = ["B", "A", "B", "C"] * number_question
goran_answer = ["C", "C", "A", "A", "B", "B"] * number_question

i = 0
for sol in lst_solution: 
    if sol == adrian_answer[i]:
        adrian_point+=1
    else:
        adrian_point+=0
    i+=1

i = 0
for sol in lst_solution:
    if sol == bruno_answer[i]:
        bruno_point+=1
    else:
        bruno_point+=0
    i+=1

i = 0
for sol in lst_solution:
    if sol == goran_answer[i]:
        goran_point+=1
    else:
        goran_point+=0
    i+=1

all_point = max(adrian_point, bruno_point, goran_point)

print(all_point)
if all_point == adrian_point:
    print("Adrian")
if all_point == bruno_point:
    print("Bruno")
if all_point == goran_point:
    print("Goran")
