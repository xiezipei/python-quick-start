# str = 'hello'
# print(str)


def p (str): 
    print(str)

s = 'abcdef'
p(s) # abcdef
p(s.startswith('a')) # True
p(s.endswith('f')) # True
p(s.find('c')) # 2
p(s.find('C')) # -1
p(s.replace('def', 'xyz')) # abcxyz
p('a,b,c,d,e,f'.split(',')) # ['a', 'b', 'c', 'd', 'e', 'f']
p(s.upper()) # ABCDEF
p(s.lower()) # abcdef
p('   abc   def   '.strip()) # abc   def