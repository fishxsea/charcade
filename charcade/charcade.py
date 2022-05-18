import random, time, os
from itertools import permutations
from math import sqrt


class Arcade:

    '''
    Create animations for your CLI applications
    ---
    ---
    Parameters
    ---
    - word: String that you want to animate. 
    - flow: How fast the animation flow is. Default value is .1
    - color: Determines what color the text in the animation is. 
          Accepts color names and RGB values. RGB format: color='0,0,0' 
    ---
    ~Animation Types/Methods~
    ---
    - write -------/ Autotypes the string out.
    - casewave --/ Sends a wave of uppercase or lowercase letters across string.
    - shuffle -----/ Shuffles up the word.
    - slide -------/ Slides words right or left. 
    - load -------/ Loading animation.
    - stamp -----/ Stamps your string in place and goes to the next line.
    - flicker -----/ Flickers like a neon sign.
    - glitch ------/ Glitches text out.
    - erase ------/ Clears the terminal. Called by Arcade.erase() \n
    Example: \n
    ```
    Arcade.erase()
    my_string = 'charcade' 
    animation = Arcade(my_string, color='orange50') 
    animation.write() 
    animation.glitch()
    animation.stamp()
    ```
    ---
    ---
    All Colors
    ---
    
    ```
    > white, gray10, gray20, gray30, gray40, gray50, 
      gray60, gray70, gray80, gray90, black
    
    > red10, red20, red30, red40, red50, 
      red60, red70, red80, red90, red
    
    > orange10, orange20, orange30, orange40, orange50, 
      orange60, orange70, orange80, orange90, orange
    
    > yellow10, yellow20, yellow30, yellow40, yellow50, 
      yellow60, yellow70, yellow80, yellow90, yellow
    
    > green10, green20, green30, green40, green50, 
      green60, green70, green80, green90, green
    
    > blue10, blue20, blue30, blue40, blue50, 
      blue60, blue70, blue80, blue90, blue
    
    > purple10, purple20, purple30, purple40, purple50, 
      purple60, purple70, purple80, purple90, purple
    
    > pink10, pink20, pink30, pink40, pink50, 
      pink60, pink70, pink80, pink90, pink
    ```
    
    '''

    def __init__(self, word, color='', flow=.1):
        self.word = word
        self.color = color
        self.flow = flow

        colors = {
    
        # Red Scale
        'red10': '255;225;225m',
        'red20': '255;200;200m',
        'red30': '255;175;175m',
        'red40': '255;150;150m',
        'red50': '255;125;125m',
        'red60': '255;100;100m',
        'red70': '255;75;75m',
        'red80': '255;50;50m',
        'red90': '255;30;30m',
        'red':   '255;0;0m',

        'red orange': '255;60;0m',

        # Orange Scale
        'orange10': '255;240;215m',
        'orange20': '255;225;185m',
        'orange30': '255;210;155m',
        'orange40': '255;195;125m',
        'orange50': '255;180;95m',
        'orange60': '255;165;65m',
        'orange70': '255;150;35m',
        'orange80': '255;135;5m',
        'orange90': '255;120;0m',
        'orange':   '255;105;0m',

        # Yellow Scale
        'yellow10': '255;255;225m',
        'yellow20': '255;255;200m',
        'yellow30': '255;255;175m',
        'yellow40': '255;255;150m',
        'yellow50': '255;255;125m',
        'yellow60': '255;255;100m',
        'yellow70': '255;255;75m',
        'yellow80': '255;255;50m',
        'yellow90': '255;255;25m',
        'yellow':   '255;255;0m',
        
        'yellow green': '200;255;0m',

        # Green Scale
        'green10': '225;255;225m',
        'green20': '200;255;200m',
        'green30': '175;255;175m',
        'green40': '150;255;150m',
        'green50': '125;255;125m',
        'green60': '100;255;100m',
        'green70': '75;255;75m',
        'green80': '50;255;50m',
        'green90': '25;255;25m',
        'green':   '0;255;0m',

        'blue green': '0;255;180m',

        # Blue Scale
        'blue10': '225;225;255m',
        'blue20': '200;200;255m',
        'blue30': '175;175;255m',
        'blue40': '150;150;255m',
        'blue50': '125;125;255m',
        'blue60': '100;100;255m',
        'blue70': '75;75;255m',
        'blue80': '50;50;255m',
        'blue90': '25;25;255m',
        'blue':   '0;0;255m',

        # Purple Scale
        'purple10': '240;225;255m',
        'purple20': '225;200;255m',
        'purple30': '210;175;255m',
        'purple40': '195;150;255m',
        'purple50': '180;125;255m',
        'purple60': '165;100;255m',
        'purple70': '150;75;255m',
        'purple80': '145;50;255m',
        'purple90': '130;25;255m',
        'purple':   '115;0;255m',

        # Pink Scale
        'pink10': '255;220;250m',
        'pink20': '255;195;240m',
        'pink30': '255;170;230m',
        'pink40': '255;145;220m',
        'pink50': '255;120;210m',
        'pink60': '255;95;200m',
        'pink70': '255;70;190m',
        'pink80': '255;45;180m',
        'pink90': '255;25;170m',
        'pink':   '255;0;160m',

        # Gray Scale
        'white': '255;255;255m',
        'gray10': '225;225;225m',
        'gray20': '200;200;200m',
        'gray30': '175;175;175m',
        'gray40': '150;150;150m',
        'gray50': '125;125;125m',
        'gray60': '100;100;100m',
        'gray70': '75;75;75m',
        'gray80': '50;50;50m',
        'gray90': '30;30;30m',
        'black': '0;0;0m'
        }


        f = '\033[38;2;'

        if self.color != '':
            self.color = self.color.replace(' ', '')
            if self.color not in colors:
                self.color = f + self.color.replace(',',';') + 'm'
            else:
                self.color = f + colors[self.color]

    def write(self, pause=False):
        '''
        Takes no arguments. Simply writes your string out in the terminal.
        ---
        Does not accept lists.
        '''
        animation_slides = []
        count = 1
        for i in self.word:
            animation_slides.append(self.word[:count])
            count += 1

        punctuation = [',', '.', '!', '?']
        for slide in animation_slides:
            if pause == True:
                if slide[-1] in punctuation:
                    print(self.color + slide + '\033[0m', end='\r')
                    time.sleep(self.flow)
                    time.sleep(.3)
                else:
                    print(self.color + slide + '\033[0m', end='\r')
                    time.sleep(self.flow)
            if pause == False:
                print(self.color + slide + '\033[0m', end='\r')
                time.sleep(self.flow)
        
    def casewave(self, direction='right', cycles=1):
        '''
        ---
        Creates a casewave across your strings.\n
        ---
        Accepts 2 arguments: 
        - direction --/ args: right, left. Default: right
        - cycles -----/ accepts int as arg. The amount of times the animation occurs.
        ---
        Does not accept lists. \n
        '''
        animation_slides = []
        if direction == 'right':
            count = 0
            for i in self.word:
                if i.isupper():
                    i = i.lower()
                else:
                    i = i.upper()   
                animation_slides.append(self.word[:count] + i + self.word[count+1:])
                count += 1
        if direction == 'left':
            count = len(self.word)
            for i in self.word[::-1]:
                if i.isupper():
                    i = i.lower()
                else:
                    i = i.upper() 
                animation_slides.append(self.word[:count-1] + i + self.word[count:])
                count -= 1
        for i in range(cycles):
            for slide in animation_slides:
                print(self.color + slide + '\033[0m', end='\r')
                time.sleep(self.flow)
        
    def shuffle(self, cycles=10):
        '''
        Shuffles your strings.
        ---
        Accepts 1 argument.
        - cycles --/ accepts int as arg. The amount of times the animation occurs.
        ---
        Does not accept lists
        '''
        
        animation_slides = []
        for i in range(cycles):
            shufword = [letter for letter in self.word]
            random.shuffle(shufword)
            shufword = ''.join(shufword)
            animation_slides.append(shufword)
        for slide in animation_slides:
            print(self.color + slide + '\033[0m', end='\r')
            time.sleep(self.flow)

    def load(self, endofword='', cycles=1):
        '''
        Loading animation. The animation stays in place.
        ---
        Accepts 2 arguments.
        - endofword --/ put the string from other animations to put the loading animation at the end of the string.
        - cycles -------/ accepts int as arg. The amount of times the animation occurs.
        ---
        Accepts lists and strings
        '''
        animation_slides = []
        keepword = endofword
        for i in self.word:
            animation_slides.append(i)
        for i in range(cycles):
            for slide in animation_slides:
                print(self.color + keepword + slide + '\033[0m', end='\r')
                time.sleep(self.flow)

    def slide(self, direction='left', cycles=1):
        '''
        Creates a billboard like slide animation.
        ---
        Accepts 2 arguments.
        - direction ---/ args: right, left. Default: left
        - cycles ------/ accepts int as arg. The amount of times the animation occurs.
        ---
        Does not accept lists.
        '''
        animation_slides = []

        if direction == 'left':
            count = 0
            for i in self.word:
                animation_slides.append(self.word[count:] + self.word[:count])
                count += 1

        if direction == 'right':
            count = 0
            for i in self.word:
                animation_slides.append(self.word[count:] + self.word[:count])
                count -= 1
                
        for i in range(cycles):
            for slide in animation_slides:
                print(self.color + slide + '\033[0m', end='\r')
                time.sleep(self.flow)

    def glitch(self, cycles=35):
        
        '''
        Glitches text out in terminal.
        ---
        Does not accept lists.
        '''
        animation_slides = []
        letters_in_word = []

        for i in self.word:
            letters_in_word.append(i)
        square = sqrt(len(self.word))

        for i in range(cycles):
            new_word = letters_in_word
            for i in range(random.randint(1, int(square))):
                random_chars = random.choice(['',' ', 'x', '>', '<', '#', '_', '+', '$'])
                random_number = random.randint(0, len(letters_in_word)-1)
                new_word[random_number] = random_chars
            new_word = ''.join(new_word)

            if (random_number % 2) == 0:
                animation_slides.append(new_word)
            else:
                animation_slides.append(self.word)

            letters_in_word.clear()
            for i in self.word:
                letters_in_word.append(i)

        for slide in animation_slides:
            print(self.color + slide + '\033[0m', end='\r')
            random_number = random.randint(1, 10)
            if (random_number % 6) == 0:
                print(self.color + random.choice(['x', '#'])*len(self.word), end='\r')
                time.sleep(random.choice([.05, .07, .1, .3]))
                print(self.color + self.word + '\033[0m', end='\r')
                time.sleep(.03)

            time.sleep(self.flow)

    def shadeglitch(self, cycles=15):

        red_codes = [
            '\033[38;2;255;225;225m',
            '\033[38;2;255;200;200m',
            '\033[38;2;255;175;175m',
            '\033[38;2;255;150;150m',
            '\033[38;2;255;125;125m',
            '\033[38;2;255;100;100m',
            '\033[38;2;255;75;75m',
            '\033[38;2;255;50;50m',
            '\033[38;2;255;30;30m',
            '\033[38;2;255;0;0m'
        ]

        orange_codes = [
            '\033[38;2;255;240;215m',
            '\033[38;2;255;225;185m',
            '\033[38;2;255;210;155m',
            '\033[38;2;255;195;125m',
            '\033[38;2;255;180;95m',
            '\033[38;2;255;165;65m',
            '\033[38;2;255;150;35m',
            '\033[38;2;255;135;5m',
            '\033[38;2;255;120;0m',
            '\033[38;2;255;105;0m'
        ]

        yellow_codes = [
            '\033[38;2;255;255;225m',
            '\033[38;2;255;255;200m',
            '\033[38;2;255;255;175m',
            '\033[38;2;255;255;150m',
            '\033[38;2;255;255;125m',
            '\033[38;2;255;255;100m',
            '\033[38;2;255;255;75m',
            '\033[38;2;255;255;50m',
            '\033[38;2;255;255;25m',
            '\033[38;2;255;255;0m'
        ]

        green_codes = [
            '\033[38;2;225;255;225m',
            '\033[38;2;200;255;200m',
            '\033[38;2;175;255;175m',
            '\033[38;2;150;255;150m',
            '\033[38;2;125;255;125m',
            '\033[38;2;100;255;100m',
            '\033[38;2;75;255;75m',
            '\033[38;2;50;255;50m',
            '\033[38;2;25;255;25m',
            '\033[38;2;0;255;0m'
        ]
        
        blue_codes = [
            '\033[38;2;225;225;255m',
            '\033[38;2;200;200;255m',
            '\033[38;2;175;175;255m',
            '\033[38;2;150;150;255m',
            '\033[38;2;125;125;255m',
            '\033[38;2;100;100;255m',
            '\033[38;2;75;75;255m',
            '\033[38;2;50;50;255m',
            '\033[38;2;25;25;255m',
            '\033[38;2;0;0;255m'
        ]

        purple_codes = [
            '\033[38;2;240;225;255m',
            '\033[38;2;225;200;255m',
            '\033[38;2;210;175;255m',
            '\033[38;2;195;150;255m',
            '\033[38;2;180;125;255m',
            '\033[38;2;165;100;255m',
            '\033[38;2;150;75;255m',
            '\033[38;2;145;50;255m',
            '\033[38;2;130;25;255m',
            '\033[38;2;115;0;255m'
        ]

        pink_codes = [
            '\033[38;2;255;220;250m',
            '\033[38;2;255;195;240m',
            '\033[38;2;255;170;230m',
            '\033[38;2;255;145;220m',
            '\033[38;2;255;120;210m',
            '\033[38;2;255;95;200m',
            '\033[38;2;255;70;190m',
            '\033[38;2;255;45;180m',
            '\033[38;2;255;25;170m',
            '\033[38;2;255;0;160m'
        ]

        gray_codes = [
            '\033[38;2;255;255;255m',
            '\033[38;2;225;225;225m',
            '\033[38;2;200;200;200m',
            '\033[38;2;175;175;175m',
            '\033[38;2;150;150;150m',
            '\033[38;2;125;125;125m',
            '\033[38;2;100;100;100m',
            '\033[38;2;75;75;75m',
            '\033[38;2;50;50;50m',
            '\033[38;2;30;30;30m',
            '\033[38;2;0;0;0m'
        ]


        red = ['red50', 'red70', 'red']
        orange = ['orange50', 'orange70', 'orange']
        yellow = ['yellow50', 'yellow70', 'yellow']
        green = ['green50', 'green70', 'green']
        blue = ['blue50', 'blue70', 'blue']
        purple = ['purple50', 'purple70', 'purple']
        pink = ['pink50', 'pink70', 'pink']
        gray = ['white', 'gray30', 'gray50', 'gray70', 'black']

        
        if self.color in red_codes:
            col_list = red

        elif self.color in orange_codes:
            col_list = orange

        elif self.color in yellow_codes:
            col_list = yellow

        elif self.color in green_codes:
            col_list = green

        elif self.color in blue_codes:
            col_list = blue

        elif self.color in purple_codes:
            col_list = purple

        elif self.color in pink_codes:
            col_list = pink

        elif self.color in gray_codes:
            col_list = gray

        else:
            col_list = ['']

        for i in range(cycles):
            ani = Arcade(self.word, random.choice(col_list), self.flow)
            ani.glitch(cycles=2)
    
    def writeglitch(self):
        write_slides = []
        count = 1
        for i in self.word:
            write_slides.append(self.word[:count])
            count += 1
        for i in write_slides:
            ani = Arcade(i, self.color[:-1], self.flow)
            ani.glitch(cycles=1)

    def flicker(self, cycles=10):
        
        '''
        Flickers text like a billboard
        ---
        Does not accept lists.
        '''
        animation_slides = []
        letters_in_word = []
        for i in self.word:
            letters_in_word.append(i)
        
        for i in range(cycles):
            new_word = letters_in_word
            for i in range(random.randint(int(len(self.word)/2), int(len(self.word)))):
                random_chars = ' '
                random_number = random.randint(0, len(letters_in_word)-1)
                new_word[random_number] = random_chars
            new_word = ''.join(new_word)
            animation_slides.append(new_word)
            if (random_number % 2) == 0:
                animation_slides.append(self.word)
            letters_in_word.clear()
            for i in self.word:
                letters_in_word.append(i)
        
        for slide in animation_slides:
            print(self.color + slide + '\033[0m', end='\r')
            time.sleep(self.flow*random.choice([1, 1.1, 1.2, 1.5]))
            if slide == self.word:
                time.sleep(random.choice([.1, .2, .3, .4]))

    def pause(self, waittime=.4):
        time.sleep(waittime)

    def stamp(self, colorend=True):
        '''
        Put at the end of the animation sequence to paste your string in place.
        
        ---
        Takes 1 argument.
        - colorend --/ If set to False the terminal will retain color of the animation. Good for animated text input. \n
        Default: True
        '''
        if colorend == True:
            colend = '\033[0m'
        if colorend == False:
            colend = ''
        
        print(self.color + self.word + colend)

    def erase():

        '''
        Clears the terminal screen.
        '''
        os.system('cls' if os.name == 'nt' else 'clear')

    def clearline(self):
        print(' '*len(self.word), end='\r')

