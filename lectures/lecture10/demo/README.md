function decorators and closures

- arith.py

- add print function that prints out the name
  - see slide 31 from beazley
  - refactor repeated code

- basic decorator s34
  - func = debug(func)
  - @ shorthand
    - closures
    - arg passing
    - staging
      - generate closure when defining the function 
        since the decorater is called on the function definition
      - the closure is executed at runtime
    - introspection: func.__qualname__

  - decoraters with arguments - add prefix
  @debug(arg) -> debug(arg)(func) - one more stage!
      function that returns a function that decorates the func

  - @wraps preserving metadata
    - f.__wrapped__

class decoraters

- klass.py, klass2.py

@classmethod
@staticmethod

metaclasses

- metaklass.py
- metaklass2.py
- metaklass3.py

Other examples

