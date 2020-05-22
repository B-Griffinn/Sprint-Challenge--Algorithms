#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) Linear O(n) bc as n grows so does a on line 11.
Example input 1 then our loop runs 1 time,
input = 10 then our loop runs 10 times and so on.

b) for loop = O(n) && while loop is O(log n) bc we are stopping once j is == n
Being that we are looping through the same list twice our run time grows at a larger rate than the input.
Best Case is O(log n)
Worst Case is O(n ^ 2)

c) This is a Recursive function and it loops n number of times, n being our input aka bunnies. No matter what `bunnies` is, we will loop that many times.
Best case is that bunnies == 0 making it O(1)
Worst case is O(n)

## Exercise II

Being that we are given a building with floors we can assume that this buidling in equivelant to a sorted list being that floors start at 0/1 and go up by 1 each floor.
In this case we can use a binary search approach.

With the given list we will need to initialize 3 variables before we do anything. Those vars are: Left_pointer, Right_pointer, Middle_pointer.

We can now loop through our arr while the left pointer is less than or equal to our right pointer.

We need to update our Middle_pointer to be half of the length of the list which is Left_pointer + right_pointer divided by 2.

Create a var to store the new middle index. Fond_var = list at index middle.

Now we need to compare our found to our target floor.
If the found_var is our middle on the first loop then we have found the floor and our time complexity is O(1)

If found_var is less than the target floor then we need to update our left pointer to be the middle + 1 index becasue we now need to eliminate the left hand side of our ordered list.
Keep looping until found is met.

If found_var is greater than the target floor then we need to update our right pointer to be the middle - 1 index becasue we now need to eliminate the right hand side of our ordered list.
Keep looping until found is met.

Best case this searching method is O(1) if our condition is met on first loop.
Otherwise it is O(log n). We are cutting the list in half every loop in this case, which is great!!
