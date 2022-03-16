import string


def main():
    word_dict, doc_dict = read_files()
    while True:
        try:
            # create menu
            i = int(input("What would you like to do?\n"
                          "1. Search for documents\n"
                          "2. Read Document\n"
                          "3. Quit program\n"))
            # call correct function depending on user input
            if i == 1:
                search_docs(word_dict)
            elif i == 2:
                doc_input = int(input("Enter document number:"))
                display_doc(doc_input, doc_dict)
            elif i == 3:
                exit()
        except ValueError:
            print("Invalid input, please try again: ", '\n')
        except KeyError:
            print("Invalid input, please try again: ", '\n')


# function reads the files and creates word_dict (words and corresponding document numbers)
# and doc_dict (document numbers and corresponding text)
def read_files():
    f = open('ap_docs.txt', 'r')
    text = f.read()

    # list of the documents where the line breaks are removed
    docs_list = text.split('<NEW DOCUMENT>')
    docs_list = [s.strip() for s in docs_list]      #
    docs_list.remove('')
    f.close()

    # doc dict contains document numbers and corresponding text
    doc_dict = dict()
    for j in docs_list:
        doc_dict[docs_list.index(j) + 1] = j

    # set of all words in all documents
    word_set = set()
    for doc in docs_list:
        # all words in the document are stripped of punctuation and uppercase letters
        words_list = doc.strip(string.punctuation).lower().split()
        for i in range(0, len(words_list)):
            word_set.add(words_list[i])

    # word dict contains all words and corresponding document numbers the word is present in
    word_dict = {}
    stripped_doc = [x.lower().strip(string.punctuation) for x in doc_dict.values()]
    for k in stripped_doc:
        for ws in word_set:
            if ws in k:
                # to make sure we add the word only once to the dictionary
                # and have all the document numbers corresponding to one key
                if ws in word_dict:
                    word_dict[ws].add(stripped_doc.index(k) + 1)
                else:
                    word_dict[ws] = {stripped_doc.index(k) + 1}
    return word_dict, doc_dict


# function that takes user search input and returns relevant document numbers
def search_docs(word_dict):
    try:
        k = input("Enter search words: ")
        k = k.lower().strip(string.punctuation)
        search_words = k.split()
        doc_sets_list = [word_dict[w] for w in search_words if w in word_dict]
        result = list(set.intersection(*doc_sets_list))

        # when the result list is empty rais an exception
        if len(result) == 0:
            raise ValueError

        # formatting results to print
        result.sort()
        res = [str(a) for a in result]
        res = ' '.join(res)

        print('Documents fitting search:', res, sep='\n')
    except TypeError:
        print("No relevant documents found", '\n')
    except ValueError:
        print("No relevant documents found", '\n')


# function to display a specific document
def display_doc(doc_number, doc_dict):
    f = "-" * 25
    print("Document #{}".format(doc_number), f, doc_dict[doc_number], f, sep='\n')


main()
