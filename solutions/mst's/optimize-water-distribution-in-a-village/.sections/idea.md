Problem statement :

Given an integer N, where N denotes the number of villages numbered 1 to N, an array wells[] where wells[i] denotes the cost to build a water well in the i'th city, a 2D array pipes in form of [X Y C] which denotes that the cost to connect village X and Y with water pipes is C. Your task is to provide water to each and every village either by building a well in the village or connecting it to some other village having water. Find the minimum cost to do so.

- imp point is we want to connect to water supply and this can be done by using a well or connecting with other houses which have water supply.
- So if houses are points on a graph and pipes work as edges b/w them and consider wells as a water supply point which has edge with evry node 
- So Now problem becomes simple MST problem and we find using Krushkal's or prim's