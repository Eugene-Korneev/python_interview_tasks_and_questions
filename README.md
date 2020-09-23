# Python interview tasks and questions

### Requirements:
- python 3.6 or newer

### Tasks:
1. Function to receive n fibonacci number or list of numbers 
(with given start number, stop number and step)
- **Answer**: [001_fibonacci.py](001_fibonacci.py)

2. Decorator that sets the number of positional arguments for given function
- **Answer for python < 3.8**: [002_args_num_decorator](002_args_num_decorator.py)
- **Answer for python >= 3.8**: Use '/' in function parameters. 
    Example for the function with 2 positional only arguments: 
    ```
    def foo(a, b, /, c, d):
        pass
    ```

3. Find and print substring with three most frequent words from the string 
"abba com mother bill mother com abba dog abba mother com". 
Words order in the substring doesn't matter.
- **Answer**: [003_three_most_frequent_words.py](003_three_most_frequent_words.py)
