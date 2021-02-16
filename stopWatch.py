import time 

def timeCon(s):
    min= s // 60
    s = s % 60 
    h = min % 60
    print('time: {0}:{1}:{2}'.format(int(h),int(min),s))


input('clique sur un boutton pour commence')
start_time = time.time()

input('clique sur un boutton pour stp')
end_time = time.time()

time_lapset = end_time - start_time
if __name__ == '__main__':
    res = timeCon(time_lapset)
    print(res)
