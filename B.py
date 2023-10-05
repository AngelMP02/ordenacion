n, x = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort() 
gondolas = 0
left, right = 0, n - 1 
while left <= right:
    if weights[right] + weights[left] <= x:
        left += 1
    right -= 1  
    gondolas += 1

print(gondolas)