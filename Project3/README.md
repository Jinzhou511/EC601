# EC601Project3
Here is EC601 project 3, which contains the unit test, performance test and pylint test of project2. 

My project2-Sentiment Analysis was written in Jupyter Notebook, so it is quite different to run unit test for .ipynb files, therfore I also post a guidance as following.

## How to do unit test for .ipynb

I explored 3 ways to do so, which are `doctest`,`unittest`,`testbook`. In the end, I decided on using testbook and pytest to finish unit testing. Official website of testbook: `https://testbook.readthedocs.io/en/latest/`

* First, you need `pip install testbook` into your environment, I am using Ubuntu in Virtual Machine.
* Second, download the code from jupyter notebook in .ipynb format, and remember the path of this file, we will use the path later. 
Please see `code_for_unittest.ipynb`

* Third, write your test code in .py, such as 'test.py':
`from testbook import testbook`

`@testbook('/path/to/notebook.ipynb', execute=True)`(replace the path)

`def test_foo(tb):`

    foo = tb.ref("foo")

    assert foo(2) == 3

Please see `unit_test.py`
* Forth, run `pytest test.py` in terminal, then you can see result.

## Performance test

For performance test, I use `line_profiler`module to finish the work. 

* First, `pip install line_profiler` to your environment.
* Second, add `@profile` in your code before the first function. Please see `performance_test_code.py` line 36.
* Third, run `kernprof -l -v performance_test_code.py` in terminal, then you will see the result, and the result will be saved into `performance_test_code.py.lprof`

## Pylint test

Also, I used the pylint function package mentioned in the slide to score the code, and constantly modify the naming style (such as snake naming, camel case naming), modify indentation, and delete redundant conditional judgment statements.

## Result and report
### Unit test

