#AGGREGATE METHOD IN AMORTIZED ANALYSIS USING DYNAMIC TABLES

def aggregate(n):
    size=1
    dcost=0
    icost=0
    total_cost=0
    total=0

    print('Element\tDoubling Copying cost\tInsertion cost\Total cost')

    for i in range(1, n + 1):
        icost=1
        if i > size:
            size *= 2
            dcost = i - 1
        total_cost = dcost + icost
        total = total + total_cost

        print(i,"\t",dcost,"\t\t\t",icost,"\t\t",total_cost)
        dcost = 0
        icost = 0

    amortized_cost = total / n
    return amortized_cost

n = int(input("Enter no of elements: "))
am = aggregate(n)
print("Amortized cost: ",am)


#AGGREGATE METHOD IN AMORTIZED ANALYSIS USING STACK

class aggregateStack:
    def _init_(self):
        self.stack=[]
        self.cost= 0 

    def push(self, item):
        self.stack.append(item)
        self.cost += 1

    def pop(self):
        self.stack.pop()
        self.cost += 1

    def multipop(self, k):
        for _ in range(k):
            self.pop()

s = aggregateStack()
s.push(10)
s.push(20)
s.pop()
s.push(30)
s.push(40)
s.multipop(2)

print('Amortized cost: ', s.cost / 7)