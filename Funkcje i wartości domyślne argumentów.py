def BuyMe(prefix='Please buy me', what='something nice'):
    print(prefix, what)


BuyMe('Please buy me', 'a new car')
BuyMe(prefix='Please buy me', what='a car')
BuyMe(what='a brand new car', prefix='Please buy me')
BuyMe('Please')
BuyMe(prefix='Please buy me')
BuyMe(what='something sweet')

# ćwiczenia

def show_progress(how_many, character = '*'):
    line = character * how_many
    print(line)

show_progress(10)
show_progress(15)
show_progress(30)

show_progress(10,'-')
show_progress(15,'+')