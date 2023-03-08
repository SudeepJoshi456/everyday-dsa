
def test_location(cards,query,mid):
    mid_number = cards[mid]
    if mid_number == query:
        if cards[mid-1] and mid-1 >=0:
            return 'left'
        else:
            return 'found'
    elif mid_number > query:
        return 'left'
    else: 
        return 'right'

def locate_card(cards,query):
    lo,hi = 0, len(cards)-1
    
    while lo<=hi:
        mid = (hi+lo)//2
        location = test_location(cards,query,mid)
        if location == 'found':
            return mid
        elif location == 'left':
            hi = mid-1
        elif location == 'right':
            lo = mid+1
    return -1
        

    #   *       *   *   *   *   **  **  *   **  *   **  



def binary_search(lo,hi,condition):
    while lo<=hi:    
        mid = (lo+hi)//2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        elif result == 'right':
            lo = mid+1
    return -1

def first_position(nums,target):
    def condition(mid):
        mid_number = nums[mid]
        if mid_number == target:
            if mid>0 and nums[mid-1]==target:
                return 'left'
            return 'found'
        elif mid_number > target:
            return 'left'
        elif mid_number < target:
            return 'right'
    return binary_search(0,len(nums)-1,condition)

def last_position(nums,target):
    def condition(mid):
        mid_number = nums[mid]
        if mid_number == target:
            if len(nums)-1>mid and nums[mid+1]==target:
                return 'right'
            return 'found'
        elif mid_number > target:
            return 'left'
        elif mid_number < target:
            return 'right'
    return binary_search(0,len(nums)-1,condition)

def first_and_last_position(nums,target):
    return first_position(nums,target), last_position(nums,target)


    


    

    

    
    
