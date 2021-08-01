def best_schedule(weekly_income, competitions):
    '''
    Calculate the maximum amount of money that can earn by combining job as a personal
    trainer with participating in competitions
    :param: weekly_income: A list of non-negative integers where weekly_income[i] is the income the person will 
                            receive during i week when working as a trainer
    :param: competitions: A list of tuples with non-negative integers. Each tuple contains
                            3 non-negative integers, (start_time, end_time, winnings)
    :return: A positive integer which the maximum amount of money the person can gain while working as a 
                trainer and competeting in competitons
    :time complexity: O(n log n), where n is the total number of elements in weekly_income and competitions put together
    :space complexity: O(n), where n is the total number of elements in weekly_income and competitions put together
    '''
    #add weekly_income into the competitions list to combine them
    for i in range(len(weekly_income)):
        competitions += [(i,i, weekly_income[i])]
    
    #sorting the list in a non decreasing order with the end week of each job as the key
    #O(n log n)
    competitions.sort(key=lambda x:x[1])

    #O(n)
    #create a list for memoisation
    memo = [0]*(len(weekly_income)+1)

    #O(n)
    #iterate through the competitions list 
    for i in range(0, len(competitions)):
        week = competitions[i][1]
        current_profit = competitions[i][2]

        #storing a reference to the value of current profit
        temp = current_profit

        #check if there are multiple jobs that start or end in the same week
        if (competitions[i][0] <= competitions[i-1][0]) or (competitions[i-1][0] <= competitions[i][0] and competitions[i-1][1] == competitions[i][1]):
            prev_profit = memo[competitions[i][0]] #the profit from previous week
            temp += prev_profit 

            #if temp is larger than the current income for this week and the coming week, temp is maximum that can be earned during the week
            if temp > memo[week] and temp > memo[week+1]:
                current_profit = temp
            else:
                if temp <= memo[week]:
                    current_profit = memo[week]

                #if temp less than memo[week+1]
                else:
                    current_profit = memo[week+1]
        else:
            current_profit += memo[week]
        memo[week+1] = current_profit
    return memo[-1]


def best_itinerary(profit, quarantine_time, home):
    '''
    Find the maximum profit to be earned by deciding which cities to travel to and to work in
    :param: profit: A list of lists where each interior list has a length of n. Each interior list represent a different day.
                    profit[d][c] is the profit that the salesperson will make by working in city c on day d.
    :param: quarantine_time: A list of non-negative integers.quarantine_time[i] is the number of
                            days city i requires visitors to quarantine before they can work there.
    :param: home: An integer between 0 to n-1 , where n = number of cities. Home is the current city that the salesman is currently at 
    :return: The maximum profit that can be earned
    :time complexity: O(nd), where n is the number of cities(length of quarantine_time), and d is the number of days(length of profit)
    :space complexity: O(nd), where n is the number of cities(length of quarantine_time), and d is the number of days(length of profit)
    '''
    day = len(profit)
    cities = len(quarantine_time)
    memo = []

    #O(nd)
    #create a memo as a list of lists of tuples
    for i in range(len(profit)+1):
        memo += [[(0,0)]*(len(quarantine_time))]
    
    #the first value in the tuple is the profit that can be earned if the person choose to work in the same city
    #the second value in the tuple is the profit that can be earned if the person choose to travel to another city

    #O(nd)
    #iterate through the day starting from the end
    for i in range(day-1, -1, -1):
        for j in range(cities):
            left = 0
            right = 0
            temp_left = 0
            temp_right = 0

            #if it is the first city
            if j == 0:
                #check if the person can go to the next city after quarantine, if not the second value in the tuple will be zero
                if i+1+quarantine_time[j+1] > day-1: 
                    temp = (profit[i][j]+max(memo[i+1][j]), 0)
                else:
                #first value in the tuple is the profit that can be earned if the person choose to work in the same city
                    temp = (profit[i][j]+max(memo[i+1][j]), max(memo[i+1+quarantine_time[j+1]][j+1]))
                
                #check if travel to 1 or more cities consequencely and after being quarantined will result in higher profit
                if memo[i+1][j+1][1] > max(temp):
                    temp = (profit[i][j]+max(memo[i+1][j]), memo[i+1][j+1][1])
                memo[i][j] = temp

            #if it is the last city
            elif j == cities-1:
                #check if the person can go to another city after quarantine, if not the second value in the tuple will be zero
                if i+1+quarantine_time[j-1] > day-1: 
                    temp = (profit[i][j]+max(memo[i+1][j]), 0)
                else:
                #first value in the tuple is the profit that can be earned if the person choose to work in the same city
                    temp = (profit[i][j]+max(memo[i+1][j]), max(memo[i+1+quarantine_time[j-1]][j-1]))
                
                #check if travel to 1 or more cities consequencely and after being quarantined will result in higher profit
                if memo[i+1][j-1][1] > max(temp):
                    temp = (profit[i][j]+max(memo[i+1][j]), memo[i+1][j-1][1])
                memo[i][j] = temp
            else:
                 #check if the person can go to the city before the current city after quarantine, if not the second value in the tuple will be zero
                if i+1+quarantine_time[j-1] <= day-1:
                    left = max(memo[i+1+quarantine_time[j-1]][j-1])
                else:
                    left = 0

                #Obtain the profit value that can be gained after travelling the 1 or more cities consequencely 
                if i + 1 <= day-1:
                    temp_left = memo[i+1][j-1][1]

                 #check if the person can go to the next city after quarantine, if not the second value in the tuple will be zero
                if i+1+quarantine_time[j+1] <= day-1:
                    right = max(memo[i+1+quarantine_time[j+1]][j+1])
                else:
                    right = 0
                
                #Obtain the profit value that can be gained after travelling the 1 or more cities consequencely 
                if i + 1 <= day - 1:
                    temp_right = memo[i+1][j+1][1]
                
                #add the profit if staying at the same city with the maximum profit that can be earned up to the i+1 day
                #second value: find the maximum profit between travelling to one city to work or travel to more than 1 city consequencely  
                memo[i][j] = (profit[i][j]+max(memo[i+1][j]), max(left,right, temp_left, temp_right))
    return max(memo[0][home])




   
