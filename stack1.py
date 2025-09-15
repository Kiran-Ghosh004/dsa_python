MAX = 5  # maximum size of stack
stack = [0] * MAX
top = -1

def isFull():
    return top == MAX - 1

def isEmpty():
    return top == -1

def push(x):
    global top
    if isFull():
        print("Stack Overflow")
    else:
        top += 1
        stack[top] = x
        print(x, "pushed")

def pop():
    global top
    if isEmpty():
        print("Stack Underflow")
    else:
        val = stack[top]
        top -= 1
        return val

def peek():
    if isEmpty():
        print("Stack is Empty")
    else:
        return stack[top]

def display():
    if isEmpty():
        print("Stack is Empty")
    else:
        print("Stack elements (top to bottom):")
        for i in range(top, -1, -1):
            print(stack[i])

# Example usage
push(10)
push(20)
push(30)
display()
print("Peek:", peek())
print("Pop:", pop())
display()

