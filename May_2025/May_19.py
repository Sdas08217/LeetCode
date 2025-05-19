class Solution:
    def triangleType(self, nums: List[int]) -> str:
        # Check if the given sides can form a valid triangle
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"
        
        # Check for equilateral triangle
        if a == b == c:
            return "equilateral"
        
        # Check for isosceles triangle
        if a == b or b == c or a == c:
            return "isosceles"
        
        # If none of the above, it is a scalene triangle
        return "scalene"
