# It's been a few weeks since I wrote some python, since I have an English
# class with many assignments to worry about.

def count():
    import random
    top = raw_input('count up to: ')
    try:
        top = int(top)
    except:
        return
    for i in range(top):
        print random.randint(1,top)

count()

# looking back on this, I hope you know I was being silly by printing
# random numbers.
