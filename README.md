# charcade

charcade is a string manipulation library that can animate, color, and bruteforce strings.

## Features

- Animating text for CLI applications with easy to use syntax.
- Coloring text with easy to use syntax.
- Bruteforce strings showing all possible outcomes, or real words that are hidden within.

## Usage

### **Arcade class**

---

**_This class is for animating text._**

**_General Functions_**

- Arcade.erase() # Clears Terminal
- Arcade("text here", "color here").clearline() # Clears current line of animation.

**There are currently 9 animation types.**

- write()
  > _Writes your string out like a typewriter._
- casewave()
  > _Sends a casewave across your string._
- slide()
  > _Slides your string like a billboard._
- shuffle()
  > _Randomly shuffles your string._
- load()
  > _Creates an in-place animation. Accepts lists and strings._
- flicker()
  > _Flickers your string like a neon sign._
- glitch()
  > _Glitches your string out._
- shadeglitch()
  > _Glitches your string out with flashing shades of the color in your Arcade object_
- writeglitch()
  > _Glitches out strings as they're typed out in the terminal_

**Lets look at an example of some code.**

```python
from charcade import Arcade

# This will clear your terminal for cleaner looking applications.
Arcade.erase()


# The 'flow=' parameter controls the animation speed. default value is .1
animation = Arcade('charcade charcade', 'orange40', flow=.08)

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

---

**_This class is for brute-forcing strings_**

**There are 4 ways to brute-force your strings.**

- bulk()
  > _Returns a list of all possible combinations of your string._
- halfbulk()
  > _Returns a list of all possible combinations of your string that are the same length._
- genuine()
  > _Returns a list of all possible combinations of your string that are real words._
- bigfoot()
  > _Returns a list of all possible combinations of your string that are real words and the same length as your string._

**Lets look at an example of some code.**

```python
from charcade import Brute

words = Brute('ports').bigfoot()

# Since Brute returns a list we're going to iterate over it and print each element.
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

**_This method is for coloring strings_**

_There are currently 26 colors to choose from although you are not
limited to just the available colors._

_This method also accepts RGB values in place of the color for the
fg color and bg color._

\*All colors here are also available in **Arcade\***

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
white, gray10, gray20, gray30, gray40, gray50,
gray60, gray70, gray80, gray90, black

red10, red20, red30, red40, red50,
red60, red70, red80, red90, red

orange10, orange20, orange30, orange40, orange50,
orange60, orange70, orange80, orange90, orange

yellow10, yellow20, yellow30, yellow40, yellow50,
yellow60, yellow70, yellow80, yellow90, yellow

green10, green20, green30, green40, green50,
green60, green70, green80, green90, green

blue10, blue20, blue30, blue40, blue50,
blue60, blue70, blue80, blue90, blue

purple10, purple20, purple30, purple40, purple50,
purple60, purple70, purple80, purple90, purple

pink10, pink20, pink30, pink40, pink50,
pink60, pink70, pink80, pink90, pink
```

---

# Roadmap

- _Add more animation styles_
- _Add custom tailored color palettes for your apps_
- _Autocorrect_
- _Word mixing to create new words_
- _Show definitions of words_
- _Color blending functionality_
