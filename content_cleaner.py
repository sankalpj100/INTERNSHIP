from quiz_app.models import Question, QuestionType, Tag, ReportFlag, User
import language_tool_python

# Main function.
def main(q_tags):
	cleaner_user = User.query.first()
	print(cleaner_user)
	content_check(cleaner_user, q_tags=[])

# To select questions using the tags.
def filter_questions(tags):

    questions = Question.query.filter()
    print("total", questions.count(), "questions")
    for tag in tags:
        questions = questions.filter(
            Question.tags.any(Tag.text == tag)
        )
    print("filtered", questions.count(), "questions")
    return questions

# Initiating the content check for the questions and explanations
def content_check(cleaner_user, q_tags=[]):
	tag_all_lang = q_tags + ["language"]
	tag_all_quant = q_tags + ["quantitative"]
	tag_all_logic = q_tags + ["logical"]
	tag_all_tech = 	q_tags	+ ["technical"]
	lang_questions = filter_questions(tag_all_lang)
	quant_questions = filter_questions(tag_all_quant)
	logic_questions = filter_questions(tag_all_logic)
	tech_questions = filter_questions(tag_all_tech)
	for question in lang_questions.all():

		language_type_check(question, cleaner_user)		
	for question in quant_questions.all():
		quant_type_check(question, cleaner_user)
	for question in logic_questions.all():
		logic_type_check(question, cleaner_user)
	for question in tech_questions.all():
		tech_type_check(question, cleaner_user)
	return

# Different types of the function for formatting and grammar corrections:

# Adds fullstop at the end of sentence, if absent.
def add_period(content_char_set, error_count):

	if (content_char_set[-1] != "?" and content_char_set[-1] != "."):
		content_char_set.append(".")
		error_count += 1
	return content_char_set, error_count

# Add fullstop in para change.
# Removes extra spaces before and after "," and "."
# Add spaces before and after ":"
def other_styles(content_char_set, error_count):
	# Add space after ":"
	for index in range(len(content_char_set)):
		if index == (len(content_char_set)-1):
			break
		if (content_char_set[index] == ":"):
			if (content_char_set[index+1] not in ["\n"," "]):
				content_char_set.insert(index + 1, " ")
				error_count += 1

	# Add space before ":"
	for index in range(len(content_char_set)):
		if index == (len(content_char_set)-1):
			break
		reverse_index = (index + 1) * (-1)
		if (content_char_set[reverse_index] == ":"):
			if (content_char_set[reverse_index - 1] != " "):
				content_char_set.insert(((index + 1) * (-1)), " ")
				error_count += 1

	# Add space after ","
	for index in range(len(content_char_set)):
		if index == (len(content_char_set)-1):
			break
		if (content_char_set[index] == ","):
			if (content_char_set[index+1] not in ["\n"," "]):
				content_char_set.insert(index + 1, " ")
				error_count += 1

	# Removes space before ","
	for index in range(len(content_char_set)):
		if index == (len(content_char_set)-1):
			break
		reverse_index = (index + 1) * (-1)
		if (content_char_set[reverse_index] == ","):
			if (content_char_set[reverse_index - 1] == " "):
				content_char_set.pop(reverse_index - 1)
				error_count += 1

	# Add space after "."
	for index in range(len(content_char_set)):
		if index == (len(content_char_set)-1):
			break
		if (content_char_set[index] == "."):
			if (content_char_set[index+1] not in ["\n"," "]):
				content_char_set.insert(index + 1, " ")
				error_count += 1

	# Add space before "."
	for index in range(len(content_char_set)):
		if index == (len(content_char_set)-1):
			break
		reverse_index = (index + 1) * (-1)
		if (content_char_set[reverse_index] == "."):
			if (content_char_set[reverse_index - 1] == " "):
				content_char_set.pop(reverse_index - 1)
				error_count += 1

	# Add period after para change
	for index in range(len(content_char_set)):
		if index == (len(content_char_set)-1):
			break
		reverse_index = (index + 1) * (-1)
		if (content_char_set[reverse_index] == "\n"):
			if(content_char_set[reverse_index - 1] != "\n" and content_char_set[reverse_index - 1] != "." and content_char_set[reverse_index - 1] != "," and content_char_set[reverse_index - 1] != ":"):
				content_char_set.insert(((index + 1) * (-1)), ".")
				error_count += 1
	return content_char_set, error_count

