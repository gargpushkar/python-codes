# Trains and Platforms

# You are given the arrival and departure times for n trains at a railway station. Find the minimum number of platforms the railway station needs so that none of the trains have to wait.

# The time is given in minutes from midnight. All trains have departures on the same day.

# Example:
# Trains (arrival, departure): [(120, 130), (130, 150), (125, 145), (150, 180)]
# Output: 3
# Explanation: At 2:10 AM (130th minute), there are 3 trains at the station.

# trains = [(120, 130), (130, 150), (125, 145), (150, 180)]
trains = [(360, 400), (260, 380), (210, 250), (420, 450), (440, 480), (370, 420)]

n = len(trains)
arrival = [0]*n
departure = [0]*n
k = 0
for i, j in trains:
    arrival[k] = i
    departure[k] = j
    k+=1


arrival.sort()
departure.sort()
i=0
j=0
count = 0
ans = 0
print(arrival)
print(departure)
while i<n:
    if arrival[i] <= departure[j]:
        count += 1
        ans = max(count, ans)
        i+=1
    else:
        count -= 1
        j+=1

print(ans)