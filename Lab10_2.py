def read_file(filen):
    try:
        file = open(filen, 'r', encoding='utf-8')
        content = file.read()
        if not content:
            raise Exception(f"файл {filen} пустой")
        print(content)
    except Exception as e:
        print(str(e))
read_file('pusto')
read_file('nepusto')