import Cnf as cnf

# Arquivo para testes:

formulas = [
    '(((p>q)>p)>p)', 
    '((p#q)>-(q#r))', 
    '(-(p&q))',
    '((p&s)#(q&r))',
    '(p#(q&r))',
    '((q&r)#p)',
    '((p&(q>r))>s)',
    '-(b # c)',
    '(a&(b#(d&e)))',
    '(a & b)'
]

c = 1
for i in formulas:
    print(f'{c}. Fomula.......:')
    print(f'Old formula......: {i}')
    print(f'New formula (cnf): {cnf.to_cnf(i)}\n\n')
    c += 1
