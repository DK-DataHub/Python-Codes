from collections import deque, Counter, namedtuple
tasks = deque()
tasks.append("regular task")
tasks.appendleft("urgent task")
tasks.append("Optional task")
while tasks:
    current_task = tasks.popleft()
    print("Ongoing task:",current_task)
customer_feedback = [
    "Accounts are not maintained properly",
    "Proper guidance is not provided",
    "Accurate measurements are not taken",
    "Staffs are not good in explaining processes",
    "Staff's attitude upon customers is unacceptable",
    "Clean desk is not maintained properly"

]
comments = []
for comment in customer_feedback:
    comments.extend(comment.lower().split())
    print(comments)
word_count = Counter(comments)
print(word_count.most_common(3))
Employee = namedtuple("Employee", ["Name","Role","Salary"])
e1 = Employee("Deepak","Manager", "98000")
e2 = Employee("Rajesh", "Clerk", "80000")
print(f"{e1.Name} is a {e1.Role} earning {e1.Salary}")
print(f"{e2.Name} is a {e2.Role} earning {e2.Salary}")

