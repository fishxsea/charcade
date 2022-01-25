import random, string, time
from itertools import permutations
import os

def color(word, fg=None, bg=None, colorend=True) -> str: 

    '''
    Colors for your strings. \n
    ---
    Args 
    ---
    - word: The string that is inputted \n
    - fg: The color of the text. \n
    - bg: The color of the background. \n
    - colorend: Determines whether the color ends on the word or not. It is recommended to keep this at the default value of True.


    Examples: \n
    - print(color('String', fg='light blue', bg='black'))
    - print(color('String', 'light blue', 'black')) \n
    returns: 'String' with text color as light blue and background color as black. \n

    ---
    All Colors
    ---
    
    - red, red orange, orange, light orange, yellow, yellow green, green, blue green, light blue, blue, violet, purple, light pink, pink, hot pink
    ---
    - white, gray 10, gray 20, gray 30, gray 40, gray 50, gray 60, gray 70, gray 80, gray 90, black

    --- 
    Accepts RGB values in place of color name in the format 'R,G,B'\n
    Example: \n
    print(color('String', '143,233,129'))
    '''


    # If any color are added add them to the color_list
    color_list = ['red', 'red orange', 'light orange', 'orange', 'yellow','yellow green', 'green', 'blue green', 'blue','violet', 'purple','light pink', 'pink','hot pink', 'light blue', 'white','gray 10','gray 20','gray 30', 'gray 40','gray 50', 'gray 60','gray 70','gray 80','gray 90', 'black']

    # Colors
    red = '255;0;0m'
    red_orange = '255;60;0m'
    orange = '255;140;0m'
    light_orange = '255;200;0m'
    yellow = '255;255;0m'
    yellow_green = '200;255;0m'
    green = '0;255;0m'
    blue_green = '0;255;180m'
    blue = '0;0;255m'
    light_blue = '0;130;255m'
    violet = '85;0;255m'
    purple = '150;85;220m' 
    light_pink = '255;150;255m'
    pink = '255;80;255m'
    hot_pink = '255;0;200m'

    # Gray Scale
    white = '255;255;255m'
    gray_10 = '225;225;225m'
    gray_20 = '200;200;200m'
    gray_30 = '175;175;175m'
    gray_40 = '150;150;150m'
    gray_50 = '125;125;125m'
    gray_60 = '100;100;100m'
    gray_70 = '75;75;75m'
    gray_80 = '50;50;50m'
    gray_90 = '30;30;30m'
    black = '0;0;0m'
    f = '\033[38;2;'
    b = '\033[48;2;'

    if fg != None:
        if fg not in color_list:
            fg = f + fg.replace(',', ';') + 'm'
        if fg == 'red':
            fg = f + red
        if fg == 'red orange':
            fg = f + red_orange
        if fg == 'orange':
            fg = f + orange
        if fg == 'light orange':
            fg = f + light_orange
        if fg == 'yellow':
            fg = f + yellow
        if fg == 'yellow green':
            fg = f + yellow_green
        if fg == 'green':
            fg = f + green
        if fg == 'blue':
            fg = f + blue
        if fg == 'light blue':
            fg = f + light_blue
        if fg == 'blue green':
            fg = f + blue_green
        if fg == 'violet':
            fg = f + violet
        if fg == 'purple':
            fg = f + purple
        if fg == 'light pink':
            fg = f + light_pink
        if fg == 'pink':
            fg = f + pink
        if fg == 'hot pink':
            fg = f + hot_pink

        # Gray scale
        if fg == 'white':
            fg = f + white
        if fg == 'gray 10':
            fg = f + gray_10
        if fg == 'gray 20':
            fg = f + gray_20
        if fg == 'gray 30':
            fg = f + gray_30
        if fg == 'gray 40':
            fg = f + gray_40
        if fg == 'gray 50':
            fg = f + gray_50
        if fg == 'gray 60':
            fg = f + gray_60
        if fg == 'gray 70':
            fg = f + gray_70
        if fg == 'gray 80':
            fg = f + gray_80
        if fg == 'gray 90':
            fg = f + gray_90
        if fg == 'black':
            fg = f + black


    # Background colors
    if bg != None:
        if bg not in color_list:
            bg = b + bg.replace(',', ';') + 'm'
        if bg == 'red':
            bg = b + red
        if bg == 'red orange':
            bg = b + red_orange
        if bg == 'orange':
            bg = b + orange
        if bg == 'light orange':
            bg = b + light_orange
        if bg == 'yellow':
            bg = b + yellow
        if bg == 'yellow green':
            bg = b + yellow_green
        if bg == 'green':
            bg = b + green
        if bg == 'blue':
            bg = b + blue
        if bg == 'light blue':
            bg = b + light_blue
        if bg == 'blue green':
            bg = b + blue_green
        if bg == 'violet':
            bg = b + violet
        if bg == 'purple':
            bg = b + purple
        if bg == 'light pink':
            bg = b + light_pink
        if bg == 'pink':
            bg = b + pink
        if bg == 'hot pink':
            bg = b + hot_pink

        # Gray scale
        if bg == 'white':
            bg = b + white
        if bg == 'gray 10':
            bg = b + gray_10
        if bg == 'gray 20':
            bg = b + gray_20
        if bg == 'gray 30':
            bg = b + gray_30
        if bg == 'gray 40':
            bg = b + gray_40
        if bg == 'gray 50':
            bg = b + gray_50
        if bg == 'gray 60':
            bg = b + gray_60
        if bg == 'gray 70':
            bg = b + gray_70
        if bg == 'gray 80':
            bg = b + gray_80
        if bg == 'gray 90':
            bg = b + gray_90
        if bg == 'black':
            bg = b + black


    if colorend == True:
        colorend = '\033[0m'

    elif colorend == False:
        colorend = ''
    
    if bg != None and fg == None:
        return bg + word + colorend

    elif fg != None and bg != None:
        return fg + bg + word + colorend
    
    else:
        return fg + word + colorend

