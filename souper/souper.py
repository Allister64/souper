import requests
from bs4 import BeautifulSoup

place = 0


# opens the three input text files and stores contents in list
a_file = open("book.txt", "r")

bookList = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  bookList.append(line_list)

a_file.close()

b_file = open("chapter.txt", "r")

chapterList = []
for line in b_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  chapterList.append(line_list)

b_file.close()

c_file = open("verse.txt", "r")

verseList = []
for line in c_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  verseList.append(line_list)

c_file.close()



# does the scraping are returns formatted result
def text_output(x):
  page = requests.get(("https://www.biblegateway.com/passage/?search={}+{}%3A{}&version=NKJV&interface=print").format(''.join(bookList[x]),''.join(chapterList[x]),''.join(verseList[x])))
  soup = BeautifulSoup(page.content, 'lxml')
  found = soup.find("meta", property="og:description")
  return(found["content"] + "{{DQP}}" + ''.join(bookList[x]) + " " +
   ''.join(chapterList[x]) + ":" + ''.join(verseList[x]))


# writes the output of the above function to a text file
with open("output.txt", "a") as outputFile:
  for i in bookList:
    outputFile.write(text_output(place))
    outputFile.write("\n")
    print(text_output(place))
    place = place + 1
