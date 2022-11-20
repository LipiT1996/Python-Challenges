file_content = open("questions.txt", 'r')
q_and_a = [i.strip() for i in file_content]
file_content.close()
print(q_and_a)

score = 0
total = len(q_and_a)


for i in q_and_a:
    q,a = i.split('=')
    ans = input(f"{q}: ")

    if ans == a:
        score +=1

result_write = open('results.txt', 'w')
result_write.write(f"Your final score is {score}/{total}")
result_write.close



