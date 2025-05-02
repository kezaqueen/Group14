def hello():
    print('Hello AkiraChix')
     


def say_hello(name):
    print(f"Hello {name}")


def greet(name, age):
    year = 2025 - age
    print(f'Hello {name}, born in {year}')


def greetings(names):
    for name in names:
        print(f'Hello {name}')

def year_of_birth(name,age):
    year = 2025 - age
    print(f'Hello {name}, born in {year}')

def my_country(name = 'Uganda'):
    print(f'I love my country,{name}')


# 
def welcome_student(**kwargs):
    print(kwargs)


def create_sentence(**words):
    sentence = ''
    for word in words.values():
        sentence += word
        sentence += ''
    return sentence



def exam_result(*args,  **kwargs):
    print(args)
    print(kwargs)


def student_info(name, course, *scores):
    total_score = sum(scores)
    average_score = total_score / len(scores)
    print(f 'Student Name: {name}')
    print(f 'course: {course}')
    print(f 'Average Score: {average_score:.2f}')
