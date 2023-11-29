import pygame
import random
import time
import threading
import multiprocessing
from Balls.methood1 import ball
'''Method 1 : using a semaphore'''

def print_process(queue, semaphore):
    while True:
        message = queue.get()
        if message == "STOP":
            break
        with semaphore:
            print(message)

def print_process2(semaphore):
    while True:
        #with semaphore:
            state = f"Semaphore state: {semaphore.get_value()}"
            print(state)

def run_ball_thread(screen, id, queue, semaphore):
    with semaphore:
        queue.put(f"{id}- start, balls on screen: {threading.active_count() - 1}")
    num_of_appearances = random.randint(12, 20)
    ball_instance = ball.Ball(screen, semaphore)
    for _ in range(num_of_appearances):
        ball_instance.move()
    with semaphore:
        queue.put(f"{id}- end, balls on screen: {threading.active_count() - 2}")

def update_screen(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()  # Update the display

def main():
    while True:
        num_of_threads = input("Enter the number of balls you would like to see: \n")
        if not num_of_threads.isdigit():
            print("This isn't a number. try again")
        else:
            num_of_threads = int(num_of_threads)
            if num_of_threads < 1 or num_of_threads > 20:
                print("This number is not valid (range is: 1 - 20)")
            else:
                print("Number of balls= " + str(num_of_threads))
            break

    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Set your screen size here
    pygame.display.set_caption("Random Moving Balls")

    threads = []

    # Create a queue and semaphore for printing messages
    message_queue = multiprocessing.Queue()
    semaphore = multiprocessing.Semaphore(value=1)  # Set the initial value

    # Create a printing process
    printing_process = multiprocessing.Process(target=print_process, args=(message_queue, semaphore))
    printing_process.start()

    # # Uncomment the following lines if you want to see the semaphore state
    # printing_process2 = multiprocessing.Process(target=print_process2, args=(semaphore,))
    # printing_process2.start()

    for x in range(num_of_threads):
        ball_thread = threading.Thread(target=run_ball_thread, args=(screen, x + 1, message_queue, semaphore))
        threads.append(ball_thread)

    for thread in threads:
        thread.start()  # Start all threads

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()  # Update the display
        if threading.active_count() - 1 == 0:
            break

    message_queue.put("STOP")  # Signal the print process to stop
    printing_process.join()  # Wait for the printing process to finish

    # Release resources
    semaphore.release()
    pygame.quit()

if __name__ == "__main__":
    main()
