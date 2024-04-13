import time 
seconds=input("enter the time in number of seconds :")


def countdown_timer(seconds):
    mins=int(seconds/60)
    secs=int(seconds%60)
    timer=f'{mins}:{secs}'
    print(timer) 
    seconds-=1
    print('time up!!!!')

countdown_timer(int(seconds))