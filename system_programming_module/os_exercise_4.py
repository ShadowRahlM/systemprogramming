# import re
# test = re.split(r"the|a", "One sentence. Another one? And the last one!")



# print(test)


# ['One sentence. Another one? And ', ' last one!']

# ['One sentence. Another one? And ', 'the', ' last one!']

# ['One sentence. Ano', 'r one? And ', ' l', 'st one!']

# ['One sentence. Ano', 'the', 'r one? And ', 'the', ' l', 'a', 'st one!']



def findMaxTemperature(n, temperatureChange):
    # Initialize current temperature and maximum temperature
    current_temperature = 0
    max_temperature = float('-inf')  # Smallest possible value to start
    
    # Iterate through the temperature changes
    for change in temperatureChange:
        current_temperature += change  # Update the current temperature
        max_temperature = max(max_temperature, current_temperature)  # Update max if needed
    
    return max_temperature

if __name__ == "__main__":
    n = int(input())
    temperatureChange = list(map(int, input().split()))
    result = findMaxTemperature(n, temperatureChange)
    print(result)