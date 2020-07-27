from scripts.content_cleaner import rem_dup_period, add_period, other_styles, grammar_tool, case_of_eqn, capitalize_first_char, eqn_styles

def test_add_period():
	assert add_period(list("I am a period adder"), 0) == (list("I am a period adder."), 1)
def test_rem_dup_period():
	assert rem_dup_period(list("I am a duplicate period remover..."), 0) == (list("I am a duplicate period remover."), 2)
def test_grammar_tool():
	assert grammar_tool("I am a gramar checker.", 0) == ("I am a grammar checker.", 1)
def test_case_of_eqn():
	assert case_of_eqn(list("i am not an equation"), 0) == (list("I am not an equation"), 1)
	assert case_of_eqn(list("a/4 = 2. Therefore, a = 8 and i am an equation."), 0) == (list("a/4 = 2. Therefore, a = 8 and i am an equation."), 0)
def test_capitalize_first_char():
	assert capitalize_first_char(list("i capitalize the first character."), 0) == (list("I capitalize the first character."), 1)
def test_other_styles():
	assert other_styles(list("""Lets check this example :
Value: thoughts,ideologies and deeds of mind
Victory :winning a goal .
Job:a task to be completed."""), 0) == (list("""Lets check this example :
Value : thoughts, ideologies and deeds of mind.
Victory : winning a goal.
Job : a task to be completed."""), 7)
def test_eqn_styles():
	assert eqn_styles(list("""So, our equation is as follows.
(2x-1)*5=50
2x-1=50/5
2x= 10 +1
2x =11
now we are just left with normal division.
x=11/2
x = 5.5
hence, our answer is 5.5."""), 0) == (list("""So, our equation is as follows.
(2x - 1) * 5 = 50
2x - 1 = 50 / 5
2x = 10 + 1
2x = 11
Now we are just left with normal division.
x = 11 / 2
x = 5.5
Hence, our answer is 5.5."""), 21)
