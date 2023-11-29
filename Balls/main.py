import pygame
import random
import time
import threading
import multiprocessing
from Balls.methood1 import ball  # Import the Ball class from the Balls module
''' Method 1: Using the pygame.display (= screen) in order to check color
    where you want to print the ball - appears inside ball class'''

def print_process(queue):
    while True:
        message = queue.get()
        if message == "STOP":
            break
        print(message)


def run_ball_thread(screen, id, queue):
    queue.put(f"{id}- start, balls on screen: {threading.active_count() - 1}")
    num_of_appearances = random.randint(12, 20)
    ball_instance = ball.Ball(screen)
    for _ in range(num_of_appearances):
        ball_instance.move()
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

    # Create a queue and process for printing messages
    message_queue = multiprocessing.Queue()
    printing_process = multiprocessing.Process(target=print_process, args=(message_queue,))
    printing_process.start()

    for x in range(num_of_threads):
        ball_thread = threading.Thread(target=run_ball_thread, args=(screen, x + 1, message_queue))
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

    pygame.quit()


if __name__ == "__main__":
    main()
