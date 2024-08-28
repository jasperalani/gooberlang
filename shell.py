import goober

while True:
    text = input("Goober > ")
    result, error = goober.run('<stdin>', text)
    if error:
        print(error.as_string())
    else:
        print(result)
