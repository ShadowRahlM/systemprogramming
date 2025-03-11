num = [1,5,3,7,4]
target = 8
output = [(1,7),(5,3)]# explainaion: both pairs sum to 8, and (3,5) is considered the same as (5,3)
def two_sum(nums, target):
    pairs = []
    seen = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = tuple(sorted([nums[i], nums[j]]))
                if pair not in seen:
                    pairs.append(pair)
                    seen.add(pair)
    return pairs

result = two_sum(num, target)
if result:
    print(f"Pairs of numbers that add up to {target} are: {result}")
else:
    print("No two numbers add up to the target.")

# Test the function
assert two_sum([1,5,3,7,4], 8) == [(1,7), (3,5)]  # pairs that sum to 8