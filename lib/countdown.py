# your code goes here!

def count_down(integer):
    while integer>0:
        print(f'{integer} SECONDS(S)')
        if integer==1:
            print('Happy New Year')
        integer-=1
count_down(integer=20)
