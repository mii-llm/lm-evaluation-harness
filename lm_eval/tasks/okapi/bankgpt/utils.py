def doc_to_text(x):
    question = x["question"].strip()
    choices = x["options"]
    inp = f"{question}"
    _keys = ["A", "B", "C", "D", "E", "F"]
    for _key in _keys:
        inp = inp + f"\\n{_key}. {choices[_key]}"
    return inp + "\\nRisposta:"


def doc_to_choice(x):
    choices = x["options"]
    answers = []
    for idx, choice in enumerate(choices):
        answers.append(choice['value'])
    return answers