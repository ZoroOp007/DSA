def mySqrt(x: int) -> int:
    
    if( x == 0 or x == 1):
        return x
    else:
        beg = 1
        end = x
        mid = -1

        while( beg <= end ):
            mid = (beg+end)/2

            if( mid*mid == x):
                return mid

            if( mid*mid > x):
                end = mid-1
            else:
                beg = mid+1
        
        return mid
    
print(mySqrt(4))