def concat_words(words:list[str]) -> str:
    letters = [word[i] for i, word in enumerate(words)]
    return ''.join(letters)

def main():
    w = ['yoda', 'best', 'has']
    print(concat_words(w))

if __name__ == '__main__':
    main()