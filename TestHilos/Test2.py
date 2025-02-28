from multiprocessing import Process, freeze_support  # Use multiprocessing, not multiprocessing.dummy































def foo():
    while True:
        x = 2

def main():
    print('hello')

p = Process(target=foo)  # Creating a new process
p.start()  # Start the process

if __name__ == '__main__':
    # freeze_support()  # Commented out to trigger the error
    main()
