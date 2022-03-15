import string


def main():
    word_dict, doc_dict = read_files()
    while True:
        try:
            # create menu
            i = int(input("What would you like to do?\n"
                          "1. search for documents\n"
                          "2. Read Document\n"
                          "3. Quit program\n"))
            # call correct function depending on user input
            if i == 1:
                search_docs(word_dict)
            elif i == 2:
                i = int(input("Enter document number:"))
                display_doc(i, doc_dict)
            elif i == 3:
                exit()
        except KeyError:
            print('ugh')
            # i = int(input("Invalid input, please try again: "))           #?


# function reads the files and creates word_dict (words and corresponding document numbers)
# and doc_dict (document numbers and corresponding text)
def read_files():
    f = open('ap_docs2.txt', 'r')
    text = f.read()

    # list of the documents where the line breaks ar removed
    docs_list = text.split('<NEW DOCUMENT>')
    docs_list = [s.strip().replace('\n', ' ') for s in docs_list]
    docs_list.remove('')
    f.close()

    # set of all words in all documents
    word_set = set()
    for doc in docs_list:
        # all words in the document are stripped of punctuation and uppercase letters
        words = doc.strip(string.punctuation).lower().split()
        for i in range(0, len(words)):
            word_set.add(words[i])

    # doc dict contains document numbers and corresponding text
    doc_dict = dict()
    for j in docs_list:
        doc_dict[docs_list.index(j) + 1] = j

    # word dict contains all words and corresponding document numbers the word is present in
    word_dict = dict()
    stripped_doc = [x.lower().strip(string.punctuation) for x in doc_dict.values()]
    for k in stripped_doc:
        for l in word_set:
            if l in k:
                if l in word_dict:
                    word_dict[l] = word_dict[l] + ', ' + str(stripped_doc.index(k) + 1)
                else:
                    word_dict[l] = set(stripped_doc.index(k) + 1)       #?
                    print(word_dict[l])
                # if l in word_dict:
                #     word_dict[l] = word_dict[l] + ', ' + str(stripped_doc.index(k) + 1)
                # else:
                #     word_dict[l] = str(stripped_doc.index(k) + 1)
    print(word_dict)
    return word_dict, doc_dict


def search_docs(word_dict):
    k = input("Enter search words: ")
    k = k.lower().strip()
    search_words = k.split()
    doc_sets_list = []
    m = [word_dict[w] for w in search_words if w in word_dict]
    for sw in m:
        sw = sw.split(',')
        sw = {x.strip() for x in sw}
        doc_sets_list.append(sw)
    result = list(set.intersection(*doc_sets_list))
    result.sort()
    result = ' '.join(result)
    print('Documents fitting search:')
    print(result, '\n')


def display_doc(doc_number, doc_dict):
    sentences = doc_dict[doc_number].replace('.', '.\n')
    print("Document #{}".format(doc_number))
    print("-" * 25)
    print(sentences)
    print("-" * 25)


main()