# Removes extra fullstops, if present.
def rem_dup_period(content_char_set, error_count):
	for index in range(len(content_char_set)):
		if index == (len(content_char_set)-1):
					return content_char_set, error_count
		if content_char_set[index]==".":
			while content_char_set[index+1] == ".":
				content_char_set.pop(index+1)
				error_count += 1
				if index == (len(content_char_set)-1):
					return content_char_set, error_count

# Corrects grammar of the sentence.
def grammar_tool(text, error_count):
	tool = language_tool_python.LanguageTool('en-US')
	corrected_text = tool.correct(text)
	error_count += 1
	return corrected_text, error_count

# Checks if the text is an equation or not. If not, then captializes the first letter, if it is in lowercase.
def case_of_eqn(content_char_set, error_count):
	operators = ["/", "*", "=", "+", "-", "%", "(", ":"]
	for i in range(5):
		for operator in operators:
			if content_char_set[i] == operator:
				return content_char_set, error_count
	return capitalize_first_char(content_char_set, error_count)

#  Capitalizes the first character of the sentence if not.
def capitalize_first_char(content_char_set, error_count):
	if content_char_set[0].islower():
		first_char = content_char_set.pop(0)
		content_char_set.insert(0, first_char.upper())
		error_count += 1
	return content_char_set, error_count

# Checks  for the text having equations and formulas.
# Add necessary spaces for the operators like "/", "*", "=", "+", "-", "%", ":"
def eqn_styles(content_char_set, error_count):
	operators = ["/", "*", "=", "+", "-", "%", ":"]
	h = "False"
	for operator in operators:
		for index in range(len(content_char_set)):
			if index == (len(content_char_set)-1):
				break
			if (content_char_set[index] == operator):
				if (content_char_set[index+1] != " "):
					content_char_set.insert(index + 1, " ")
					error_count += 1
		for index in range(len(content_char_set)):
			if index == (len(content_char_set)-1):
				break
			reverse_index = (index + 1) * (-1)
			if (content_char_set[reverse_index] == operator):
				if (content_char_set[reverse_index - 1] != " "):
					content_char_set.insert(((index + 1) * (-1)), " ")
					error_count += 1
	for index in range(len(content_char_set)):
		if index == (len(content_char_set)-1):
			break
		if content_char_set[index] == "\n":
			ops = ["/", "*", "=", "+", "-", "%", "(", ":"]
			for i in range(5):
				i += 1
				for new_op in ops:
					if (content_char_set[index + i] == new_op):
						print(content_char_set[index + i])
						h = "True"
						break
			if h == "False":
				if content_char_set[index + 1].islower():
					first_char = content_char_set.pop(index + 1)
					content_char_set.insert(index + 1, first_char.upper())
					error_count += 1
			h = "False"
	return content_char_set, error_count

#  Specific types of content checks:

# Checks for the language based questions. 
def language_type_check (question, cleaner_user):
	error_count = 0
	ques_text = question.text
	q_content_char_set = list(ques_text)
	q_content_char_set, error_count = capitalize_first_char(q_content_char_set, error_count)
	q_content_char_set, error_count = add_period(q_content_char_set, error_count)
	punct_corrected_content = "".join(q_content_char_set)
	
	if ques_text != punct_corrected_content:
		question.text = punct_corrected_content
	else:
		error_count = 0

	exp_text = question.explanation
	exp_content_char_set = list(exp_text)
	exp_content_char_set, error_count = other_styles(exp_content_char_set, error_count)
	exp_content_char_set, error_count = add_period(exp_content_char_set, error_count)
	exp_content_char_set, error_count = rem_dup_period(exp_content_char_set, error_count)
	punct_corrected_content = "".join(exp_content_char_set)
	grammar_corrected_content, error_count = grammar_tool(punct_corrected_content, error_count)	

	if exp_text != grammar_corrected_content:
		question.explanation = grammar_corrected_content
	else:
		error_count = 0

	flag = "{} grammatical and formatting errors were found.".format(error_count)
	if error_count != 0:
		ReportFlag.create(text=flag, user=cleaner_user, question=question, is_resolved = True)
		question.save()
	print(question.reports)
	return 

