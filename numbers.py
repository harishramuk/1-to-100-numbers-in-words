n = int(input('enter the numbers 1 to 100:'))
output = ''
word_ones = [' ','one','two','three','four',
             'five','six','seven','eight','nine','ten',
             'eleven','twelve','thirteen','fourteen',
             'fifteen','sixteen','seventine','eighteen',
             'ninteen']
word_tens = ['','','twenty','thirty','fourty','fifty',
             'sixty','seventy','eighty','ninty']
if n ==0:
    print('zero')
elif n<=19:
    print(word_ones[n])
elif n<=100:
    print((word_tens[n//10])+' '+(word_ones[n%10]))
else:
    print('n is not in bettwin for 1 to 100:')

print('branch test')
print('fork test')
print('resolving merge confilicts')
print('harishramuk77')
    
