class Stack:
    def __init__(self):
        self.list = [] # -------------> Time Complixety = O(1), Space Complixety = O(1)
    
    def __str__(self) -> str:
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)