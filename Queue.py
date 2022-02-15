class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, element):
        self.data.append(element)
    
    def dequeue(self):
        if len(self.data) > 0:
            return self.data.pop(0)
        else:
            return False

    def read(self):
        if len(self.data) > 0:
            return self.data[0]
        else:
            return False
            
class ServerManager:
    def __init__(self):
        self.queue = Queue()
    
    def queue_enter_server(self, IP):
        self.queue.enqueue(IP)
    
    def run(self):
        while self.queue.read():
            print(self.queue.dequeue())

server_manager = ServerManager()
server_manager.queue_enter_server("IP1")
server_manager.queue_enter_server("IP2")
server_manager.queue_enter_server("IP3")
server_manager.run()