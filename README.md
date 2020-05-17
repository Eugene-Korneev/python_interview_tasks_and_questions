# Python interview tasks and questions

### Requirements:
- python 3.6 or newer

### Tasks:
1. Function to receive n fibonacci number or list of numbers 
(with given start number, stop number and step)
- **Answer**: [fibonacci.py](./fibonacci.py)
2. Decorator that sets the number of positional arguments for given function
- **Answer for python < 3.8**: [args_num_decorator.py](./args_num_decorator.py)
- **Answer for python >= 3.8**: Use '/' in function parameters. 
    Example for the function with 2 positional only arguments: 
    ```
    def foo(a, b, /, c, d):
        pass
    ```
