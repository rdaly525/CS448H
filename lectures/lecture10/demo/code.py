import ast, dis

a = ast.parse('a+b', mode='eval')
print(ast.dump(a))
c = compile(a, '<stdin>', 'eval') 
dis.dis(c)
