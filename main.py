import threading

counter = 0

def increment():
    global counter
    for _ in range(1000000):
        counter += 1

def decrement():
    global counter
    for _ in range(1000000):
        counter -= 1

def race():
    # Create two threads: one for incrementing and one for decrementing
    thread1 = threading.Thread(target=increment)
    thread2 = threading.Thread(target=decrement)
    
    # Start both threads
    thread1.start()
    thread2.start()
    
    # Wait for both threads to finish
    thread1.join()
    thread2.join()
    
    # Print the final value of the counter
    print("Result: ", counter)

if __name__ == '__main__':
    race()
