

def min_element(arr: list) -> int:
    n:int = len(arr)
    if n == 0:
        raise Exception("empty array")
    else:
        if n==1:
            return arr[0]
        else:
            ans:int = arr[0]
            for i in range(1, n):
                ans = min(ans, arr[i])
            return ans

def max_element(arr:list) -> int:
    n:int = len(arr)
    if n == 0:
        raise Exception("empty array")
    else:
        if n==1:
            return arr[0]
        else:
            ans:int = arr[0]
            for i in range(1, n):
                ans = max(ans, arr[i])
            return ans   

def print_odd(arr: list):
    for i in arr:
        if i%2!=0:
            print(i)


def is_prime(x: int) -> bool:
    if x<2: return False
    elif x==2: return True
    else:
        for i in range(2, x-1):
            if x%i==0:
                return False
        return True
    
        

def print_prime(arr: list) -> list:
    response: list = []
    for i in arr:
        if is_prime(i):            
            response.append(i)
    return response
            
def rotate_array(arr: list) -> list:
    k: int = len(arr)//2
    n: int = len(arr)
    for i in range(k):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    return arr

if __name__ == "__main__":
    l: list = [7,4,6,10,56,-4,9,-5,-45]
    try:
        print(rotate_array(l))
    except:
        print("Exception caught")


