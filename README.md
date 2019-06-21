#  Algorithms in Bioinformatics SoSe 2019
Programming tasks from the exercise-sheets.

##  Topics
* Exercise-Sheet 1
	* Random Numbers
	* Hamming-Distance
* Exercise-Sheet 2
	* First Occurrence
	* Multiset
	* d-Neighbourhood

---

###  Random Numbers | Exercise-Sheet 1
Write a program that keeps printing integers between 0 and 50 until the number 42 appears. 
Print the total number of generated integers at the end.

###  Hamming-Distance | Exercise-Sheet 1
Given to strings of same length, calculate their `Hamming-Distance`.

---

### First Occurrence | Exercise-Sheet 2
Given a long text `String T`, a shorter pattern `String s`, and an `integer k`, give an algorithm that finds the first occurrence in `T` of a string (if any) `s'` such that `dH(s, s') <= k` What is the complexity of your algorithm? `O(len(T) * len(s))`

### Multiset | Exercise-Sheet 2
A multiset is a set that allows duplicate elements (e.g. `{2, 2, 3, 3, 4, 5}` is a multiset with duplicate
elements `2` and `3`). If `X = {x1 = 0, x2, . . . , xn}` is a set of `n` points on a line segment in increasing
order, then `∆X` denotes the multiset of all `N chooose 2` pairwise distances between points in `X`: 
`∆X = {xj - xi | 1 <= i < j <= n}`<br>
For example, if `X = {0, 2, 4, 7, 10}`, then `∆X = {2, 2, 3, 3, 4, 5, 6, 7, 8, 10}`.<br>
Describe an algorithm that, given a set `X`, calculates the multiset `∆X`.

### d-Neighbourhood | Exercise-Sheet 2
Given a k-mer pattern `x`, we define its d-neighbourhood as the set of all k-mers that have a Hamming-Distance of at most `d` from the k-mer pattern `x`.<br>For example, given the pattern 
`x = ‘ACG’` and `d = 1`,<br>`d_neighbourhood = {‘ACG’, ‘CCG’, ‘GCG’, ‘TCG’, ‘AAG’, ‘AGG’, ‘ATG’, ‘ACA’, ‘ACC’, ‘ACT’}`. Describe an algorithm, that calculates the d-Neighbourhood.