class Brute:
    '''
    Bruteforce Strings 
    ---
    ---
    Args
    ---
    - word: The string to bruteforce.
    ---
    ---
    Bruteforce Types/Methods
    ---
    - bulk ------/ Returns all string outcomes.
    - halfbulk --/ Returns all string outcomes with the same length.
    - genuine --/ Returns all string outcomes that are a real word.
    - bigfoot ---/ Returns all string outcomes with same length and if the word is real. \n
    Example: \n
        - my_string = 'lunch' \n
         brute = Brute(my_string) \n
         [print(word) for word in brute.genuine()]
    ---
    
    ---
    Note
    ---
    - Longer words will take significantly longer to calculate as every possible combination in the string is tested.
    '''

    def __init__(self, word):
        self.word = word

    def bulk(self):

        '''
        Returns a list with all possible word outcomes with recursion
        '''

        all_words = []
        used_letters = []
        # Returns all possible outcomes while being recursive 
        for letter in self.word:
            for i in range(1, len(self.word)+1):
                if letter not in used_letters:
                    combos =  map(''.join, permutations(self.word, i))
                    [all_words.append(c) for c in combos if c not in all_words] 
            used_letters.append(letter)    
        return all_words

    def halfbulk(self):
        '''
        Returns a list with all possible word outcomes without recursion
        '''
        all_words = []
        used_letters = []
        # Returns all possible outcomes without being recursive
        for letter in self.word:
            for i in range(len(self.word)):
                if letter not in used_letters:
                    combos =  map(''.join, permutations(self.word))
            [all_words.append(c) for c in combos if c not in all_words] 
        used_letters.append(letter)
        return all_words

    def genuine(self):

        '''
        Returns a list with all possible words that are real with recursion
        '''
        dirname, filename = os.path.split(os.path.abspath(__file__))
        real_words = []
        used_letters = []
        words_with_letter = []
        # Returns all real words while being recursive
        for firstletter in self.word:
            words_file = open(dirname + '/words_by_letter/' + firstletter + '.txt', 'r')
            for words in words_file:
                words_with_letter.append(words.strip())
            for i in range(1, len(self.word)+1):
                # Ensures that duplicate letters do not get re-bruteforced
                if firstletter not in used_letters:
                    combos =  map(''.join, permutations(self.word, i))
                    [real_words.append(c) for c in combos if c in words_with_letter and c not in real_words] 
            words_file.close()
            used_letters.append(firstletter)
        real_words.sort(key=len)
        return real_words 

    def bigfoot(self):
        '''
        Returns a list with all possible words that are real without recursion
        '''
        dirname, filename = os.path.split(os.path.abspath(__file__))
        real_words = []
        used_letters = []
        words_with_letter = []
        # Returns all real words without being recursive
        for firstletter in self.word:
            words_file = open(dirname + '/words_by_letter/' + firstletter + '.txt', 'r')
            for words in words_file:
                words_with_letter.append(words.strip())
            for i in range(len(self.word)):
                # Ensures that duplicate letters do not get re-bruteforced
                if firstletter not in used_letters:
                    combos =  map(''.join, permutations(self.word))
            [real_words.append(c) for c in combos if c in words_with_letter and c not in real_words]
            words_file.close()
            used_letters.append(firstletter)
        real_words.sort()
        return real_words

