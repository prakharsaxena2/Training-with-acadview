'''Q1'''
import re

'''Importing re module for regex'''
emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""
print(re.findall(r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})', emails, flags=re.IGNORECASE))
'''Extracting the details'''

'''Q2'''
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
print(re.findall(r'\bB\w+', text, flags=re.IGNORECASE))
'''Printing word starting with letter 'b' '''

'''Q3'''
sentence = "A, very very; irregular_sentence"
output = " ".join(re.split('[;,\s_]+', sentence))
'''Converting into regular sentence'''
print(output)
'''Printing Sentence'''

'''Q4'''
import re

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
tweet = re.sub('(http\S+\s*)|(RT|cc)|(#\S+)|(@\S+)', ' ', tweet)
'''Removing URLs,  RTs/CCs, hashtags, tags(@) etc. '''
tweet = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), '', tweet)
'''Removing punctuations '''
tweet = re.sub('\s+', ' ', tweet)
'''Removing extra whitespaces'''
print(tweet)
