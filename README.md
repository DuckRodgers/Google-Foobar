# Google-Foobar
The snips of codes developed during the Google-Foobar challenge.

## A Little Context
In case you're not familiar with the Google-Foobar challenge, the first question is why are you here? Just kidding. The Foobar is a secret challenge which may precede a recruitment process done by Google. This is their equivalent of a CV reading, except instead of being open, is _super secret_, except for the thousands of git repositories and posts about it you can find online.

Legends says if you pass the third phase you get an interview with someone from Google. If you go through Quora and Reddit this checks out.

If, like me, you aren't from TI as your original academic formation, then you must imagine what an incredible feeling I got when not only I got the invite but decided to google it and find out what it actually meant. So... this are my code snips which I used to pass from the first and second phase. At the moment I'm still completing the challenge, now entering the **Second Level - Second Challenge**, and 100% hyped up about it.

## The First Level
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

## The Second Level - Second Challenge
Happily past the first round, our adventure must go on. Pretty excited and confident, I was thinking "huh, getting into Google isn't _that_ hard", I put on my best pompous mask and requested the second challenge. This was a saturday morning, because I worked so I wanted to have as much time as possible to crack this.

Good news: My strategy worked out fine, because I needed every single minute for this.

### The Challenge
Long story short: **Commander LAMBCHOP** has a ion-flux machine which is conveniently built as a **perfect binary tree**. Unluckily (for her), the ion-flux machine broke down, and all the labels from the components got misplaced. The minions are now manually trying to figure out the best to way fix them, but you believe you can do it faster because, and check this out, the tree is built in a **post-order traverse** fashion.

First things first: It's a real bummer that they don't teach us this kinds of things in petroleum engineering.