def color(word, fg=None, bg=None, colorend=True): 

    '''
    Colors for your strings. \n
    ---
    Parameters
    ---
    - word: The string that is inputted \n
    - fg: The color of the text. \n
    - bg: The color of the background. \n
    - colorend: Determines whether the color ends on the word or not. It is recommended to keep this at the default value of True.
    Examples:
    ```
    print(color('String', fg='blue', bg='black'))
    print(color('String', 'blue', 'black'))
    print(color('String', '0,0,255', '0,0,0'))
    ```
    returns: 'String' with text color as blue and background color as black. \n
    ---
    ~All Colors~
    ---
    
    ```
    > white, gray10, gray20, gray30, gray40, gray50, 
      gray60, gray70, gray80, gray90, black
    
    > red10, red20, red30, red40, red50, 
      red60, red70, red80, red90, red
    
    > orange10, orange20, orange30, orange40, orange50, 
      orange60, orange70, orange80, orange90, orange
    
    > yellow10, yellow20, yellow30, yellow40, yellow50, 
      yellow60, yellow70, yellow80, yellow90, yellow
    
    > green10, green20, green30, green40, green50, 
      green60, green70, green80, green90, green
    
    > blue10, blue20, blue30, blue40, blue50, 
      blue60, blue70, blue80, blue90, blue
    
    > purple10, purple20, purple30, purple40, purple50, 
      purple60, purple70, purple80, purple90, purple
    
    > pink10, pink20, pink30, pink40, pink50, 
      pink60, pink70, pink80, pink90, pink
    ```
    ---
    Accepts RGB values in place of color name in the format 'R,G,B'\n
    Example: \n
    ```
    print(color('String', '143,233,129'))
    ```
    '''

    # Colors
    colors = {
    
    # Red Scale
    'red10': '255;225;225m',
    'red20': '255;200;200m',
    'red30': '255;175;175m',
    'red40': '255;150;150m',
    'red50': '255;125;125m',
    'red60': '255;100;100m',
    'red70': '255;75;75m',
    'red80': '255;50;50m',
    'red90': '255;30;30m',
    'red':   '255;0;0m',

    'red orange': '255;60;0m',

    # Orange Scale
    'orange10': '255;240;215m',
    'orange20': '255;225;185m',
    'orange30': '255;210;155m',
    'orange40': '255;195;125m',
    'orange50': '255;180;95m',
    'orange60': '255;165;65m',
    'orange70': '255;150;35m',
    'orange80': '255;135;5m',
    'orange90': '255;120;0m',
    'orange':   '255;105;0m',

    # Yellow Scale
    'yellow10': '255;255;225m',
    'yellow20': '255;255;200m',
    'yellow30': '255;255;175m',
    'yellow40': '255;255;150m',
    'yellow50': '255;255;125m',
    'yellow60': '255;255;100m',
    'yellow70': '255;255;75m',
    'yellow80': '255;255;50m',
    'yellow90': '255;255;25m',
    'yellow':   '255;255;0m',
    
    'yellow green': '200;255;0m',

    # Green Scale
    'green10': '225;255;225m',
    'green20': '200;255;200m',
    'green30': '175;255;175m',
    'green40': '150;255;150m',
    'green50': '125;255;125m',
    'green60': '100;255;100m',
    'green70': '75;255;75m',
    'green80': '50;255;50m',
    'green90': '25;255;25m',
    'green':   '0;255;0m',

    'blue green': '0;255;180m',

    # Blue Scale
    'blue10': '225;225;255m',
    'blue20': '200;200;255m',
    'blue30': '175;175;255m',
    'blue40': '150;150;255m',
    'blue50': '125;125;255m',
    'blue60': '100;100;255m',
    'blue70': '75;75;255m',
    'blue80': '50;50;255m',
    'blue90': '25;25;255m',
    'blue':   '0;0;255m',

    # Purple Scale
    'purple10': '240;225;255m',
    'purple20': '225;200;255m',
    'purple30': '210;175;255m',
    'purple40': '195;150;255m',
    'purple50': '180;125;255m',
    'purple60': '165;100;255m',
    'purple70': '150;75;255m',
    'purple80': '145;50;255m',
    'purple90': '130;25;255m',
    'purple':   '115;0;255m',

    # Pink Scale
    'pink10': '255;220;250m',
    'pink20': '255;195;240m',
    'pink30': '255;170;230m',
    'pink40': '255;145;220m',
    'pink50': '255;120;210m',
    'pink60': '255;95;200m',
    'pink70': '255;70;190m',
    'pink80': '255;45;180m',
    'pink90': '255;25;170m',
    'pink':   '255;0;160m',


    # Gray Scale
    'white': '255;255;255m',
    'gray10': '225;225;225m',
    'gray20': '200;200;200m',
    'gray30': '175;175;175m',
    'gray40': '150;150;150m',
    'gray50': '125;125;125m',
    'gray60': '100;100;100m',
    'gray70': '75;75;75m',
    'gray80': '50;50;50m',
    'gray90': '30;30;30m',
    'black': '0;0;0m', 
    }

    f = '\033[38;2;'
    b = '\033[48;2;'

    if fg != None:
        fg = fg.replace(' ', '')
    if bg != None:
        bg = bg.replace(' ', '')

    rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
    if fg == 'rainbow' and bg == None:   
        rainbow_word = ''
        count = 0
        for letter in word:
            if count == len(rainbow):
                count = 0
            rainbow_word += f + colors[rainbow[count]] + letter + '\033[0m'
            count += 1
        return rainbow_word 

    if bg == 'rainbow' and fg == None:   
        rainbow_word = ''
        count = 0
        for letter in word:
            if count == len(rainbow):
                count = 0
            rainbow_word += b + colors[rainbow[count]] + letter + '\033[0m'
            count += 1
        return rainbow_word 

    if fg == 'rainbow' and bg != None:
        rainbow_word = ''
        count = 0
        for letter in word:
            if count == len(rainbow):
                count = 0
            rainbow_word += f + colors[rainbow[count]] + b + colors[bg] + letter + '\033[0m'
            count += 1
        return rainbow_word

    if bg == 'rainbow' and fg != None:
        rainbow_word = ''
        count = 0
        for letter in word:
            if count == len(rainbow):
                count = 0
            rainbow_word += f + colors[fg] + b + colors[rainbow[count]] + letter + '\033[0m'
            count += 1
        return rainbow_word
        

    if fg != None:

        if fg not in colors:
            foreground = f + fg.replace(',', ';') + 'm'
        else:
            foreground = f + colors[fg]

    if bg != None:
        if bg not in colors:
            foreground = f + bg.replace(',', ';') + 'm'
        else:
            background = b + colors[bg]

    if colorend == True:
        colorend = '\033[0m'
    elif colorend == False:
        colorend = ''
    
    if bg != None and fg == None:
        return background + word + colorend
    elif fg != None and bg != None:
        return foreground + background + word + colorend
    else:
        return foreground + word + colorend

