def Clamp01(value):
    return min(1,max(0, value))

def Repeat(value, min, max):
    if value > max:
        return min + (value - max) - 1
    if value < min:
        return max + (value - min)
    return value
    
def Lerp(a,b,t):
    return a + (b-a) * t