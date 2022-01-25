
# charcade

charcade is a string manipulation library that can animate, color, and bruteforce strings.


## Features

- Animating text for CLI applications with easy to use syntax.
- Coloring text with easy to use syntax.
- Bruteforce strings showing all possible outcomes, or real words that are hidden within.


## Usage

### **Arcade class**
***

***This class is for animating text.***

__There are currently 5 animation types.__

- write()
> *Writes your string out like a typewriter.*
- casewave()
> *Sends a casewave across your string.*
- slide()
> *Slides your string like a billboard.*
- shuffle()
> *Randomly shuffles your string.*
- load()
> *Creates an in-place animation. Accepts lists and strings.*

**Lets look at an example of some code.**

```python
from charcade import Arcade

# This will clear your terminal for cleaner looking applications.
Arcade.erase()


# The 'flow=' parameter controls the animation speed. default value is .1
animation = Arcade('charcade charcade', 'light orange', flow=.08)

# To create an animation sequence simply do this.
animation.write()
animation.casewave()
animation.casewave('left')
animation.slide()
animation.slide('right')
animation.casewave()
animation.casewave('left')

# Without stamp() your animation will stack ontop of itself
# It is recommended to use this at the end of every animation sequence
animation.stamp() 
```

---
### **Brute class**
***
***This class is for brute-forcing strings***

__There are 4 ways to brute-force your strings.__

- bulk()
> *Returns a list of all possible combinations of your string.*
- halfbulk()
> *Returns a list of all possible combinations of your string that are the same length.*
- genuine()
> *Returns a list of all possible combinations of your string that are real words.*
- bigfoot()
> *Returns a list of all possible combinations of your string that are real words and the same length as your string.* 

**Lets look at an example of some code.**

```python
from charcade import Brute

words = Brute('ports').bigfoot()

# Since Brute returns a list we're going to iterate over it and print.
for word in words:
    print(word)
```
**Output:**
```
ports
prost
sport
sprot
strop
```

---
### **color method**

***This method is for coloring strings***

*There are currently 26 colors to choose from although you are not
limited to just the available colors.*

*This method also accepts RGB values in place of the color for the 
fg color and bg color.*

*All colors here are also available in **Arcade***

**Lets look at an example of some code.**

```python
from charcade import color

my_string = 'charcade'

print(color(my_string, fg='red', bg='black'))
# OR
print(color(my_string, fg='255,0,0', bg='0,0,0'))

# Both will output the same thing since RGB values are accepted as colors.
```
**Available colors:**

---
```
red
red orange
light orange
orange
yellow
yellow green
green
blue green
light blue
blue
violet
purple
light pink
pink
hot pink

white
gray 10
gray 20
gray 30
gray 40
gray 50
gray 60
gray 70
gray 80
gray 90
black
```
***
# Roadmap

- *Add more animation styles*
- *Add custom tailored color palettes for your apps*
- *Autocorrect*
- *Word mixing to create new words*
- *Show definitions of words*

