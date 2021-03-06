# Google-Foobar
The snips of codes developed during the Google-Foobar challenge.

## Table of Content
1. [The First Challenge](#Level1) - More Square More Roots
2. [The Second Challenge - Level 1](#level2A) - The Perfect Binary Tree of Life
3. [The Second Challenge - Level 2](#level2B) - The Midnight Base Gospel
4. [The Third Challenge - Level 1](#level3A) - Lo0per

## A Little Context
In case you're not familiar with the Google-Foobar challenge, the first question is why are you here? Just kidding. The Foobar is a secret challenge which may precede a recruitment process done by Google. This is their equivalent of a CV reading, except instead of being open, is _super secret_, except for the thousands of git repositories and posts about it you can find online.

Legends says if you pass the third phase you get an interview with someone from Google. If you go through Quora and Reddit this checks out.

If, like me, you aren't from TI as your original academic formation, then you must imagine what an incredible feeling I got when not only I got the invite but decided to google it and find out what it actually meant. So... this are my code snips which I used to pass from the first and second phase. At the moment I'm still completing the challenge, now entering the **Second Level - Second Challenge**, and 100% hyped up about it.

## The First Level <a name="Level1"></a> - More Square More Roots
When you first open the challenge there is a small sci-fi story to get you going. I am **COMPLETELY ENGAGED** into this weird bunny terminator thing they have going on. I don't know who wrote it, but it feels like a Tim Burton meets J.J. Abrams vibe to it, I am _into_ this thing, like I would buy the novelization and everything.

Long story short: you (a spy) have infiltrated the base of the evil **Commander Lambchop** who has kidnapped your buddies, but you are on the lowest of the lowest hierarchy level, just a poor minion, far away from everyone relevant in the organization. Except, behold, you just might get your chance to rise up the ranks in the best John Connor fashion. **Evil Commander Lambchop** has a DOOMSDAY machine which needs a lot of power, and she needs to quickly calculate how many solar panels would be necessary to power it.

### The Challenge
Create a function that accepts an integer varying from 1 to 1.000.000 (inclusive) standing for the total area of solar panels (int x is x² units of area) that returns a list containing the solar panel sizes you need to fill it. If you had a total area of 12 square yards of solar material, you would be able to make one 3x3 square panel (with a total area of 9). That would leave 3 square yards, so you can turn those into three 1x1 square solar panels. So your function would look like:
```
input: solution.solution(9)
output: [9,1,1,1]
```
### [The Solution](first-challenge.py)
This one was pretty straightforward. Given a number, such as 12m², calculate the panel sizes that can be installed to fill the whole thing. 3m by 3m panels (3x3) return a total of 9m², and the remaining 3m² of area (12-9) need to be filled by 1x1 solar panels. While the input is greater than 1 and less than 1.000.000, run the following logic:

**Some backtesting:**
```
x = 8m².
Then --> root = int(x ** 0.5) --> Approximately 2
         solution = [2]
         x = x - root ** 2 --> x = 8 - 2 ** 2
         root = int(x ** 0.5) --> 2
         solution = [2,2]
         x = x - root ** 2 --> x = 4 - 2 ** 2
```
         
Since the output required by the challenge was "2,2", I used from __future__ import print_function. Complete success! We were able to win **LAMBCHOP's** attention and go to **LEVEL 2!**

## The Second Level - First Challenge <a name="Level2A"></a> - The Perfect Binary Tree of Life
Happily past the first round, our adventure must go on. Pretty excited and confident, I was thinking "huh, getting into Google isn't _that_ hard", I put on my best pompous mask and requested the second challenge. This was a saturday morning, because I worked so I wanted to have as much time as possible to crack this.

Good news: My strategy worked out fine, because I needed every single minute for this.
Bad news: Getting into Google isn't easy, it isn't easy **at all**. I was wrooooooong!

### The Challenge
Long story short: **Commander LAMBCHOP** has a ion-flux machine which is conveniently built as a **perfect binary tree**. Unluckily (for her), the ion-flux machine broke down, and all the labels from the components got misplaced. The minions are now manually trying to figure out the best to way fix them, but you believe you can do it faster because, and check this out, the tree is built in a **post-order traverse** fashion.

First things first: It's a real bummer that they don't teach us this kinds of things in petroleum engineering. This is why engineering is going to waste.
In case you don't know what a binary tree is, the best way to define it is a group of objects (called **nodes**), where each node contain a self value and may contain two children, a **left node** and a  **right node**. A **Perfect Binary Tree** is a tree where each and every node of the Tree contains exactly two children, so, for example, a Binary Tree of Height 3 would look something like this:
```
         X
       /   \
      Y     Z
     / \   / \
    W1 W2 W3 W4
```
OK, so that settles the first part, but how about the **post-order traversal** which definitely sounds like something you'd want to say on a dinner when meeting your boyfriend/girlfriend's family. Well, I had to google that bit a little bit, and the concept is actually pretty simple: a **post-order traversal** is a way to create a binary tree, in which the logical filling guide happens:
```
Step 1: Try to reach the node's left children.
Step 2: If not possible, try to reach the node's right children.
Step3: If not possible, return the value of the node.
```
### [The Solution](second-chall-level1.py)
Not going to lie, I spent 50% of my time trying to understand this problem. Because I'm an engineer, my first instinct was trying to understand the functioning logic of the example trees they provided, so I tested my hypothesis and for the tree of height 3 it worked perfectly. Then I tried to assemble the tree of height 5, and to my surprise... it failed. I cracked my head around a bit and did some research, until I found out how was the _actual_ logic behind it.

Once I got that out of the way, the next step was trying to understand **how to actually do the thing**. There are plenty of algorithms in the internet about post-order traversals, except all of them take into consideration you're building your tree randomly. **We aren't**, the top-most value will always be the number x = (2^h - 1), where h is the heigth of the tree. So, for a tree of height 3, the top-most value will be 7. Then, you need to start filling the tree in order, with values from 1 to "x" as given above. The "1" has to be the lower-most left value in the tree, then "2" will be the lower-most right children... ok, that was weird, here it is:
```
         7
       /   \
      3     6
     / \   / \
    1  2  4   5
```
The first thing is: **OOP** is fundamental here. I saw some people filling this with lists, which was even my first guess, but when I tried to implement I started hitting brick walls. My second guess was dictionaries, but I soon dropped that. OOPs was the way to go. Another keyword was **Recurssion**. This is one of those topics which every (non-programmer) python learner reads and thinks: "yeah, I'll definitely never use that". Unless you want to make **factorials**, in which case you'd better.

Well, to my surprise, I had to take that out of my toolbox and use it as well.

```
The logic behind the algorithm is very simple:
1) First check in which **level** you are, that is, the **heigth** of the tree. If you are not on the lower-most level, then you can keep on going down.
2) Check to see if the left children is empty. 
2.1) If it is, create a Node on it with value 0 and change that children's **level** to self+1.
2.2) If it's Node(0), then start the **recurssion** using that left children as the new reference node (basically I called this _go down_).
2.3) If it's not empty nor Node(0), check its own value.
2.3.1) If self value is Node(0):
2.3.1.1) Repeat step 2.1) except now for the right leg.
2.3.1.2) If none of that worked, change self value to the number you're currently trying to attribute.
3) If all of the above failed, check if right leg is None.
3.1) If not, create Node(0).
3.2) If right leg's value is already Node(0), start **recurssion** using that node as reference.
3.3) If all else fails, change self value to the number you're currently trying to attribute.
```
Wheew! I mean, **hard**. The worse part wasn't programming it _per se_, but trying to come up with the logic. Recurssion wasn't something I use daily, so adding that and understanding how I could make it work was a little bit challenging, but it all turned out great at the end and Google hir...

**WAIT**. We have _created_ the tree, but the challenge asked for something different. What **LAMBCHOP** actually wants is the following:

```
Given a function solution(h,q), where h is the height of the tree and q is a list of integers, return a list of integers with the positions of the nodes above the ones provided in each q element, and if there isn't any, return -1.

Example: input solution(3,[1,2,6,7]) outputs [3,3,7,-1].
```
So, it's not the tree itself, but the numbers above it!!!

This was actually more simple. We needed **recurssion** again, and the checking procedures were as follows:
```
1) First check if the number provided is less than the value in the left leg. If positive, make a recurssion at the left leg.
2) If not, check self value. If it's the same as the number provided, return self value.
3) If not, check to see if the number provided is less than the value in the right leg. If positive, make a recurssion at the right leg.
4) If not, check self value. If it's the same as the number provided, return self value.
```
And so, for a solution(3, [1,2,7,6]) we have an output:
```
[3,3,-1,7]
```
We passed all the tests, but I'm not entirely sure this code is without errors, so feel free to jiggle it a bit!

## The Second Level - Second Challenge <a name="Level2B"></a> - The Midnight Base Gospel
With the head fuming for the first challenge of the second level, I went fully prepared (and aware) of the dangers ahead. As any motivational coach would say, we need to change our mindset, and my mindset was: _this will be hard_.

So, things we learned from the previous phase: before programming, _read_ carefully the problem and write down keywords which might help solving the problem.

On the little sci-fi story they have going on, in order to keep impressing **COMMANDER LAMBCHOP** we are given a new problem: she has an algorithm that awards duties for the minions, and it receives the ID from the minion, creates two numbers from it, one in descending order, the other in ascending, and then subtracts one from the other, generating a new number to repeat the process and choose the next minion's ID. Problem is: the algorithm enters in an infinite loop after some trials.

### The Challenge
Given a def solution(n,b), where n is an non-negative integer and b is given integer's base (binary, ternary, etc), indicate after how many different inputs does the algorithm starts looping.

The algorithm from **COMMANDER LAMBCHOP** did this:

```
1) Receive a non-negative integer n
2) Reorder such number by descending order and ascending (variables x,y)
3) Subtract z = x-y. If z has a length smaller than the original n, add a '0' in front until it doesn't.
4) n = z
```
For example, for:
```
Input: def solution(1211, 3):
Output: 1
```

### [The Solution](second-chall-level2.py)
What happens in the code is pretty fun. The first interesting thing is how binaries work (and other bases as well). I didn't really learn a lot about binaries in Petroleum Engineering, so absolutely everything was uncharted territory for me. I did a research (quick one, though) on how to transform different-base numbers and different-base operations (different as in 'not base 10'). The idea was pretty straigthforward: get two numbers in different bases, convert them to base 10, do the operation, and finally return the result in the given base. Now, before the criticism rain starts pouring in, I did thought about simply doing the operation in the original base, but it was 11pm and I was really sleepy, so I went with what came first.

I created two functions, **def convert_10** and **convert_base** and they respectively convert any number to base 10 and convert any base-10 number to a different base. Then, I accept the user's input and start looping through the numbers. If the number I am adding to the list ``` is in ``` the **answer list**, then I stop the loop and return the length of the list minus the last available index, and...

And that's pretty much it! I mean, there is definitely room for improvement in this code, but I wrote it specifically well aware of its flaws and how I _could_ improve it, but again, wasn't really going for performance in this one. Other than that, I think it was pretty simple, considerably easier than the phase 1. There were about 10 tests, and all of them passed, so _yupiii_. On the other hand, I finished writing the code at around 11h30pm, but only actually submitted it on the other day around 16h00pm, so Google will think it took me longer than what it actually did...

Here I am now, ready and eager for Phase 3!

**Oh, and, btw, I did get the token!!** I shared it with a friend of mine who is a pretty good programmer. What surprised me from this part is that I got _one_ token invite, not _two_ as people were pointing out there, so, **disappointed**. But happy.

Mainly happy.

#BringLevel3

## The Third Level - First Challenge <a name="Level3A"></a> - Lo0per
I was feeling pumped. Ever watched "The Big Short"? Know that "jacked to the t#ts" scene from it? That's how I'm feeling. *Shane, Shane (stares at Shane until he leaves)*. That's pretty much how I felt by the beginning of the challenge.

As always, things we learned from the past phases was to pay attention to keywords from the text
