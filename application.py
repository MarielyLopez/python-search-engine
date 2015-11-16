# Aqui escribe tu codigo

print "Hello World"

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
            print "      Greate!"
            break
        except:
            print "   Page not found! :("


def enter_of_answers():
    answer_one = insert_url()
    answer_two = insert_url()
    insert_word()


def insert_word(reading):
    print ""
    word = raw_input("What word you want to find? ")
    answer_word = str(word).isspace()
    emptynumb = len(word)
    if answer_word == False and emptynumb > 0:
        searcher = re.findall(word, reading)
        coincidence = len(searcher)
    else:
        print "Enter some data"

def verific_num_words():




        if coincidence > coincidencetwo:
            print ""
            print "Words found on", str(tofind), ":", str(coincidence)
            print "Words found on", str(tofindtwo), ":", str(coincidencetwo)
            print ""
            print "  >>*We recommend", str(tofind), "because it has more matches."
            break
        elif coincidencetwo > coincidence:
            print ""
            print "Words found on", str(tofind), ":", str(coincidence)
            print "Words found on", str(tofindtwo), ":", str(coincidencetwo)
            print ""
            print "We recommend", str(tofindtwo), "because it has more matches."
            break
        elif coincidence == coincidencetwo:
            print ""
            print "Words found on", str(tofind), ":", str(coincidence)
            print "Words found on", str(tofindtwo), ":", str(coincidencetwo)
            print ""
            print "You can visit any website, because the results are the same."
            break
        else:
            print ""
            print "No matches found."
            break
    else:
        print "Enter some data"



#insert_url()
enter_of_answers()