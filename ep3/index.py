def converter(conv):
    eur = 4168.79
    ary = 0.00024

    if conv[:2] == "AE":
        print(float(conv[3:])*ary)
    elif conv[:2] == "EA":
        print(float(conv[3:])*eur)

converter("AE 4000")