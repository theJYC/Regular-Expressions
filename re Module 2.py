def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''
~appendix
* this is the third of the four note txts on python regex *
~lb(0)  : quantifiers
~lb(1) : quantifiers in practice 0
~lb(2) : quantifiers in practice 1
~lb(3) : quantifiers in practice 2
~lb(4) : groups-to-the-rescue
~lb(5) : **quick recap exercise** (writing your own regular expression from scratch)
~lb(6) : reading someone else's regular expression from the internet

'''
import re

lb(0)
'''
quantfrs|___matches______________________________
        |
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum

'''

# everything that you have looked at so far have involved searching for a pattern one. character. at. a. time.
# e.g. to match with a phone number, you had to construct a regex, digit-by-digit, as:

# a)
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')

# it's easy to make mistakes when you have a lot of characters to type out.
# but you can use quantifiers to match multiple characters at a time.

# in this case, instead of typing out \d three times for the first three digits,
# you can just type \d once, and quantify it with a {3}.
# and the rest applies...:

# b)
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')


# a) and b) are the same code, but the latter is much less prone to mistakes along the way.

lb(1)
# in lb(9) you were matching exact numbers.
# sometimes you don't know the exact numbers, and you'll need to use other quantifiers.

# e.g. here's a text consisting of names:
names = '''
Mr. Choi
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

# and some lines starts with a Mr. , others with Ms / Mrs./ etc.
# let's say you wanted to write a pattern that would match these prefixes and the entire name that comes afterwards.

# to start off, work with the names that start with 'Mr'.
# you can see that some of these have a '.' after the 'Mr' ('Mr.'), and some do not ('Mr').

# to write this pattern, you need to specify that the period after the prefix is optional.
# you'll need to use the '?' quantifier to do this.
# n.b. as with {3} in lb(9), quantifiers are placed after the digit of interest.

# reminder that a period inside the pattern needs to be written with an escape
pattern = re.compile(r'Mr\.?')

matches = pattern.finditer(names)

for match in matches:
    print(match.group())
'''returns:
Mr.
Mr
Mr
Mr.
'''

lb(2)
# the next logical step would be to write the remainder of the pattern.
# a common occurence between these names is the (prefix).?(space)[Uppercase letter], which format will be written as:
pattern = re.compile(r'Mr.?\s[A-Z]')

matches = pattern.finditer(names)

for match in matches:
    print(match.group())
'''returns:
Mr. C
Mr S
Mr. T
'''

# at this point, you have a decision to make:
# you have completely matched Mr. T (as in the names string of line 336, Mr. T doesn't have any more info. to his name)
# but you still need to match the rest of the other names (Mr. C and Mr S, who are actually Mr. Choi and Mr Smith)

# so you could say that you'd match any word character after that first uppercase letter, after the prefix, [A-Z].
# which would be done by placing a \w.
lb(3)
# then, specify the quantifier that should be used with the \w.

# a) you can either use the (+) quantifier:
pattern = re.compile(r'Mr.?\s[A-Z]\w+')

matches = pattern.finditer(names)

for match in matches:
    print(match.group())
'''returns:
Mr. Choi
Mr Smith
'''

# b) or you can use the (*) quantifier,
# which would also take Mr. T into account, unlike the limited a) approach:
pattern = re.compile(r'Mr.?\s[A-Z]\w*')

matches = pattern.finditer(names)

for match in matches:
    print(match.group())
'''returns:
Mr. Choi
Mr Smith
Mr. T
'''

lb(4)
'''
_groups_|___matches______________________________
        |
|       - Either Or
( )     - Group

'''

# now that you have figured out how to write the pattern for the Mr(.) names,
# tackle how you would write the pattern for Ms/Mrs too.
# groups would be a good go-to.

# here is how groups could be written into the pattern to incorporate Mrs/Ms prefix into all names.
#using the '|', called the pipe character, (r|s|rs) written below matches with Mr/Ms/Mrs *:
pattern = re.compile(r'M(r|s|rs).?\s[A-Z]\w*')

matches = pattern.finditer(names)

for match in matches:
    print(match.group())
'''returns:
Mr. Choi
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

# *if you want to improve readability, you could also group Mr/Ms/Mrs as (Mr|Ms|Mrs):
pattern = re.compile(r'(Mr|Ms|Mrs).?\s[A-Z]\w*')

matches = pattern.finditer(names)

for match in matches:
    print(match.group())
'''returns:
Mr. Choi
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

lb(5)
# now for a quick recap of all that has been learned so far:
# e.g. here is a sample emails variable
emails = '''
JinYoungChoi@gmail.com
JinYoung.Choi@univ.edu
JinYoung-067-Choi@work.net
'''

# to try and match all three of these seemingly different emails,
# start by breaking down the email into [name][@][.][gmail/univ/work][.][com/edu/net]
# and looking at writing the pattern for the first email:
re.compile(r'[a-zA-Z]+@[a-zA-z]+\.com')

# matches with: JinYoungChoi@gmail.com

# as you can see the other two emails were not matched.
# e.g. the second email was not matched because the regular expression didn't account for:
# a) the period between firstname and lastname, and
# b) the .edu instead of the .com

# edit the regular expression to match the second email, granted the two [a), b)] observations:

re.compile(r'[a-zA-Z.]+@[a-zA-z]+\.(com|edu)+')

# matches with: JinYoungChoi@gmail.com and JinYoung.Choi@univ.edu

# lastly, to match the third email, it looks like you need to account for:
# a) the dash (-) in the part before @
# b) the numbers (067) in the part before @
# c) the dash in the domaim (i.e. part after @ and before \).
# d) the (net) at the end of the email

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-z-]+\.(com|edu|net)+')

matches = pattern.finditer(emails)

for match in matches:
    print(match.group())
'''returns:
JinYoungChoi@gmail.com
JinYoung.Choi@univ.edu
JinYoung-067-Choi@work.net
'''

lb(6)
# n.b. for something like email addresses, it can be tough writing your own regular expressions from scratch,
# but fortunately there's a lot of these available online. And once you're able to write regular expressions,
# you should be able to read them and figure out what they'll match.

# generally it is much harder to read someone else's regular expression though.
# e.g. a regular expression that can be found online for email addresses:
re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

# looks a little intimidating but all they are is just some large character sets.

# 1) first we have a character set that matches all lowercase and uppercase letters / digits / _ / . / + / -
re.compile(r'[a-zA-Z0-9_.+-]')

# 2) then there is a plus sign (+), that will match one or more of any of those characters in the character set
re.compile(r'[a-zA-Z0-9_.+-]+')

# 3) and it matches those all the way until it reaches the @ symbol.
re.compile(r'[a-zA-Z0-9_.+-]+@')

# 4) after the @ symbol, for the domain,
# we have another character set that matches all lowercase and uppercase letters / digits / -
re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]')

# 5) then another plus sign (+), for the same purpose of matching with one or more of the above character set
re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+')

# 6) then an escape key (\) and the period (.), meaning a (.) will follow in format:
re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.')

# 7) then another character set that matches all lowercase and uppercase letters / digits / - / .
re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]')

# 8) until finally the plus sign (+) to match one or more of any of those characters in the character set (net/com/edu/etc.)
re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')


# # # # # # # # # # # # # # # # continue onto re Module 3 # # # # # # # # # # # # # # # #