'''
def cipher(word, crypt, shift, includespaces=True, alph='all_alph'):
    
    Creates a Caesar Cipher of a string. \n
    --- \n
    Args \n
    - word: The string that is inputted \n
    - crypt: 'e' for encrypt. 'd' for decrypt. \n
    - shift: The shift for the cipher. \n
    - includespaces: True is default. If set to false then spaces in word will not be accounted for. Default: True \n
    - alph: Type of alphabet to use. \n alph options: upper, lower, and all_alph. Default: all_alph\n
    --- 
    Example: \n
    Lunch.cipher('String', 'e', 10)   ->   '2DBsxq'
    

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    all_alpha = string.ascii_letters + string.digits + string.punctuation

    if includespaces == True:
        space = ' '
    if includespaces == False:
        space = ''

    if alph == 'all_alph':
        alph = all_alpha + space
    if alph == 'upper':
        alph = upper + space
    if alph == 'lower':
        alph = lower + space
    
    if crypt == 'e':
        shift = shift
    if crypt == 'd':
        shift = shift * -1

    ciph = ''
    for i in range(len(word)):
        char = word[i]
        loc = alph.find(char)
        new_loc = (loc + (shift)) % len(alph)
        ciph += alph[new_loc]
    return ciph
'''
'''
TODO
def allwords(alph, wordlength=None, wordamount=1, inword=False):

    words = []

    
    if wordamount != 1 and alph != 'random':
        print('\nWord amount can only be used with random as alph parameter.\n')
        exit()

    # Logic for random
    if (alph, wordlength, wordamount) == ('random', wordlength, wordamount):
        if wordamount == 1 and wordlength == None:
            return [random.choice(words)]

        elif wordamount > 1 and wordlength == None:
            return [random.choice(words) for i in range(wordamount)]

        else:
            word_list = [w for w in words if len(w) == wordlength]
            return [random.choice(word_list) for i in range(wordamount)]

    # Logic for words
    if type(alph) is int:
        return [w for w in words if len(w) == alph]

    if inword == True and alph != 'random':
        if wordlength != None:
            word_list = [w for w in words if len(w) == wordlength and alph in w]
            return [w for w in word_list]
        elif wordlength == None:
            return [w for w in words if alph in w]
            


    elif type(wordlength) is int:
        word_list = [w for w in words if len(w) == wordlength]
        return [w for w in word_list if w[0:len(alph)] == alph]
        
    
    elif type(alph) is str:
        return [w for w in words if w[0:len(alph)] == alph]
'''

