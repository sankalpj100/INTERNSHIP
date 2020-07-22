from quiz_app.models import Question, QuestionType, Tag, ReportFlag
from quiz_app.database import db
import language_tool_python

def main():
	question_content_check ()

def filter_questions(tags):
    questions = Question.query.filter()
    print("total", questions.count(), "questions")
    for tag in tags:
        questions = questions.filter(
            Question.tags.any(Tag.text == tag)
        )
    print("filtered", questions.count(), "questions")
    return questions


def question_content_check ():
	row = 0
	serial = 0
	i = 0
	tag_all_lang = ["tcs", "language"]
	tag_all_quant = ["infosys", "quantitative"]
	tag_all_logic = ["infosys", "logical"]
	tag_all_tech = ["infosys", "technical"]
	lang_questions = filter_questions(tag_all_lang)
	quant_questions = filter_questions(tag_all_quant)
	logic_questions = filter_questions(tag_all_logic)
	tech_questions = filter_questions(tag_all_tech)
	for question in lang_questions.all():
		if i < 1 :
			row, serial  =  language_type_check(question, row, serial)
			i += 1
		else:
			break
	return

def add_period(content_char_set, error_count):
	if (content_char_set[-1] != ("." or "?")):
		content_char_set.append(".")
		error_count += 1
	return content_char_set, error_count

def other_styles(content_char_set, error_count):
	for index in range(len(content_char_set)):
		reverse_index = (index + 1) * (-1)
		if (content_char_set[reverse_index] == "\n"):
			if(content_char_set[reverse_index - 1] != "\n"):
				content_char_set.insert(((index + 1) * (-1)), ".")
				error_count += 1
	for index in range(len(content_char_set)):
		if (content_char_set[index] == ":"):
			content_char_set.insert(index + 1, " ")
			error_count += 1
	for index in range(len(content_char_set)):
		reverse_index = (index + 1) * (-1)
		if (content_char_set[reverse_index] == ":"):
			if (content_char_set[reverse_index - 1] != " "):
				content_char_set.insert(((index + 1) * (-1)), " ")
				error_count += 1
	for index in range(len(content_char_set)):
		reverse_index = (index + 1) * (-1)
		if (content_char_set[reverse_index] == ","):
			if (content_char_set[reverse_index- 1] != " "):
				content_char_set.insert((((index + 1) * (-1)) + 1), " ")
				error_count += 1
	for index in range(len(content_char_set)):
		reverse_index = (index + 1) * (-1)
		if (content_char_set[reverse_index] == "."):
			if (content_char_set[reverse_index - 1] == " "):
				content_char_set.pop(reverse_index - 1)
				error_count += 1
	return content_char_set, error_count

def rem_dup_period(content_char_set, error_count):
	for index in range(len(content_char_set)):
		reverse_index = (index + 1) * (-1)
		if (content_char_set[reverse_index] == "."):
			if (content_char_set[reverse_index - 1] == "."):
				content_char_set.pop(reverse_index - 1)
				error_count += 1
			if (content_char_set[reverse_index + 1] == "."):
				content_char_set.pop(reverse_index + 1)
				error_count += 1
	return content_char_set, error_count

def grammar_tool(text):
	tool = language_tool_python.LanguageTool('en-US')
	corrected_text = tool.correct(text)
	return corrected_text

def case_of_eqn(content_char_set, error_count):
	operators = ["/", "*", "=", "+", "-", "%", "("]
	for i in range(5):
		for operator in operators:
			if exp_content_char_set[i] == operator:
				return content_char_set
	return capitalize_first_char(content_char_set, error_count)

def capitalize_first_char(content_char_set, error_count):
	if content_char_set[0].islower():
		first_char = content_char_set.pop(0)
		content_char_set.insert(0, first_char.upper())
		error_count += 1
	return content_char_set, error_count

