from testbook import testbook

@testbook('/home/ece/Downloads/Untitled3 (3).ipynb',execute=True)

# test for tweets number
def test_print(tb):
    print_tweets = tb.ref("print_tweets")
    # normal use cases
    assert print_tweets(10)==10
    assert print_tweets(100)==10
    # misuse case
    #assert print_tweets(-1)==0

@testbook('/home/ece/Downloads/Untitled3 (3).ipynb',execute=True)


# test for cleaning method
def test_clean(tb):
    cleanTxt = tb.ref("cleanTxt")
    # normal use cases
    assert cleanTxt('abc')=="abc"
    assert cleanTxt('@abc')==""
    assert cleanTxt('Lol#funny')=="Lolfunny"

# test for subjectivity score
@testbook('/home/ece/Downloads/Untitled3 (3).ipynb',execute=True)
def test_subj(tb):
    getSubjectivity = tb.ref("getSubjectivity")
    # normal use cases
    assert getSubjectivity('I love ECE')>0
    assert getSubjectivity('123456')==0
    # error handling
    #assert getSubjectivity(123456)==0

 #test for polarity score
@testbook('/home/ece/Downloads/Untitled3 (3).ipynb',execute=True)
def test_pola(tb):
    getPolarity = tb.ref("getPolarity")
    # normal use cases
    assert getPolarity('I am so sad')<0
    assert getPolarity('I am so happy')>0
  