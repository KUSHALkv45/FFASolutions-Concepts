```
Krushkal's TC : if N- vertices and pipes are "edges" - given constraint <= N we add N more to it 
so they are total of 2*N in krushkal's we sort them so O(NlogN) 

and then traversing and using union find (constant time O(4alpha) ) - so total will be O(NlogN + N)

SC : O(2N)

```