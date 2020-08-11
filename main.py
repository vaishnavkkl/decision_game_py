print('welcome to the game')
name = input('what is your name: ')
age = int(input('what is your age: '))
print('hello', name, 'you are', age, 'years old')
cond = True
while cond:
    if age <= 10:
        print('game only for above age of 10')
        break
    else:
        play = input('do you wanna play(yes/no)').lower()
        if play == 'yes':
            print('lets play')
            left_right = input('first choice....left or right (left/right)?').lower()
            if left_right == 'right':
                ans = input('nice, you followed the correct path and reached at a lake...'
                            'do you wanna swim or go through bridge(swim/bridge)?').lower()
                if ans =='swim':
                    print('you are killed by an crocodile and you loss')
                else:
                    print('you passed the lake safely and won the game')
                again = input('do you wanna play again(yes/no)?')
                if again =='yes':
                    cond =True
                else:
                    cond = False

            else:
                print('you loss')
        else:
            print('game ended')