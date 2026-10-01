class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        fleets = 0
        prevTime = 0
        for car in cars:
            time = (target - car[0]) / car[1]
            if time > prevTime:
                fleets += 1
                prevTime = time
        
        return fleets
