def capitalize(values):
    for value in values:
         yield value.upper()


def hyphenate(values):
    for value in values:
        yield f"-{value}-"


def leetspeak(values):
    for value in values:
        if value in {'t', 'T'}:
            yield '7'
        elif value in {'e', 'E'}:
            yield '3'
        else:
            yield value


def join(values):
    return "".join(values)


if __name__ == "__main__":
    text = "This is processed text"

    print("join(leetspeak(text)) result:")
    print(join(leetspeak(text)))
    print("join(hyphenate(text.split())) result:")
    print(join(hyphenate(text.split())))
