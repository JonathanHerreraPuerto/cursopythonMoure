"""
Pilas y Colas
"""

# Pila/Stack (LIFO)

stack = []

stack.append("1")
stack.append("2")
stack.append("3")
print(stack)

#pop

stack_item = stack[len(stack)-1]
del stack[len(stack)-1]

print(stack_item)

print(stack.pop())

print(stack)

print("---------------------------------")
# Cola/Queue

queue = []

# enqueue
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)

# dequeue
queue_item=queue[0]
del queue[0]
print(queue_item)

print(queue.pop(0))

print(queue)

"""
Extra
"""
# Web

def web_navigation():
    
    stack = []
    
    while True:
        action = input(
            "Añade una url o interactúa con las palabras adelante/atrás/salir:"
        )
        
        if action == "salir":
            print("Saliendo del navegador web.")
            break
        if action == "adelante":
            pass
        if action == "atrás":
            if len(stack) > 0:
                stack.pop()
        else:
            stack.append(action)
        if len(stack) > 0:   
            print(f"Has navegado a la web:{stack[len(stack)-1]}")
        else:
            print("Estas en la pagina de inicio.")        
    
#web_navigation()    

print("-----------------------------------------")

def shared_printed():
    queue = []
    while True:
        action = input("Añade un documento o selecciona imprimir/salir:")
        
        if action == "salir":
            break
        elif action == "imprimir":
            if len(queue) > 0:
                print(f"Imprimiendo:{queue.pop(0)}")
        else:
            queue.append(action)
            
        print(f"Cola de impresión: {queue}")
        
shared_printed()                
