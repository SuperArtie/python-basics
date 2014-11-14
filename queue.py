class Queue:
    data = []
    def enqueue(self, name):
        self.data.append(name)
    def dequeue(self):
        self.data.remove(self.data[0])



pogz = Queue()
pogz.enqueue('limited edition alf pog')
pogz.enqueue('polly pocket pog set')
pogz.enqueue('jambalaya recipe pog')
pogz.dequeue()
print(pogz.data)
if 'bob' > 'cl':
    print('ffff')