def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''
~appendix
* this is the first of the four note txts on python regex *
~lb(0): basic introduction to regex
~lb(1): metacharacters and regex
~lb(2): metacharacters within pattern search regex
~lb(3): list of metacharacters
~lb(4): using anchors  (\b and \B)
~lb(5): using anchors extnded. (carets ^ and dollarsign $)
~lb(6): when to use metacharacters instead of literal characters (pattern search vs literal search)

'''
lb(0)
# you can create a regular expression for text in basically any pattern you can think of.
# first, import the regex module
import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

jychoi.com
'''

# run the re.compile() method to write a text pattern to look up
# this method will allow you to separate out the patterns into a variable, and make it easier to reuse that variable to perform multiple searches.
pattern = re.compile(r'abc')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# returns: <re.Match object; span=(1, 4), match='abc'>

# the 'span' range shows the beginning and end index of the match.
# span can be useful because these indexes show the position of the match, meaning you can find the match using string slicing:
print(text_to_search[1:4])
#returns: abc

lb(1)
# notice that when abc was searched, it didn't pick up 'ABC' which is on the next line down from the 'abc' match.
# this is because regex is case sensitive. it is also order-sensitive (i.e. you can't search for 'cba' for 'abc')

# MetaCharacters(Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )

# n.b. when you search for any of the above special characters, take caution since they mean different things in regex.
# escape--[use backslash (\) before]-- the character to search for em.

pattern = re.compile(r'\.')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
'''returns:
<re.Match object; span=(112, 113), match='.'>
<re.Match object; span=(147, 148), match='.'>
<re.Match object; span=(168, 169), match='.'>
<re.Match object; span=(172, 173), match='.'>
<re.Match object; span=(219, 220), match='.'>
<re.Match object; span=(250, 251), match='.'>
<re.Match object; span=(263, 264), match='.'>
'''

lb(2)
# when special characters are a part of the text-pattern, insert the escape (i.e. backslash \) within the regex

# e.g. searching for 'jychoi.com' in the text
pattern = re.compile(r'jychoi\.com')  # note the \.com instead of .com

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# returns: <re.Match object; span=(140, 150), match='jychoi.com'>

lb(3)
# literal search is not as exciting as pattern searching!
# to search patterns, you need to use the metacharacters.
# below is a table of metamatches and what they match with
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

'''

# n.b. the capital letters basically negate their small letter counterparts.
# e.g:
# \w matches with any word character, whereas
# \W mathces with anything that is NOT a word character.

lb(4)
# anchors are a little different to metacharacters:
'''

anchors_|___matches______________________________
        |
\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

'''

# anchors don't actually match any character, but rather,
# invisible positions before or after characters.
# you can use these in conjunction with other patterns you're searching for

# e.g. referring to 'Ha HaHa' on line 27

# the \b anchor looks for a word boundary,
pattern = re.compile(r'\bHa')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
'''returns:
<re.Match object; span=(67, 69), match='Ha'>  <--word boundary (beginning of a new line) here for the first Ha of '[Ha] HaHa'
<re.Match object; span=(70, 72), match='Ha'>  <--word boundary (space between the fist Ha and Haha) for the second Ha of 'Ha [Ha]Ha'
'''

# n.b. r'\bHa' is not matching the third Ha, since there is no word boundary preceding it.
# which means that \B, which is the opposite of the \b anchor, will pick it up:
pattern = re.compile(r'\BHa')

matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# returns: <re.Match object; span=(72, 74), match='Ha'>

lb(5)
# moving on in the anchors list
# carets (^) will match the position that is the beginning of a string,
# and the $ will match the position that is the end of the string.

# e.g. here is a sample text
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'^Start')

matches = pattern.finditer(sentence)

for match in matches:
    print(match)
# returns: <re.Match object; span=(0, 5), match='Start'>
 # only returns a match because the pattern searched was strictly 'Start' that is at the beginning of a string
 #(stipulated by the caret (^)).

# you can use the $ similarly to the ^.

pattern = re.compile(r'end$')

matches = pattern.finditer(sentence)

for match in matches:
    print(match)
# returns: <re.Match object; span=(41, 44), match='end'>


# # # # # # # # # # # # # # # # continue onto re Module 1 # # # # # # # # # # # # # # # #
