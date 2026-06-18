class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        n = len(position)
        for i in range(n):
            d[position[i]] = speed[i]
        sorted_d = dict(sorted(d.items(),key = lambda x : x[0]))
        times = []
        for i in sorted_d:
            time = (target-i)/sorted_d[i]
            times.append(time)
        fleet = 1
        i = n-2
        fleet_time = times[-1]
        while i >=0:
            if times[i] <= fleet_time:
               pass
              
            else :
                fleet += 1
                fleet_time = times[i]
            i -= 1
        return fleet
           




        