def language_type_check (question, row, serial):
	serial += 1
	row += 1 
	# ADD TO MATTER TO THE WORKBOOK
	error_count = 0
	ques_text = question.text
	print("Before:", ques_text)
	q_content_char_set = list(ques_text)
	q_content_char_set, error_count = capitalize_first_char(q_content_char_set, error_count)
	q_content_char_set, error_count = add_period(q_content_char_set, error_count)
	punct_corrected_content = "".join(q_content_char_set)
	print("After:", punct_corrected_content)
	# question.text = punct_corrected_content

	exp_text = question.explanation
	print("Before:", exp_text)
	exp_content_char_set = list(exp_text)
	exp_content_char_set, error_count = other_styles(exp_content_char_set, error_count)
	exp_content_char_set, error_count = add_period(exp_content_char_set, error_count)
	exp_content_char_set, error_count = rem_dup_period(exp_content_char_set, error_count)
	punct_corrected_content = "".join(exp_content_char_set)
	grammar_corrected_content= grammar_tool(punct_corrected_content)
	print("After:", grammar_corrected_content)
	# question.explaination = grammar_corrected_content
	# print(question.reports.ReportFlag.text)
	question = Question(text=punct_corrected_content, explanation=grammar_corrected_content)
	flag = "{} Grammatical and Style errors".format(error_count)
	print(flag)
	question.save()
	return row, serial

# def quant_type_check (question, row, serial):
# 	serial, row += 1
# 	# ADD TO MATTER TO THE WORKBOOK
# 	worksheet.write(row, 0, serial)

#     ques_text = question
#     q_content_char_set = list(ques_text)
# 	q_content_char_set, error_count = add_period(q_content_char_set, error_count)
# 	q_content_char_set, error_count = other_styles(q_content_char_set, error_count)
# 	punct_corrected_content = "".join(q_content_char_set)
# 	grammar_corrected_content= grammar_tool(punct_corrected_content)
# 	worksheet.write(row, 1, grammar_corrected_content)

# 	exp_text = question.explaination
# 	exp_content_char_set = list(exp_text)
# 	exp_content_char_set, error_count = case_of_eqn(exp_content_char_set, error_count)
# 	exp_content_char_set, error_count = add_period(exp_content_char_set, error_count)
# 	exp_content_char_set, error_count = rem_dup_period(exp_content_char_set, error_count)
# 	exp_corrected_content = "".join(exp_content_char_set)

# 	flag = "{} Grammatical and Style errors".format(error_count)
# 	return row, serial 

# def logic_type_check (question, row, serial):
# 	ques_text = question
#     q_content_char_set = list(ques_text)
# 	q_content_char_set, error_count = capitalize_first_char(q_content_char_set, error_count)
# 	q_content_char_set, error_count = add_period(q_content_char_set, error_count)
# 	punct_corrected_content = "".join(q_content_char_set)
# 	worksheet.write(row, 1, punct_corrected_content)

# 	exp_text = question.explaination
# 	exp_content_char_set = list(exp_text)
# 	exp_content_char_set, error_count = first_char(exp_content_char_set, error_count)
# 	exp_content_char_set, error_count = add_period(exp_content_char_set, error_count)
# 	exp_grammar_corrected_content = "".join(exp_content_char_set)
# 	worksheet.write(row, 2, exp_grammar_corrected_content)

# 	flag = "{} Grammatical and Style errors".format(error_count)
# 	return row, serial 

# def tech_type_check(question, row, serial)():
# 	serial, row += 1
	    
#     q_text = question.explaination
# 	q_content_char_set = list(q_text)

# 	if q_content_char_set[-1] != "}" or ")":
# 		q_content_char_set, error_count = add_period(q_content_char_set, error_count)
# 	punct_corrected_content = "".join(q_content_char_set)
# 	worksheet.write(row, 1, punct_corrected_content)

# 	exp_text = question.explaination
# 	exp_content_char_set = list(exp_text)

# 	if exp_content_char_set[-1] != "}" or ")":
# 		exp_content_char_set, error_count = add_period(exp_content_char_set, error_count)
# 	punct_corrected_content = "".join(exp_content_char_set)

# 	flag = "{} Grammatical and Style errors".format(error_count)
# 	return row, serial	

if __name__ == "__main__":
    main()