def doc_to_text(x):
    question = x["question"].strip()
    choices = x["options"]
    inp = f"{question}"
    for idx, choice in enumerate(choices):
        inp = inp + f"\\n{choice['value']}. {choice['text']}"
    return inp + "\\nRisposta:"


def doc_to_choice(x):
    choices = x["options"]
    answers = []
    for idx, choice in enumerate(choices):
        answers.append(choice['key'])
    return answers