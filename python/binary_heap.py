class MinBinaryHeap():
  def __init__(self):
    self.heapList = [0]
    self.currentSize = 0

  def insert(self, val: int) -> None:
    self.heapList.append(val)
    self.currentSize += 1
    self._percolateUp(self.currentSize)

  def _percolateUp(self, i: int) -> None:
    while i // 2 > 0:
      if self.heapList[i] < self.heapList[i // 2]:
        temp = self.heapList[i // 2]
        self.heapList[i // 2] = self.heapList[i]
        self.heapList[i] = temp
      i = i // 2

  def _percolateDown(self, i: int) -> None:
    while i * 2 <= self.currentSize:
      mc = self._minChild(i)
      if self.heapList[i] > self.heapList[mc]:
        temp = self.heapList[i]
        self.heapList[i] = self.heapList[mc]
        self.heapList[mc] = temp
      i = mc

  def _minChild(self, i: int) -> None:
    if i * 2 + 1 > self.currentSize:
      return i * 2
    else:
      return i * 2 if self.heapList[i*2] < self.heapList[i*2+1] else i * 2 + 1

  def deleteMin(self) -> int:
    retVal = self.heapList[1]
    self.heapList[1] = self.heapList[self.currentSize]
    self.currentSize -= 1
    self.heapList.pop()
    self._percolateDown(1)
    return retVal

  def getMin(self) -> int:
    return self.heapList[1]

  def buildHeap(self, alist: list):
    i = len(alist) // 2
    self.currentSize = len(alist)
    self.heapList = [0] + alist[:]
    while i > 0:
      self._percolateDown(i)
      i -= 1

  def __str__(self):
    return str(self.heapList[1:])

class MaxBinaryHeap:
  def __init__(self):
    self.heapList = [0]
    self.currentSize = 0

  def _percolateUp(self, i: int) -> None:
    while i // 2 != 0:
      if (self.heapList[i] > self.heapList[i // 2]):
        temp = self.heapList[i // 2]
        self.heapList[i // 2] = self.heapList[i]
        self.heapList[i] = temp
      i = i // 2

  def _percolateDown(self, i: int) -> None:
    while i * 2 <=  self.currentSize:
      mc = self._maxChild(i)
      if self.heapList[i] < self.heapList[mc]:
        temp = self.heapList[mc]
        self.heapList[mc] = self.heapList[i]
        self.heapList[i] = temp
      i = mc

  def deleteMax(self) -> int:
    retVal = self.heapList[1]
    self.heapList[1] = self.heapList[self.currentSize]
    self._percolateDown(1)
    self.heapList.pop()
    self.currentSize -= 1
    return retVal

  def getMax(self):
    return self.heapList[1]

  def _maxChild(self, i: int) -> None:
    if i * 2 + 1 > self.currentSize:
      return i * 2
    else:
      return i * 2 if self.heapList[i * 2] > self.heapList[i * 2 + 1] else i * 2 + 1

  def insert(self, x: int) -> None:
    self.heapList.append(x)
    self.currentSize += 1
    self._percolateUp(self.currentSize)

  def buildHeap(self, alist: list) -> None:
    i = len(alist) // 2
    self.currentSize = len(alist)
    self.heapList = [0] + alist[:]
    while i > 0:
      self._percolateDown(i)
      i = i - 1

  def __str__(self):
    return str(self.heapList[1:])

if __name__ == "__main__":
  bh = MaxBinaryHeap()
  bh.buildHeap([9, 3, 7, 2, 4, 10])
  print(bh)