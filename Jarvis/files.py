def search (word, text):
    results = []
    for line in enumerate (text,1):
        if line[1].find(word) >= 0:
            results.append(line)
    return results

def main():
    with open('test.txt') as f:
        zop = f.readlines()
        print(zop)

    word = input("Enter search word: ")
    results = search(word, zop)
    for result in results:
        print(word, ' appears on line ', result[0], ":", result[1], sep='', end='')

main()