def colorchart():
    red = ['red10', 
        'red20', 
        'red30', 
        'red40', 
        'red50', 
        'red60', 
        'red70', 
        'red80', 
        'red90', 
        'red'
    ]

    orange = ['orange10', 
            'orange20', 
            'orange30', 
            'orange40', 
            'orange50', 
            'orange60', 
            'orange70', 
            'orange80', 
            'orange90', 
            'orange'
    ]

    yellow = ['yellow10', 
            'yellow20', 
            'yellow30', 
            'yellow40', 
            'yellow50', 
            'yellow60', 
            'yellow70', 
            'yellow80', 
            'yellow90', 
            'yellow'
    ]

    green = ['green10', 
            'green20', 
            'green30', 
            'green40', 
            'green50', 
            'green60', 
            'green70', 
            'green80', 
            'green90', 
            'green'
    ]

    blue = ['blue10', 
            'blue20', 
            'blue30', 
            'blue40', 
            'blue50', 
            'blue60', 
            'blue70', 
            'blue80', 
            'blue90', 
            'blue'
    ]

    purple = ['purple10', 
            'purple20', 
            'purple30', 
            'purple40', 
            'purple50', 
            'purple60', 
            'purple70', 
            'purple80', 
            'purple90', 
            'purple'
    ]

    pink = ['pink10', 
            'pink20', 
            'pink30', 
            'pink40', 
            'pink50', 
            'pink60', 
            'pink70', 
            'pink80', 
            'pink90', 
            'pink'
    ]

    gray = ['gray10', 
            'gray20', 
            'gray30', 
            'gray40', 
            'gray50', 
            'gray60', 
            'gray70', 
            'gray80', 
            'gray90', 
            'black'
    ]

    sym = '█'
    count = 0
    counter = 10
    print(color(' '*79, bg='black'))
    print(color(' charcade color chart' + ' '*58, 'white', 'black'))
    print(color(' '*70 + f'white  {sym} ', 'white', 'black'))
    for i in range(10):
        bg = 'black'
        gray_col = 'gray'
        if counter == 100:
            counter = '  '
        if count == 9:
            gray_col = 'black'
        
        print(color(f' red{counter} {sym} ', red[count], bg) + 
            color(f'orange{counter} {sym} ', orange[count], bg) +
            color(f'yellow{counter} {sym} ',yellow[count], bg) +
            color(f'green{counter} {sym} ', green[count], bg) +
            color(f'blue{counter} {sym} ', blue[count], bg) +
            color(f'purple{counter} {sym} ', purple[count], bg) +
            color(f'pink{counter} {sym} ', pink[count], bg) +
            color(f'{gray_col}{counter} {sym}'.replace('  ', ' '), 
            gray[count], 'white') + color(' ', bg='black'))
        if counter == '  ':
            break
        count += 1
        counter += 10
    print(color(' '*79, bg='black'))

def palettes(name):

    retro_80s = ['pink', 'blue', 'green', 'yellow', 'black']

    soft_sun = ['orange40', 'orange60', 'red50','yellow', 'purple50']

    soft_moon = ['blue20', 'blue40','pink50', 'purple']

    watermelon = ['red10', 'red20', 'red30', 'red40', 'red50', 'red60', 'red70', 'red80', 'red90','red', 'green40','green70', 'black']

    spells = ['purple', 'blue50', 'purple30', 'pink', 'black', 'yellow']

    ice = ['white', 'gray20', 'gray40', 'gray60', 'blue30', 'blue50']

    fire = ['red', 'orange','orange70', 'orange50','orange30', 'yellow30', 'yellow']

    if name == 'retro 80s':
        return retro_80s
    if name == 'soft sun':
        return soft_sun
    if name == 'soft moon':
        return soft_moon
    if name == 'watermelon':
        return watermelon
    if name == 'spells':
        return spells
    if name == 'ice':
        return ice
    if name == 'fire':
        return fire