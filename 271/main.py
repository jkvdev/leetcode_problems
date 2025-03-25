# Leetcode Premium 271
# Encode and decode a list of strings into a single string

# ['neet', 'code'] => '4#neet4#code'
# store the number of characters per string + delimiter

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string
    """
    def encode(self, strs):
        # Store the result
        res = ""
        
        # Loop over all strings
        for s in strs:
            # Save current string + delimiter
            res += str(len(s)) + "#" + s
        
        # Return response
        return res

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # Initialize response array and counter
        res, i = [], 0
        
        # While i still in bounds
        while i < len(str):
            # set j equal to i
            # where the interval from i to j represents 
            # the length of the string after the delimiter
            j = i
            # loop until you get to delimiter
            while str[j] != '#':
                # increment j
                j += 1
            # get the length of the string 
            length = int(str[i:j])
            # append the string considering the delimiter
            res.append(str[j+1 : j+1+length])  # Fixed slicing
            # increment i to the end of the string
            i = j + 1 + length
        # return decoded array 
        return res


# Create an instance of the Solution class
solution = Solution()

# Example list of strings
strs = ["hello", "world", "encode", "decode", "123#456"]

# Encode the list of strings
encoded_str = solution.encode(strs)
print("Encoded:", encoded_str)

# Decode the encoded string
decoded_list = solution.decode(encoded_str)
print("Decoded:", decoded_list)



