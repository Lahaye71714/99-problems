def little_boxes(s):
    
    if len(s) < 2:
        return s
    else:
        output = [0 for i in range(128)]
        count = [0 for i in range(128)]
        s = list(s)
        for i in s:
            count[ord(i)] += 1
        for i in range(1, 128):
            count[i] += count[i-1]
        for i in range(1, len(s)):
            output[count[ord(s[i])]-1] = s[i]
            count[ord(s[i])] -= 1
        for i in range(len(s)):
            s[i] = str(output[i])
        s = "".join(s)
        
    return s
