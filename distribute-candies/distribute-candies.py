from collections import Counter

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candies_allowed = len(candyType)/2
        
        candy_freq_map = Counter(candyType)
        
        queue = [(candy, freq) for candy, freq in candy_freq_map.most_common()]
        
        allocated_candies = []
        while candies_allowed > 0:
            queue_element = queue.pop(0)
            
            allocated_candies.append(queue_element[0])
            candies_allowed -= 1
            if queue_element[1] > 1:
                queue_element = (queue_element[0], queue_element[1]-1)
                queue.append(queue_element)
        return len(set(allocated_candies))