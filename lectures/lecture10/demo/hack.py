import ast

class Hack(ast.NodeTransformer):
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            node.op = ast.Sub()
        return node

a = ast.parse('def f(a,b): return a+b', mode='exec')
print(ast.dump(a))
a = Hack().visit(a)
print(ast.dump(a))
f = compile(a, '<string>', 'exec')
exec(f)
print(f(4,2))
