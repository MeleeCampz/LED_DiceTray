def Clamp01(value):
    return min(1,max(0, value))

def Repeat(value, min, max):
    if value > max:
        return min + (value - max) - 1
    if value < min:
        return max + (value - min) + 1
    return value
    
def Lerp(a,b,t):
    return a + (b-a) * t

def LerpColor(a: tuple[3], b: tuple[3], t) -> tuple[3]:
    return (Lerp(a[0], b[0], t), Lerp(a[1],b[1], t), Lerp(a[2], b[2], t))