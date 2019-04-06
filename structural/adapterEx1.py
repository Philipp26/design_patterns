class Target():    
    def request(self) -> str:
        return "Target: the deafault target`s behavior"


class Adaptee():
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self):
        return f'Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}'

def client_code(target: Target) -> None:
    print(target.request(), end ='')

print("Client: I can work just fine with the target objects")
target = Target()
client_code(target)
print('\n')

adaptee = Adaptee()
print("Client: The Adaptee class has a weird interface. See, i don`t understand it")
print(f"Adaptee: {adaptee.specific_request()}", end='\n\n')

print("Client: But i can work with it via the Adapter.")
adapter = Adapter(adaptee)
client_code(adapter)
print('\n')





