print (a)
1
a=int(input("enter a number"))
b=int(input("enter a numbre"))
c=a+b
print(c)
enter a number8
enter a numbre2
10
type(a)
int
def maaark(marks):
    total = sum(marks)
    average = total / len(marks) if marks else 0
    return total, average


marks = [80, 90, 75, 85]
total, avg = maaark(marks)
print(f"Sum: {total}, Average: {avg}")
Sum: 330, Average: 82.5
def maaark(marks):
    total = sum(marks)
    average = total / len(marks) if marks else 0
    return total, average

a = input("Enter marks separated by spaces: ")
marks = list(map(int, a.split()))

total, avg = maaark(marks)
print(f"Sum: {total}, Average: {avg}")
Enter marks separated by spaces: 12 02 52 65 055 65
Sum: 251, Average: 41.833333333333336
def func():
    print("deeei")
 
