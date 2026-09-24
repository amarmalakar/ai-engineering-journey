def isCandidateEligibleForVote(age):
    # return age >= 18
    if age < 18:
        return "Candidate is not eligible for vote"
    return "Candidate is eligible for vote"


# print(isCandidateEligibleForVote(18))
# print(isCandidateEligibleForVote(17))

expenses = [
    {"category": "food", "amount": 240.5},
    {"category": "travel", "amount": 80},
    {"category": "food", "amount": 50},
]
# print(expenses)


def total_for(items, category):
    total = 0
    for item in items:
        if item["category"] == category:
            total += item["amount"]
    return total


# print(total_for(expenses, "food"))


def total_for_fast(items, category):
    l = [i["amount"] for i in items if i["category"] == category]
    return sum(l)

print(total_for_fast(expenses, "food"))