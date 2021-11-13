# EC601 Project3
Here is EC601 project 3, which contains the unit test, performance test and pylint test of project2. 

I want to first express my gratitude  to the two Teaching Assistants Feng Wang and Niantong Dong, their guidance and suggestion is very significant and really helpful!

My project2-Sentiment Analysis was written in Jupyter Notebook, so it is quite different to run unit test for .ipynb files, therefore I also post a guidance as following.

## 1. Unit test for .ipynb

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

## 2. Performance test

For performance test, I use `line_profiler`module to finish the work. 

* First, `pip install line_profiler` to your environment.
* Second, add `@profile` in your code before the first function. Please see `performance_test_code.py` line 36.
* Third, run `kernprof -l -v performance_test_code.py` in terminal, then you will see the result, and the result will be saved into `performance_test_code.py.lprof`

## 3. Pylint test

Also, I used the pylint function package mentioned in the slide to score the code, and constantly modify the naming style (such as snake naming, camel case naming), modify indentation, and delete redundant conditional judgment statements.

## 4. Result and report
### Unit test
#### All condition are correct
![image](https://user-images.githubusercontent.com/90535023/141605836-c8fbedfe-d41c-44f4-ba85-1456b4e90020.png)
#### Assert the wrong condition by design
![image](https://user-images.githubusercontent.com/90535023/141605830-b1de38d2-8cf9-4632-a2b1-c505d8f2bc3b.png)
### Performance test
#### We can see the percentage of time for each line
![image](https://user-images.githubusercontent.com/90535023/141605891-a44ef909-82d4-4f70-a9b6-0b1d8d998ca5.png)
### Pylint test
Please see `pylint_test_result.txt` for details.

