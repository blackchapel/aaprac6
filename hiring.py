# HIRING PROBLEM ANALYSIS

import random

def hiring_problem(n):
    best = 0
    cost = 0
    print("CANDIDATE\tH/DH\t\tCOST")
    for i in range(1, n+1):
        candidate = random.randint(1, 100)
        if candidate > best:
            best = candidate
            cost += 1
            decision = "H"
        else:
            cost += 0
            decision = "DH"
        print(i, "\t\t", decision, "\t\t", cost)

n = int(input("Enter the number of candidates: "))
print()
print("--------------- HIRING PROBLEM --------------")
hiring_problem(n)


# HIRING PROBLEM ANALYSIS LONG

import random

class Candidate:
    def __init__(self):
        self.score = random.randint(1, 100)
        
    def interview(self):
        return self.score

total_candidates = 10
hiring_cost = 10
interview_cost = 2

market = []
finance = []
tech = []

for _ in range(total_candidates):
    option = random.randint(0, 2)
    if option == 0:
        market.append(Candidate())
    elif option == 1:
        finance.append(Candidate())
    else:
        tech.append(Candidate())

total_cost = [0, 0, 0]
current_best = [0, 0, 0]

print("Marketing")
i = 0
while market:
    total_cost[0] += interview_cost
    current_person_score = market[0].interview()
    print(f"Candidate: {i}: Score: {current_person_score}, current-best: {current_best[0]}")
    if current_person_score > current_best[0]:
        current_best[0] = current_person_score
        total_cost[0] += hiring_cost
        print("Candidate hired")
    market.pop(0)
    i += 1

print("Finance")
j = 0
while finance:
    total_cost[1] += interview_cost
    current_person_score = finance[0].interview()
    print(f"Candidate: {j}: Score: {current_person_score}, current-best: {current_best[1]}")
    if current_person_score > current_best[1]:
        current_best[1] = current_person_score
        total_cost[1] += hiring_cost
        print("Candidate hired")
    finance.pop(0)
    j += 1

print("Tech")
k = 0
while tech:
    total_cost[2] += interview_cost
    current_person_score = tech[0].interview()
    print(f"Candidate: {k}: Score: {current_person_score}, current-best: {current_best[2]}")
    tech.pop(0)
    k += 1