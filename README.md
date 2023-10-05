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

```python
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

## **ex03**

`@dataclass decorator`

- simplifies the creation of a class for storing data
- automatically handling initialization, string representation, and equality comparison
- \_\_init__(), \_\_repr__(), \_\_eq__()

`field() function`

- specify additional metadata and default values for fields when creating a data class

`_post_init_()`

- perform additional operations or customization after the object has been initialized
- call automatically immediately after the \_\_init__()

`default factory (field)`

- specify a factory function that generates default values for a field in a data class

`init (field)`

- used to control whether a field should be included in the automatically generated \_\_init__() method
