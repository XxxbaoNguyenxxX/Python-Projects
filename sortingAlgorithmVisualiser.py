import pygame
import random, time, sys
pygame.init()
dimensions = (1600, 800)
display = pygame.display.set_mode((dimensions[0], dimensions[1]))
display.fill(pygame.Color("black"))

class Algorithm:
    def __init__(self, name):
        self.array = random.sample(range(800), 800)
        self.name = name
    def updateDisplay(self, swapBlock1=None, swapBlock2=None):
        update(self, swapBlock1, swapBlock2)
    def run(self):
        self.startTime = time.time()
        self.algorithm()
        timeElapsed = time.time() - self.startTime
        return self.array, timeElapsed

class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            minIndex = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[minIndex]:
                    minIndex = j
            self.array[i], self.array[minIndex] = self.array[minIndex], self.array[i]
            self.updateDisplay(self.array[i], self.array[minIndex])

class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            key = self.array[i]
            j = i
            while j > 0 and key < self.array[j-1]:
                self.array[j] = self.array[j-1]
                j -= 1
            self.array[j] = key
            self.updateDisplay(self.array[j], self.array[i])

class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self, array = [] , start=0, end=0):
        if array == []:
            array = self.array
            end = len(array) - 1
        if start < end:
            pivot = self.partition(array,start,end)
            self.algorithm(array,start,pivot - 1)
            self.algorithm(array,pivot + 1,end)

    def partition(self, array, start, end):
        x = array[end]
        i = start-1
        for j in range(start, end + 1, 1):
            if array[j] <= x:
                i += 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                    self.updateDisplay(array[i], array[j])
        return i

class HeapSort(Algorithm):
    def __init__(self):
        super().__init__("HeapSort")

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.array[i] < self.array[left]:
            largest = left
        if right < n and self.array[largest] < self.array[right]:
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.updateDisplay(self.array[i], self.array[largest])
            self.heapify(n, largest)

    def algorithm(self):
        n = len(self.array)
        for i in range(n,-1,-1):
            self.heapify(n, i)
        for i in range(n-1,0,-1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(i, 0)

class RadixSort(Algorithm):
    def __init__(self):
        super().__init__("RadixSort")

    def algorithm(self):

        def counting_sort(self, exp):
            output = [0] * len(self.array)
            count = [0] * (10)
            for i in range(0, len(self.array)):
                idx = (self.array[i]//exp)
                count[int((idx)%10)] += 1
            for i in range(1,10):
                count[i] += count[i-1]
            i = len(self.array)-1
            while i >= 0:
                idx = (self.array[i]/exp)
                output[count[int((idx)%10)]-1] = self.array[i]
                count[int((idx)%10)] -= 1
                i -= 1
            i = 0
            for i in range(len(self.array)):
                self.array[i] = output[i]
                self.updateDisplay(self.array[i])

        maximum = max(self.array)
        exp = 1
        while maximum // exp > 0:
            counting_sort(self, exp)
            exp *= 10

class ShellSort(Algorithm):
    def __init__(self):
        super().__init__("ShellSort")

    def algorithm(self):
        gap = len(self.array) // 2

        while gap > 0:
            for i in range(gap,len(self.array)):
                temp = self.array[i]
                j = i
                while j >= gap and self.array[j-gap] > temp:
                    self.array[j] = self.array[j-gap]
                    j -= gap
                self.array[j] = temp
                self.updateDisplay(self.array[j], self.array[self.array[i]])
            gap //= 2

class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)-1-i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
            self.updateDisplay(self.array[j], self.array[j+1])

class CocktailSort(Algorithm):
    def __init__(self):
        super().__init__("CocktailSort")

    def algorithm(self):
        swapped = True
        start = 0
        end = len(self.array) - 1
        while swapped == True:
            swapped = False
            for i in range(start, end):
                if (self.array[i] > self.array[i+1]):
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
                    swapped = True
            self.updateDisplay(self.array[i], self.array[self.array[i+1]])
            if swapped == False:
                break
            swapped == False
            end -= 1
            for i in range(end-1, start-1, -1):
                if self.array[i] > self.array[i+1]:
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
                    swapped = True
            self.updateDisplay(self.array[i], self.array[self.array[i+1]])
        start += 1

class GnomeSort(Algorithm):
    def __init__(self):
        super().__init__("GnomeSort")

    def algorithm(self):
        idx = 0
        while idx < len(self.array):
            if idx == 0:
                idx += 1
            if self.array[idx] >= self.array[idx - 1]:
                idx += 1
            else:
                self.array[idx], self.array[idx-1] = self.array[idx-1], self.array[idx]
                self.updateDisplay(self.array[idx], self.array[self.array[idx-1]])
                idx -= 1

algorithms = {0: SelectionSort(),
1: InsertionSort(),
2: QuickSort(),
3: HeapSort(),
4: RadixSort(),
5: ShellSort(),
6: BubbleSort(),
7: CocktailSort(),
8: GnomeSort()}

def closeWindow():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit();
            sys.exit();

        if event.type == pygame.KEYDOWN:
            main()

def update(algorithm, swapBlock1=None, swapBlock2=None, display=display):
    display.fill(pygame.Color("black"))
    pygame.display.set_caption("Sorting Algorithm Visualiser    Algorithm: {}   Time: {:.3f}    Status: Sorting".format(algorithm.name, time.time() - algorithm.startTime))

    blockWidth = int(dimensions[0]/len(algorithm.array))
    arrayDimensionRatio = int(dimensions[1]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        blockColor = "white"
        if swapBlock1 == algorithm.array[i]:
            blockColor = "green"
        elif swapBlock2 == algorithm.array[i]:
            blockColor = "red"
        pygame.draw.rect(display, blockColor, (i*blockWidth, dimensions[1] - algorithm.array[i]*arrayDimensionRatio, blockWidth, algorithm.array[i]*arrayDimensionRatio))
    closeWindow()
    pygame.display.update()

def updateBefore(algorithm, display=display):
    display.fill(pygame.Color("black"))
    pygame.display.set_caption("Sorting Algorithm Visualiser    Algorithm: {}   Status: Not Sorting".format(algorithm.name))

    blockWidth = int(dimensions[0]/len(algorithm.array))
    arrayDimensionRatio = int(dimensions[1]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        pygame.draw.rect(display, "white", (i*blockWidth, dimensions[1] - algorithm.array[i]*arrayDimensionRatio, blockWidth, algorithm.array[i]*arrayDimensionRatio))
    pygame.display.update()

def continueRun(algorithm, display, time):
    pygame.display.set_caption("Sorting Algorithm Visualiser    Algorithm: {}   Time: {:.3f}    Status: Done".format(algorithm.name, time))
    pygame.display.update()

def main():
    algoNum = 0
    run = True
    while run:
        sorting = False
        algorithm = algorithms[algoNum]
        updateBefore(algorithm)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_RETURN:
                print("Enter Key")
                sorting = True
            elif event.key == pygame.K_RIGHT and algoNum != len(algorithms)-1:
                print("Right Arrow Key")
                algoNum += 1
                algorithm = algorithms[algoNum]
                updateBefore(algorithm)
            elif event.key == pygame.K_LEFT and algoNum != 0:
                print("Left Arrow Key")
                algoNum -= 1
                algorithm = algorithms[algoNum]
                updateBefore(algorithm)
        if sorting:
            try:
                timeElapsed = algorithm.run()[1]
                continueRun(algorithm, display, timeElapsed)
                time.sleep(2)
                algorithm.array = random.sample(range(800), 800)
            except:
                pass

if __name__ == "__main__":
    main()
