import random

n = []
num_simulate = int(input('Enter Number of Simulate: '))
num_players = int(input("Enter The number Of Players: "))

def get_results(num_players, rolls):
    results = []
    for i in range(num_players):
        results.append([])
        results[i].append(random.randint(1, 10))
        current_position = results[i][0]
        while current_position < len(rolls):
            results[i].append(rolls[current_position])
            current_position += results[i][-1]
    return results

def calculate_steps_to_match(results):
    steps = 0
    while steps < len(results[0]):
        first_result = results[0][steps]
        match = True
        for player_results in results:
            if steps >= len(player_results) or player_results[steps] != first_result:
                match = False
                break
        if match:
            break
        steps += 1
    return steps

for numsumulate in range(num_simulate):
    rolls = [random.randint(1, 6) for _ in range(300)]
    results = get_results(num_players, rolls)

    for i in range(num_players):
        print(f"Player {i+1} results: ", end="")
        for result in results[i]: 
            print(result , end=" ")
        print('\n')

    steps_to_match = calculate_steps_to_match(results)
    n.append(steps_to_match)
    print(f"Number of steps to match all players: {steps_to_match} \n")

print('list of steps:', n)
