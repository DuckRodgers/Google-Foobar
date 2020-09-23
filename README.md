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
### The Solution
This one was pretty straightforward. Given a number, such as 12m², calculate the panel sizes that can be installed to fill the whole thing. 3m by 3m panels (3x3) return a total of 9m², and the remaining 3m² of area (12-9) need to be filled by 1x1 solar panels. There wasn't a lot of tricks being pulled out of the hat with this one, just a basic loop
