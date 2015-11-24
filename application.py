"""Search engine"""
import urllib2
import re

def insert_url():
    print ""
    pages = True
    while pages == True:
        try:
            page = raw_input("Enter a valid URL: ")
            comp_page = "http://" + str(page)
            apply_for_url = urllib2.urlopen(str(comp_page))
            reading = apply_for_url.read()
            apply_for_url.close()
            print "      Greate! XD "
            return comp_page, reading
            break
        except:
            print "   Page not found! :("



def enter_of_answers():
    link1, answer_one = insert_url()
    link2, answer_two = insert_url()
    insert_word(answer_one,answer_two,link1,link2)


def insert_word(answer_one,answer_two,link1,link2):
    print ""
    words = True
    while words == True:
        word = raw_input("What word you want to find? ")
        answer_word = str(word).isspace()
        emptynumb = len(word)
        if answer_word == False and emptynumb > 0:
            searcher1 = re.findall(word, answer_one)
            searcher2 = re.findall(word, answer_two)
            coincidence1 = length(searcher1,searcher2)
            coincidence2 = length(searcher1,searcher2)
            print " On page to ",link1 +"it was found: ",coincidence1,"words."
            print " On page to ",link2 +"it was found: ",coincidence2,"words."
            print " "
            print_recomending(coincidence1,coincidence2,link1,link2)
            break
        else:
            print "Enter some data"

def length(searcher1,searcher2):
    search1 = len(searcher1)
    return search1
    search2 = len(searcher2)
    return search2

def print_recomending(coincidence1,coincidence2,link1,link2):
    if coincidence1 > coincidence2:
        print"  We recommend",link1,"because it has more matches."
    elif coincidence2 > coincidence1:
        print"  We recommend",link2,"because it has more matches."
    elif coincidence1 == coincidence2:
        print "You can visit any website, because the results are the same."
    else:
        "No matches found."


enter_of_answers()