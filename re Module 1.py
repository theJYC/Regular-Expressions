def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''
~appendix
* this is the second of the four note txts on python regex *
~lb(0)  : using metacharacters in practice.0
~lb(1)  : using metacharacters in practice.1
~lb(2)  : using character sets
~lb(3)  : look out! character set pitfall
~lb(4)  : character set overload
~lb(5)  : using character sets in practice
~lb(6)  : dash (-) in character sets
~lb(7)  : caret (^) in character sets
~lb(8)  : caret (in character set) used in practice

'''

lb(0)
# while earlier you learned how to do a _literal_ search with regex, now you'll learn how to _pattern_ search with regex,
# through the help of metacharacters visited earlier.

# just a gentle reminder of the metacharacters and anchors used before in re Module 0:
'''
meta____|___matches______________________________
        |
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

anchors_|___matches______________________________
        |
\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

'''
import re

# e.g. sample text to search through:
text_to_search = '''

321-555-4321
123.555.1234

Mr. Choi
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

# here, to search for any phone number (i.e. line 61 and 62)
# you can use follow the format below, n.b. '.' inserted to match to 'any character except new line':
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
'''returns:
<re.Match object; span=(2, 14), match='321-555-4321'>
<re.Match object; span=(15, 27), match='123.555.1234'>
'''


lb(1)
# referring to the data.txt file within this directory, which contains n number of contact infos in the following format:
example = '''
Dave Martin
615-555-7164
173 Main St., Springfield RI 55924
davemartin@bogusemail.com
'''

# let's apply the phone number format to parse through this file to find only phone numbers.
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# reading the data via context manager
with open('data.txt', 'r') as f:
    contents = f.read()

    matches = pattern.finditer(contents)

# looping through list of matches (i.e. phonenumbers) within data.txt
for match in matches:
    # using .group() method just to cherry pick the matches in the return window
    print(match.group())
'''returns (first 5 lines):
615-555-7164
800-555-5669
560-555-5153
900-555-9340
714-555-7405
'''


lb(2)
'''
charctrs|___matches______________________________
        |
[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets

'''

# say you only wanted to match a phone number that only had a dash (-) or a dot (.) (and no other separator)

# e.g. you have a list of phonenumbers in different format
yellowpages = '''
042.8594.9242
032*1341*8425
010)1342)1442
010-4321-5930
'''

# previously, you used the '.' metacharacter within the r'\d\d\d.\d\d\d\d.\d\d\d\d',
# which basically matched with any text that follows the above format, with anything betwen the numbers as separators.

# if you want to e.g. only match with phonenumbers in yellowpages that are separated by the dot (.) or the asterisk (*),
# and hence not match with the third or fourth number that appear on yellowpages that are separated by other things,
# you can use something called a character set.

# a character set uses squarebrackets with the character(s) you want to match within the squarebrackets.
# adding as many characters as you want within the square brackets.

# in this case, only match with numbers that are separated by a dot (.) or an asterisk (*)
pattern = re.compile(r'\d\d\d[.*]\d\d\d\d[.*]\d\d\d\d')  # note the [.*]

matches = pattern.finditer(yellowpages)

for match in matches:
    print(match.group())
'''returns:
042.8594.9242
032*1341*8425
'''

# n.b. you did not have to escape the (.) when you wrote it within the character set.
# this is because character sets have a slightly different set of rules.
# i.e. you can write in the escape character (\) within the character set aswell, but not advised since it reduces readability.


lb(3)
# a common pitfall to avoid when using character sets is that within the character set [],
# you can put in as many values as you want, but they will only count as one value when regex searches for the pattern.

# i.e. you can have:
pattern = re.compile(r'\d\d\d[A-Za-z0-9-.]\d\d\d\d[.*]\d\d\d\d')

# whereby there's a lot of different characters within the first character set [A-Za-z0-9-.],
# but all of this will still only match one character.

# e.g.2. to illustrate, if you have this text:
doubledash = '010--3321--1352'

# and you want to customise a regex for this format,
# you CAN'T use:
# note the two dashes within the character set
pattern = re.compile(r'\d\d\d[--]\d\d\d\d[--]\d\d\d\d')

matches = pattern.finditer(doubledash)

for match in matches:
    print(match.group())
# returns nothing

# and instead you should use:
# note that now there are two character sets each
pattern_ = re.compile(r'\d\d\d[-][-]\d\d\d\d[-][-]\d\d\d\d')
matches = pattern_.finditer(doubledash)

for match in matches:
    print(match.group())
# returns: 010--3321--1352


lb(4)
# you can also apply character sets to a more tailored scenario:

ypgs = '''
010.8594.9242
900*1341*8425
010)1342)1442
800-4321-5930
'''

# say you only want to match with numbers under two conditions:
# a) number has to start with either 800 or 900
# b) number has to be separated by a dash (-)

# from the r'\d\d\d[.*]\d\d\d\d[.*]\d\d\d\d' of lb(2),
# 1) replace the first \d into a character set with 8 and 9 within (since 800 and 900 have 8 and 9 as first digit, respectively),
# 2) replace the second and third \d into 00 (since both 800 and 900 will have 00 as their second and third digit)
# 3) replace the separator character sets to [-] (to match the b) criterion):

pattern = re.compile(r'[89]00[-]\d\d\d\d[-]\d\d\d\d')  # note the [.*]

matches = pattern.finditer(ypgs)

for match in matches:
    print(match.group())
# returns: 800-4321-5930


lb(5)
# returning to the data.txt file,
# if you wanted to parse out only the 800- and 900- number from that file:

pattern = re.compile(r'[89]00[-]\d\d\d[-]\d\d\d\d')

with open('data.txt', 'r') as d:
    contents = d.read()

    matches = pattern.finditer(contents)

    for match in matches:
        print(match.group())
'''returns (first 5 lines):
800-555-5669
900-555-9340
800-555-6771
900-555-3205
800-555-6089
'''
# i.e. only the 800- and 900- numbers in the data.txt file were parsed.

lb(6)
# now, within a character set, a dash (-) is actually a special character aswell.
# when dash is put at the beginning or end, it will just match the literal dash character,
# but when placed between values, it can specify a range of values.

# e.g. you know that the \d (as in r'\d\d\d-\d\d\d-\d\d\d\d') matches any digit,
# but if you only wanted to match digits between 1 and 5,
# you can specify as so within the character set:

re.compile(r'[1-5]')

# similarly you can use the dash within the character set for letters aswell
# e.g. match between lowercase a to z:
re.compile(r'[a-z]')

# or match with either between lowercase a to z or uppercase a to z,
# by putting the two ranges back-to-back within the character set:
re.compile(r'[a-zA-Z]')

lb(7)
# another special character within the character set is the caret (^).
# typically, outside of the character set, the caret (^) is used to match the beginning of a string
# but within a character set, it negates the set and matches with everything that is NOT in the character set!

# e.g. if you put the caret in the above example (that matched with any lowercase or uppercase letter):
re.compile(r'[^a-zA-Z]')

# you will be returned a lot of matches that are NOT lowercase or uppercase letters (i.e. non alphabet characters, numbers, etc)


lb(8)
# say you have a scenario whereby you want to match with any three letter word that ends with -at,
# BUT you don't want to match the word 'bat'.

threeletterats = '''
cat
mat
pat
bat
'''

pattern = re.compile(r'[^b]at')  # note the caret (^)

matches = pattern.finditer(threeletterats)

for match in matches:
    print(match.group())
'''returns:
cat
mat
pat
'''

# # # # # # # # # # # # # # # # continue onto re Module 2 # # # # # # # # # # # # # # # #

