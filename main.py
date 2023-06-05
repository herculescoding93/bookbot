#Test program for my test repository

def countWords(string):
    return len(string.split())

def Letters(string):
    lowered = string.lower()
    totalLetters = {}
    for i in lowered:
        if i in totalLetters:
            totalLetters[i] += 1
        else:
            totalLetters[i] = 1
    return totalLetters

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d):
    return d["num"]

with open("books/frankenstein.txt", "r") as book:
    contents = book.read()
    totalWords = countWords(contents)
    totalLetters = Letters(contents)

with open("report.txt", "w+") as f:
    f.write("--- Start of report.txt ---\n")
    f.write(f"{totalWords} total words found in book\n\n")
    charsList = chars_dict_to_sorted_list(totalLetters)
    for i in charsList:
        if not i["char"].isalpha():
            continue
        f.write(f"The character '{i['char']}' was found {i['num']} times\n")
    f.write("--- End report ---")




