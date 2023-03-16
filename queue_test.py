from queue import Queue

queue1 = Queue(3)
queue1.add(1)
queue1.print_content()
queue1.add(2)
if not queue1.is_ready():
    print('ready ok')
else:
    print('ready failed')
queue1.print_content()
queue1.add(3)
queue1.print_content()
queue1.add(4)
queue1.print_content()
avg = queue1.get_avg()
if avg == (2 + 3 + 4) / 3:
    print('avg ok')
else:
    print('avg failed')

print(queue1.get_avg())
if queue1.is_ready():
    print('ready, ok.')
else:
    print('ready failed')