class Arcade():

    '''
    Create animations for your CLI applications
    ---
    ---
    Args 
    ---
    - word: String that you want to animate. 
    - flow: How fast the animation flow is. Default value is .1
    - color: Determines what color the text in the animation is. 
          Accepts color names and RGB values. RGB format: color='0,0,0' 

    ---
    Animation Types/Methods
    ---
    - write -------/ Autotypes the string out.
    - casewave --/ Sends a wave of uppercase or lowercase letters across string.
    - shuffle -----/ Shuffles up the word.
    - slide -------/ Slides words right or left. 
    - load -------/ Loading animation.
    - stamp -----/ Stamps your string in place and goes to the next line.
    - erase ------/ Clears the terminal. Called by Arcade.erase() \n
    Example: \n
    - my_string = 'charcade' \n
         animation = Arcade(my_string, color='light orange', flow=.1) \n
         animation.write() \n
    ---
    ---
    All Colors
    ---
    
    - red, red orange, orange, light orange, yellow, yellow green, green, blue green, light blue, blue, violet, purple, light pink, pink, hot pink
    ---
    - white, gray 10, gray 20, gray 30, gray 40, gray 50, gray 60, gray 70, gray 80, gray 90, black
    
    '''

    def __init__(self, word, color='', flow=.1):
        self.word = word
        self.color = color
        self.flow = flow
        

        # Add colors to this list when new colors are added
        color_list = ['red', 'red orange', 'light orange', 'orange', 'yellow','yellow green', 'green', 'blue green', 'blue','violet', 'purple','light pink', 'pink','hot pink', 'light blue', 'white','gray 10','gray 20','gray 30', 'gray 40','gray 50', 'gray 60','gray 70','gray 80','gray 90', 'black']

        red = '255;0;0m'
        red_orange = '255;60;0m'
        orange = '255;140;0m'
        light_orange = '255;200;0m'
        yellow = '255;255;0m'
        yellow_green = '200;255;0m'
        green = '0;255;0m'
        blue_green = '0;255;180m'
        blue = '0;0;255m'
        light_blue = '0;130;255m'
        violet = '85;0;255m'
        purple = '150;85;220m' 
        light_pink = '255;150;255m'
        pink = '255;80;255m'
        hot_pink = '255;0;200m'

        white = '255;255;255m'
        gray_10 = '225;225;225m'
        gray_20 = '200;200;200m'
        gray_30 = '175;175;175m'
        gray_40 = '150;150;150m'
        gray_50 = '125;125;125m'
        gray_60 = '100;100;100m'
        gray_70 = '75;75;75m'
        gray_80 = '50;50;50m'
        gray_90 = '30;30;30m'
        black = '0;0;0m'
        f = '\033[38;2;'
        b = '\033[48;2;'

        # Colors
        if self.color != '':
            if self.color not in color_list:
                self.color = f + self.color.replace(',', ';') + 'm'
            if self.color == 'red':
                self.color = f + red
            if self.color == 'red orange':
                self.color = f + red_orange
            if self.color == 'orange':
                self.color = f + orange
            if self.color == 'light orange':
                self.color = f + light_orange
            if self.color == 'yellow':
                self.color = f + yellow
            if self.color == 'yellow green':
                self.color = f + yellow_green
            if self.color == 'green':
                self.color = f + green
            if self.color == 'blue':
                self.color = f + blue
            if self.color == 'light blue':
                self.color = f + light_blue
            if self.color == 'blue green':
                self.color = f + blue_green
            if self.color == 'violet':
                self.color = f + violet
            if self.color == 'purple':
                self.color = f + purple
            if self.color == 'light pink':
                self.color = f + light_pink
            if self.color == 'pink':
                self.color = f + pink
            if self.color == 'hot pink':
                self.color = f + hot_pink

            # Gray scale
            if self.color == 'white':
                self.color = f + white
            if self.color == 'gray 10':
                self.color = f + gray_10
            if self.color == 'gray 20':
                self.color = f + gray_20
            if self.color == 'gray 30':
                self.color = f + gray_30
            if self.color == 'gray 40':
                self.color = f + gray_40
            if self.color == 'gray 50':
                self.color = f + gray_50
            if self.color == 'gray 60':
                self.color = f + gray_60
            if self.color == 'gray 70':
                self.color = f + gray_70
            if self.color == 'gray 80':
                self.color = f + gray_80
            if self.color == 'gray 90':
                self.color = f + gray_90
            if self.color == 'black':
                self.color = f + black

    def write(self) -> str:
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
        [print(self.color + slide + '\033[0m', end='\r') for slide in animation_slides if time.sleep(self.flow) is None]
        
    def casewave(self, direction='right', cycles=1) -> str:
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
        
    def shuffle(self, cycles=10) -> str:
        '''
        Shuffles your strings.

        ---
        Accepts 1 argument.
        - cycles --/ accepts int as arg. The amount of times the animation occurs.
        ---
        Does not accept lists
        '''
        import random
        animation_slides = []
        for i in range(cycles):
            shufword = [letter for letter in self.word]
            random.shuffle(shufword)
            shufword = ''.join(shufword)
            animation_slides.append(shufword)
        [print(self.color + slide + '\033[0m', end='\r') for slide in animation_slides if time.sleep(self.flow) is None]
        
    def load(self, endofword='', cycles=1) -> str:
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
            [print(self.color + keepword + slide + '\033[0m', end='\r') for slide in animation_slides if time.sleep(self.flow) is None]

    def slide(self, direction='left', cycles=1) -> str:
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
        if self.word[-1] != ' ':
            self.word += ' '

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
            [print(self.color + slide + '\033[0m', end='\r') for slide in animation_slides if time.sleep(self.flow) is None]

    def stamp(self, colorend=True) -> str:
        '''
        Put at the end of the animation sequence to paste your string in place.
        
        ---
        Takes 1 argument.
        - colorend --/ If set to false the terminal will retain color of the animation. Good for animated text input. \n
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

    def bulk(self) -> list:

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

    def halfbulk(self) -> list:
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

    def genuine(self) -> list:

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

    def bigfoot(self) -> list:
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

'''
TODO
def palettes(name):

    rainbow = ['red', 'red orange', 'orange', 'light orange', 'yellow', 'yellow green', 'green', 'blue green', 'light blue', 'blue', 'violet', 'purple', 'light pink', 'pink', 'hot pink']

    gray_scale = ['white','gray 10','gray 20','gray 30', 'gray 40','gray 50', 'gray 60','gray 70','gray 80','gray 90', 'black']
    
    rgb = ['red', 'green', 'blue']

    fire = ['red', 'red orange', 'orange', 'light orange', 'yellow']

    neon = ['hot pink', 'blue green', 'yellow green', 'green']

    if name == 'rainbow':
        return rainbow
    if name == 'gray scale':
        return gray_scale
    if name == 'rgb':
        return rgb
    if name == 'fire':
        return fire
    if name == 'neon':
        return neon
'''
