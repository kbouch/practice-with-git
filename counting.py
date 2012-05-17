def count():
    top = raw_input('count up to: ')
    try:
        top = int(top)
    except:
        return
    for i in range(1,top+1):
        print i

count()
