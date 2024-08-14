
import time

def stop_watch():
    """
    This function simulates a stopwatch. It starts when the user presses Enter and stops when the user presses Enter again.
    Args:
        None
        Returns:
            None
    """
    input("Press Enter to start the stopwatch")
    start_time=time.time()

    input("Press Enter to stop the stopwatch")
    end_time=time.time()
    
    elapsed_time=end_time-start_time
    print("Elapsed time is: ",elapsed_time)


def main():
    stop_watch()

main()