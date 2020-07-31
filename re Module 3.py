def line_break(x):
    print(str(x) + '---------' + str(x) + '---------' +
          str(x) + '---------' + str(x) + '---------')


lb = line_break

'''
~appendix
* this is the fourth of the four note txts on python regex *
~lb(0) : extending the use of group without the | in the parentheses
~lb(1) : capturing information from our groups
~lb(2) : back reference for the captured groups
~lb(3) : .findall() instead of .finditer() method
~lb(4) : .match() instead of .finditer()
~lb(5) : .search() instead of .match()
~lb(6) : flags for using regex in python

'''
import re

lb(0)
# the last concept that will be explored in this series of notes on regex will be on how to capture information from groups.
# you have already learned how to match groups but you can actually use the info. captured from those groups.

# to illustrate, here is an example consisting of URLs:
urls = '''
https://www.google.com
http://jychoi.com
https://youtube.com
https://www.nasa.gov
'''

# some URLs here are https whereas other is http, and some have www. while others don't; they are pretty they're pretty inconsistent

# let's say that for each of these URLs you only wanted to grab the domain name followed by the top level domain,
# e.g. 'google.com' in 'https://www.google.com', and ignore everything else.
pattern = re.compile(r'https?://(www\.)?[a-zA-Z]+\.[a-z]+')
# the www. was wrapped into a group (otherwise it would have been '(w{3}\.)?')and made optional by (?)

matches = pattern.finditer(urls)

for match in matches:
    print(match.group())
'''returns:
https://www.google.com
http://jychoi.com
https://youtube.com
https://www.nasa.gov
'''

lb(1)
# as you can see, the regular expression pattern worked to match with the URLs in urls.
# but remember, the point was to use your groups to capture some information regarding the URLs.

# so, let's capture the domain name and the top level domains (i.e. 'google.com')
# to capture these sections, you can just put them in a group by surrounding them in parentheses.
# noting that the section of the pattern of your interest is after the second question mark (?) from the above written pattern:
pattern = re.compile(r'https?://(www\.)?([a-zA-Z]+)(\.[a-z]+)')
# returns all four URLS, i.e. nothing changed from what was returned in lb(0) since you're just wrapping the same expression in ()
# as you can see: the domain name part: ([a-zA-Z]+) and the high-level domain part: (\.[a-z]+) were put into two sets of parentheses

# notice that, now, you have a regex pattern that is divided into three different groups:
# 1) www. [expressed as (www\.)]; 2) domain name [expresssed as (a-zA-Z]+)]; and 3) top-level domain [expsd. as (\.[a-z]+)]

# there's also a group 0, which is everything that you captured. i.e. entire URL in this case.

# i.e. you can pass in the group index within the .group() method!

# e.g. capturing group(1) i.e. the optional www: '(www\.)?'
matches = pattern.finditer(urls)

for match in matches:
    print(match.group(1))
'''returns:
www.
None
None
www.
'''

# e.g.2 capturing the group(2) i.e. domain name: '([a-zA-Z]+)'
matches = pattern.finditer(urls)

for match in matches:
    print(match.group(2))
'''returns:
google
jychoi
youtube
nasa
'''

lb(2)
# now, you can use what's called a back reference to reference your captured group
# it's basically a shorthand for accessing these group indexes.

# the regular expression module (re) has .sub() method you can use to perform a substitution.
# to illustrate what this looks like:
pattern = re.compile(r'https?://(www\.)?([a-zA-Z]+)(\.[a-z]+)')

# you can pass in as first argument the group index with backslash (\) + index of group (e.g. 2 and 3),
# and pass in as second argument the text you want to replace

subbed_urls = pattern.sub(r'\2\3', urls)
# i.e. for subbed_urls, you're using the pattern to substitute out group 2 and group 3 for all of your matches in urls.
# which means that everytime it finds a match, it'll replace that match with group 2 and group 3

print(subbed_urls)
'''returns:
google.com
jychoi.com
youtube.com
nasa.gov
'''

# n.b. if you had a large document you wanted to reformat like this,
# then learning how to do this with regular expressions can save you a tonne of time and allow you to do that in a couple of mins.


lb(3)
# so far, you have used the .finditer() method-
#-because it generally does the best job of showing all the matches and the location of the matches,
# but there are other methods that can be used for other purposes.

# one such method is the .findall() method.

# whereas with .finditer() method, it returned the matched objects with extra info. and functionalities,
# the .findall() method will just return the matches as a list of strings.

# n.b. if there are (n *) groups within the regex pattern, it'll only return (n *) groups (see a); b)).

# a) regex has one group within:
pattern_1 = re.compile(r'https?://(www\.)?[a-zA-Z]+\.[a-z]+')
matches_1 = pattern_1.findall(urls)  # note the .findall() used here

for match in matches_1:
    print(match)
'''returns:
www.


www.
'''

# b) regex has three groups within:
pattern_3 = re.compile(r'https?://(www\.)?([a-zA-Z]+)(\.[a-z]+)')
'''returns:
('www.', 'google', '.com')
('', 'jychoi', '.com')
('', 'youtube', '.com')
('www.', 'nasa', '.gov')
'''

# since there are multiple groups in this pattern, .findall() returned a list of tuples and the tuples contain all of the groups
# n.b. if there are no groups within the regex pattern, it'll just return all of the matches in a list of strings.

lb(4)
#.match() method is another alternative to the .finditter() method.
#.match() will determine if the regular expression matches at the beginning of the string.

# to illustrate, here's a sentence:
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'Start')
matches = pattern.match(sentence)

#(instead of looping through the results like with .finditer() and .findall(),)
#(you can just print out matches).
print(matches)
# returns: <re.Match object; span=(0, 5), match='Start'>

# given .match() only prints true if the regex matches at the beginning of the string,
# if you write a regex of a text that does appear but just not at the beginning (e.g. 'bring')
pattern = re.compile(r'bring')
matches = pattern.match(sentence)

print(matches)
#returns: None

lb(5)
# if you want to match with the entire string, you can conversely just use the .search() method,
# which only prints out the first match that it finds.
pattern = re.compile(r'Start a sentence')
matches = pattern.search(sentence)

print(matches)
# returns: <re.Match object; span=(0, 16), match='Start a sentence'>

# n.b. if you search for something that doesn't match, it'll just return None aswell.

lb(6)
# flags can be used to make your life easier when using regular expressions in python.

# e.g. you want to match with a given word-
#-and match with it regardless of whether it was in lowercase or uppercase or mixture of both

# from this string:
report = 'The police located the captive through top of the line surveillance technology'

# you wanted to match with the word 'located' but each letter could be uppercase/lowercase-
#-normally to create a pattern like this, you'd have to use a character set like:
re.compile(r'[lL][oO][cC][aA][tT][eE][dD]')
# which can be a pain and prone to mistakes.

# but you can just type in 'Located' (note the capital L written on purpose for demonstration):
re.compile(r'Located')

# and pass in a second argument which would be the IGNORECASE flag:
pattern = re.compile(r'Located', re.IGNORECASE)

matches = pattern.search(report)
print(matches)
# returns: <re.Match object; span=(11, 18), match='located'>

# as you can see, 'Location', altough it appears with the lowercase (l) in report, still matches due to the IGNORECASE flag.
# n.b. shorthands also exist for these flags, and in this particular case,
# re.IGNORECASE can be written re.I in shorthand:
re.compile(r'located', re.I)

# n.b. there are several other flags available for regular expressions in python (such as re.MULTILINE (re.M), re.VERBOSE (re.X))
# and they can be found here in the official python documentation: (https://docs.python.org/3/library/re.html#re.I)
