def get_num_words(filepath):
    with open(filepath) as f:
        words = f.read().split()
        wordCount = len(words)
        return wordCount

def get_char_num(filepath):
    with open(filepath) as f:
        string = f.read().strip().lower()
        charCount = {}
        for char in string:
            if char.isalpha():
                charCount[char] = charCount.get(char, 0) + 1
        return charCount

def report(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(filepath)} total words")
    print("--------- Character Count -------")
    char_count = get_char_num(filepath)
    char_info = {}
    for char, count in char_count.items():
        char_info[char] = {"char": char, "num": count}
    for i in char_info:
        print(f"{char_info[i]["char"]}: {char_info[i]["num"]}")
    print("============= END ===============")
        