# Checks for the quantitative aptitude based questions.
def quant_type_check (question, cleaner_user):
	error_count = 0
	ques_text = question.text
	q_content_char_set = list(ques_text)
	q_content_char_set, error_count = add_period(q_content_char_set, error_count)
	q_content_char_set, error_count = other_styles(q_content_char_set, error_count)
	punct_corrected_content = "".join(q_content_char_set)
	grammar_corrected_content, error_count = grammar_tool(punct_corrected_content, error_count)
	if ques_text != grammar_corrected_content:
		question.text = grammar_corrected_content
	else:
		error_count = 0
	exp_text = question.explanation
	exp_content_char_set = list(exp_text)
	exp_content_char_set, error_count = case_of_eqn(exp_content_char_set, error_count)
	exp_content_char_set, error_count = other_styles(exp_content_char_set, error_count)
	exp_content_char_set, error_count = add_period(exp_content_char_set, error_count)
	exp_corrected_content = "".join(exp_content_char_set)
	if exp_text != exp_corrected_content:
		question.explanation = exp_corrected_content
	else:
		error_count = 0
	flag = "{} grammatical and formatting errors were found.".format(error_count)
	if error_count != 0:
		ReportFlag.create(text=flag, user=cleaner_user, question=question, is_resolved = True)
		question.save()
	print(question.reports)
	return 

# Checks for the logic based questions.
def logic_type_check (question, cleaner_user):
	error_count = 0
	ques_text = question.text
	q_content_char_set = list(ques_text)
	q_content_char_set, error_count = capitalize_first_char(q_content_char_set, error_count)
	q_content_char_set, error_count = add_period(q_content_char_set, error_count)
	punct_corrected_content = "".join(q_content_char_set)
	if ques_text != punct_corrected_content:
		question.text = punct_corrected_content
	else:
		error_count = 0

	exp_text = question.explanation
	exp_content_char_set = list(exp_text)
	exp_content_char_set, error_count = capitalize_first_char(exp_content_char_set, error_count)
	exp_content_char_set, error_count = add_period(exp_content_char_set, error_count)
	exp_content_char_set, error_count = eqn_styles(exp_content_char_set, error_count)
	exp_content_char_set, error_count = rem_dup_period(exp_content_char_set, error_count)
	exp_grammar_corrected_content = "".join(exp_content_char_set)
	if exp_text != exp_grammar_corrected_content:
		question.explanation = exp_grammar_corrected_content
	else:
		error_count = 0	

	flag = "{} grammatical and formatting errors were found.".format(error_count)
	if error_count != 0:
		ReportFlag.create(text=flag, user=cleaner_user, question=question, is_resolved = True)
		question.save()
	print(question.reports)
	return 

# Checks for the technical based questions.
def tech_type_check(question, cleaner_user):
	error_count = 0
	q_text = question.text 	 	
	q_content_char_set = list(q_text)
	if q_content_char_set[-1] not in ["}",")"]:
		q_content_char_set, error_count = add_period(q_content_char_set, error_count)
	grammar_corrected_content = "".join(q_content_char_set)
	if q_text != grammar_corrected_content:
		question.text = grammar_corrected_content
	else:
		error_count = 0

	exp_text = question.explanation
	exp_content_char_set = list(exp_text)
	if exp_content_char_set[-1] not in ["}",")"]:
		exp_content_char_set, error_count = add_period(exp_content_char_set, error_count)
	punct_corrected_content = "".join(exp_content_char_set)
	if exp_text != punct_corrected_content:
		question.explanation = punct_corrected_content
	else:
		error_count = 0

	flag = "{} grammatical and formatting errors were found.".format(error_count)
	if error_count != 0:
		ReportFlag.create(text=flag, user=cleaner_user, question=question, is_resolved = True)
		question.save()
	print(question.reports)
	return 	

if __name__ == "__main__":
    main(q_tags)