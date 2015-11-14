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
            print "      *Greate!"
            break
        except:
            print "   *Page not found!"


def enter_of_answers():
    answer_one = insert_url()
    answer_two = insert_url()
    print "The answer is:"
    return answer_one, answer_two


insert_url()