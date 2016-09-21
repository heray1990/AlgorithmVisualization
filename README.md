# AlgorithmVisualization

## Table of Contents

- [System Requirement](https://github.com/heray1990/AlgorithmVisualization#system-requirement)
- [Bubble Sort](https://github.com/heray1990/AlgorithmVisualization#bubble-sort)
- [Insertion Sort](https://github.com/heray1990/AlgorithmVisualization#insertion-sort)

## System Requirement

- Ubuntu
- Python 2.7
- matplotlib

## Bubble Sort

As "[Introduction to Algorithms](https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844/ref=sr_1_1?ie=UTF8&qid=1474425705&sr=8-1&keywords=Introduction+to+Algorithms)" introduces, _Bubble Sort is a popular, but inefficient, sorting algorithm. **It works by repeatedly swapping adjacent elements that are out of order**_.

```
BUBBLE-SORT(A)
// A[1..n]
1 for i = 1 to n - 1
2     for j = 2 to n - i + 1
3         if A[j] < A[j - 1]
4             exchange A[j] with A[j - 1]
```

Download [src/visual_bubble_sort.py](https://github.com/heray1990/AlgorithmVisualization/blob/master/src/visual_bubble_sort.py) and run it in Linux. You will intuitively see how bubble sort works.

Run the command `python visual_bubble_sort.py -n 50`, you will get the animation as follow.

![bubble_sort_50samples_fps20_dpi50](https://raw.githubusercontent.com/heray1990/AlgorithmVisualization/master/images/bubble_sort_50samples_fps30_dpi50.gif)

If you want to save the animation into _\*.gif_ file, please run `python visual_bubble_sort.py -n 50 -o outputfile`. Then, you will get *outputfile.gif*.

## Insertion Sort

Insertion Sort is an efficient algorithm for sorting a small number of elements. **It splits a sequence into two parts, sorted sequence and unsorted one. Get an element from unsorted sequence and insert the element into the correct position in the sorted part. Do not stop until there is no element in unsorted part.**

"[Introduction to Algorithms](https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844/ref=sr_1_1?ie=UTF8&qid=1474425705&sr=8-1&keywords=Introduction+to+Algorithms)" gives an excellent example to explain this, _Insertion sort works the way many people sort a hand of playing cards. We start with an empty left hand and the cards face down on the table. We then remove one card at a time from the table and insert it into the correct position in the left hand. To find the correct position for a card, we compare it with each of the cards already in the hand, from right to left. At all times, the cards held in the left hand are sorted, and these cards were originally the top cards of the pile on the table._

![sorting_cards_using_insertion_sort](https://raw.githubusercontent.com/heray1990/AlgorithmVisualization/master/images/sorting_cards_using_insertion_sort.png)

```
INSERTION-SORT(A)
// A[1..n]
1 for j = 2 to n
2     key = A[j]
3     // Insert A[j] into the sorted sequence A[1..j - 1].
4     i = j - 1
5     while i > 0 and A[i] > key
6         A[i + 1] = A[i]
7         i = i - 1
8     A[i + 1] = key
```

![sorting_cards_using_insertion_sort](https://raw.githubusercontent.com/heray1990/AlgorithmVisualization/master/images/insertion_sort.png)