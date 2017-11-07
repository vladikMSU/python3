from collections import deque

def createGenerator(n) :
    cur_buf = deque()
    new_buf = deque()
    
    prev = '1'
    cur_n = 1

    for i in range(n+1) :
        
        if not cur_buf or prev != cur_buf[0]:
            new_buf.extend(str(cur_n)+prev)
            cur_n = 1
        else :
            cur_n += 1

        yield prev

        if not cur_buf :
            cur_buf = new_buf
            new_buf = deque()

        prev = cur_buf.popleft()

    

n = int(input())

conwayGenerator = createGenerator(n)

for i in range(n+1) :
    ans = next(conwayGenerator)
    
print(ans)