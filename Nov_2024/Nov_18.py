# Defuse The Bomb
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        
        # If k is zero, return an array of zeros
        if k == 0:
            return [0] * n
        
        # Create the extended array to handle circular wrapping
        extended_code = code * 2
        
        # Initialize result array
        result = [0] * n
        
        if k > 0:
            # Compute sum of first `k` numbers
            current_sum = sum(extended_code[1:k + 1])
            
            for i in range(n):
                result[i] = current_sum
                # Slide the window by removing the outgoing element and adding the incoming element
                current_sum -= extended_code[i + 1]
                current_sum += extended_code[i + k + 1]
        
        elif k < 0:
            k = -k  # Use absolute value for negative k
            
            # Compute sum of first `k` numbers in reverse
            current_sum = sum(extended_code[n - k:n])
            
            for i in range(n):
                result[i] = current_sum
                # Slide the window by removing the outgoing element and adding the incoming element
                current_sum -= extended_code[n - k + i]
                current_sum += extended_code[i]
        
        return result
