# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:27:36 2015

@author: Shuang

collection random stuff from overstack
"""
#loop over things after groupby
import numpy as np
import pandas as pd
rand = np.random.RandomState(1)
df = pd.DataFrame({'A': ['foo', 'bar'] * 3,
                   'B': rand.randn(6),
                   'C': rand.randint(0, 20, 6)})
gb = df.groupby(['A'])
#I can iterate through it to get the keys and groups:
for k, gp in gb:
 print 'key=' + str(k)
 print gp
 
 gb.get_group('foo')
 
 
 
#get rid of rows where id is not numeric
import numpy as np
df= pd.DataFrame({'id' : [1,2,3,'tt',4,5,'de'],
                    'name' : ['A','B','C','D','E','F','G']})
df = df[df['id'].apply(lambda x: type(x) in [int, np.int64, float, np.float64])]
# or
new_df = df[df['id'].apply(lambda x: type(x) in [int, np.int64, float, np.float64])]

#summing over values based on group
df = pd.DataFrame([['A', 'B', 'C', 'A', 'C', 'B'], [1, 6, 4, 3, 1, 2]], index=['Type1', 'Value']).T
df2 = df.groupby('Type1').sum()

#
df= pd.DataFrame({'a' : [1,2,3,4],
                    'b' : [np.nan,5,np.nan,6,]})
df['c'] = df['b'].combine_first(df['a']) #b's value is prioritized use a to fill holes
df['c'] = df['a'].where(df['b'].isnull(), df['b'])


#Unicode section in NLP with Python
import nltk
path=nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
import codecs
f = codecs.open(path,encoding='latin2')

