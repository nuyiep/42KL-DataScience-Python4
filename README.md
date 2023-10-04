# 42KL-DataScience-Python4
Data Oriented Design

## **ex00**

`args` 

- Non-keyword arguments
- receives arguments as a __tuple__

`kwargs`

- Keyword arguments
- receives arguments as a __dictionary__

`//`

- Integer division to ensure an integer result

## **ex01**

`closure`

```text
def outer_function(x):
    # This is the outer function
    def inner_function(y):
        # This is the inner function
        return x + y  # inner_function can access 'x' from the outer scope
    
    return inner_function  # Return the inner function

closure_instance = outer_function(10)  # Create a closure instance
result = closure_instance(5)  # Call the closure
print(result)  # Output: 15
```

```nonlocal``` similar to static variable

## **ex02**

`wrappers/decorator`

- modify the behavior of another function/class/object
- e.g. @my_decorator
- Common pattern for decorators:
	* nested function

```text
def tictoc(func):
	def wrapper():
		t1 = time.time()
		function

```