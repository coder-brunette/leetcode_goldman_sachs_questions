def checkInclusion(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    if len_s1 > len_s2:
        return False
    
    freq_s1 = {}  # Frequency dictionary for s1 characters
    for char in s1:
        freq_s1[char] = freq_s1.get(char, 0) + 1
    
    freq_window = {}  # Frequency dictionary for current window in s2
    for i in range(len_s1):
        freq_window[s2[i]] = freq_window.get(s2[i], 0) + 1
    
    if freq_window == freq_s1:
        return True
    
    for i in range(len_s1, len_s2):
        left_char = s2[i - len_s1]
        freq_window[left_char] -= 1
        if freq_window[left_char] == 0:
            del freq_window[left_char]
        
        right_char = s2[i]
        freq_window[right_char] = freq_window.get(right_char, 0) + 1
        if freq_window == freq_s1:
            return True
    
    return False

# Example usage:
s1 = "ab"
s2 = "dodobaei"
result = checkInclusion(s1, s2)
print(result)  # Output: True
