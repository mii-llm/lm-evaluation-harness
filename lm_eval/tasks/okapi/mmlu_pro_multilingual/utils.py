from functools import partial


voc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def doc_to_text(x):
    question = x["question"].strip()
    choices = x["options"]
    inp = f"{question}"
    for idx,choice in enumerate(choices):
        inp = inp + f'\\n{voc[idx]}. {choice}'
    return inp + "\\nRisposta:"

def doc_to_choice(x):
    choices = x["options"]
    answers = []
    for idx, choice in enumerate(choices):
        answers.append(voc[idx])
    return answers

def process_docs(dataset, subject):
    return dataset.filter(lambda x: x["category"] == subject)

process_biology = partial(process_docs, subject="biology")
process_business = partial(process_docs, subject="business")
process_chemistry = partial(process_docs, subject="chemistry")
process_computer_science = partial(process_docs, subject="computer science")
process_economics = partial(process_docs, subject="economics")
process_engineering = partial(process_docs, subject="engineering")
process_health = partial(process_docs, subject="health")
process_history = partial(process_docs, subject="history")
process_law = partial(process_docs, subject="law")
process_math = partial(process_docs, subject="math")
process_other = partial(process_docs, subject="other")
process_philosophy = partial(process_docs, subject="philosophy")
process_physics = partial(process_docs, subject="physics")
process_psychology = partial(process_docs, subject="psychology")

