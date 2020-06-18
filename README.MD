While learning Rust, [Canop](https://github.com/canop) showed me the program he did for his kids in Rust, 
that one, [Kidding](https://github.com/Canop/kidding).

As a quite simple program, I've decided to translate it into Python, to understand better Rust and delve further into Python. There are a few things I need to update some of the program subtleties only exist in Rust, and needs  further adaptation in Python. Also some part are not enough pythonic yet and will be upgraded.

It is asking questions like `35 + 12 = ?` in a loop.

The code is easy to tune and change with kid, it's a basis for a coding play too.

![screenshot](Screenshot_py.png)

##### upgrade for que_ans

  * future upgrade

- use in the new method, the enum instead of using if

###### done

- use the lines below for change when `randval == 3`

```python
~numbers = [randrange(1, 17) for _ in range(randrange(2,6))]~
~question = 'The question is: ' + ' + '.join(map(str, numbers))~
~answer = sum(numbers)~
```

##### upgrade for question

  * future upgrade

  - Use a dictionnary for the switch board, if possible


