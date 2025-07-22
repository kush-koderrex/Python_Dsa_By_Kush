count = 0

def func():
    global count
    # if count == 4:
    #     return
    print(f'{count} kush')
    count += 1
    func()

func()
