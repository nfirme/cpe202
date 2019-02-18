import random
import time

def selection_sort(list):
    count = 0

    for i in range(len(list) - 1):
        min_pos = i

        for j in range(i + 1, len(list)):
            count += 1
            if list[j] < list[min_pos]:
                min_pos = j

        temp = list[i]
        list[i] = list[min_pos]
        list[min_pos] = temp

    return count

def insertion_sort(list):
    count = 0

    for i in range(1, len(list)):
        current = list[i]
        position = i

        count += 1
        while position > 0 and list[position - 1] > current:
            list[position] = list[position - 1]
            position = position - 1
            count += 1

        list[position] = current

    return count
   

def main():
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 32000)
    start_time = time.time() 
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

