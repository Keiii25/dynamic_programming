# dynamic_programming
### Question 1: Athlete work schedule 
You are an athlete, who mostly works as a personal trainer but also competes in sporting competitions. You can sometimes make more money from competing than from training, but you need time to prepare and recover, which is time that you cannot spend working as a trainer, or preparing for, competing in or recovering from any other competitions. You want to maximise the amount of money you can earn by combining your job as a personal trainer with participating in competitions. To do this, a function `best_schedule(weekly_income, competitions)`is written.

**Input** <br>
`weekly_income` is a list of non-negative integers, where `weekly_income[i]` is the amount ofmoney you will earn working as a personal trainer in week i. 

`competitions` is a list of tuples, each representing a sporting competition. Each tuple contains 3 non-negative integers, `(start_time, end_time, winnings)`.

`start_time` is the is the week that you will need to begin preparing for this competition (i.e. the first week that you cannot do your regular job as a personal trainer, if you compete in this competition).

`end_time` is the last week that you will need to spend recovering from this competition (i.e. the last week that you cannot do your regular job as a personal trainer, if you compete in this competition).

`winnings` is the amount of money you will win if you compete in this competition.

**Output** <br>
`best_schedule` returns an integer, which is the maximum amount of money that can be earned

**Complexity** <br>
`best_schedule` run in O(Nlog(N)) time and O(N) space, where N is the total number of elements in `weekly_income` and `competitions` put together.

**Example:** <br>
```
weekly_income = [3,7,2,1,8,4,5]
competitions = [(1,3,15),(2,2,8),(0,4,30),(3,5,19)]
print(best_schedule(weekly_income, competitions))
>>> 42
```

### Question 2: Sales itinerary
A salesperson lives on the coast. They travel to various cities along the coast to work. Sometimes they stay in a city for a day or a few days to work, and other times they simply pass through on their way to another city.

Since Covid-19, each city has instituted a policy of having travelers quarantine, but only if they want to stay in the city. If they are just passing through, they can continue on their way without quarantining. Also, each city asks visitors to quarantine for a different amount of time. The salesperson has an idea of how much money they can make by working in each city, for each day. They need to decide which cities to travel to, and which cities to work in, in order to make the most money.

Each day, the salesperson can either work for the day in their current city (assuming they have finished quarantine), or they can travel to either adjacent city. Traveling always takes 1 day, and since the cities are along a coast, each city has two adjacent cities, except for two cities on the ends of the coast, which only have 1.

To solve this problem, a function `best_itinerary(profit, quarantine_time, home)` is written.

**Input** <br>
We think of the n cities as being numbered 0...n-1. In one day, the salesperson can travel from city i to either city i+1 or i-1. From city 0 they can only travel to city 1, and from city n-1 they can only travel to city n-2.

`profit` is a list of lists. All interior lists are length n. Each interior list represents a different day. profit[d][c] is the profit that the salesperson will make by working in city c on day d.

`quarantine_time` is a list of non-negative integers. quarantine_time[i] is the number of days city i requires visitors to quarantine before they can work there.

`home` is an integer between 0 and n-1 inclusive, which represents the city that the salesperson starts in. They can start working in this city without needing to quarantine on the first day. If they leave and come back later, they will need to quarantine.

**Output** <br>
`best_itinerary` returns an integer, which is the maximum amount of money that can be earned by the salesperson.

**Example:** <br>
```
profit = [
[6, 9, 7, 5, 9]
[4, 7, 3, 10, 9]
[7, 5, 4, 2, 8]
[2, 7, 10, 9, 5]
[2, 5, 2, 6, 1]
[4, 9, 4, 10, 6]
[2, 2, 4, 8, 7]
[4, 10, 2, 7, 4]]
quarantine_time = [3,1,1,1,1]
best_itinerary(profit, quarantine_time, 0)
>>> 39
best_itinerary(profit, quarantine_time, 1)
>>> 54
best_itinerary(profit, quarantine_time, 2)
>>> 47
best_itinerary(profit, quarantine_time, 3)
>>> 57
best_itinerary(profit, quarantine_time, 4)
>>> 51
```


