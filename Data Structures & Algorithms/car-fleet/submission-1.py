class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we care about ma time units a car will ake to reach the end, scnethe shuttles at the end are what we care about
        # we can mabe go for a mnontononic stack based off that ETA?

        # Once we have all ETAs, we work thoghthe front to back and cap them as we go! no stack needed!

        # ETA = target-position/speed

        ETAs = [(target-start)/speed for start, speed in sorted(zip(position,speed), key = lambda x: x[0])]
        front = ETAs.pop()
        out = 1
        while ETAs:
            eta = ETAs.pop()
            if eta > front:
                front = eta
                out +=1
        return out
            
            
        