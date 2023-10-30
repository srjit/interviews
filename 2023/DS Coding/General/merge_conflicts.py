

def has_merge_conflict(pull_requests)-> bool:
  
  has_merge_conflict = False
  for i, p1 in enumerate(pull_requests):
    for j, p2 in enumerate(pull_requests):
      
      if i != j:

        cond1 = p1[0] <= p2[0] <= p2[1] <= p1[1]
        cond2 = p2[0] <= p1[0] <= p1[1] <= p2[1]

        cond3 = p1[0] <= p2[0] <= p1[1] <= p2[1]
        cond4 = p2[0] <= p1[0] <= p2[1] <= p1[1]

        if cond1 or cond2 or cond3 or cond4:

            has_merge_conflict = True
            return has_merge_conflict

  return has_merge_conflict

pull_requests = [[5, 10], [15, 40], [25, 50]]
print(has_merge_conflict(pull_requests))

pull_requests = [[30, 40], [10, 20], [5, 8]]
print(has_merge_conflict(pull_requests))