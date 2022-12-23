import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
import lovins

def stem_by_porterstemmer(str):
    print("*************PORTER STEMMER******************")

    ps = PorterStemmer()

    tokens = [each_word for each_word in str.split(" ")]


    stemmed_dict = {every_word: ps.stem(every_word) for every_word in tokens }

    print("Stemmed output for each word in input string is : {0}".format(stemmed_dict))
    return stemmed_dict







def stem_by_snowballstemmer(str):
    print("*************SnowBall STEMMER ******************")
    ss = SnowballStemmer('english')
    tokens = [each_word for each_word in str.split(" ")]
    stemmed_dict = {every_word: ss.stem(every_word) for every_word in tokens}

    print("Stemmed output for each word in input string is : {0}".format(stemmed_dict))
    return stemmed_dict



def stem_by_lovins(str):
    print("******** STEM by LOVINS *************")

    tokens = [each_word for each_word in str.split(" ")]
    stemmed_dict = {output: lovins.stem(output) for output in tokens}
    print("Stemmed output for each word in input string is : {0}".format(stemmed_dict))


#Driver Code
stem_by_porterstemmer("impress impression impressive impresively")
stem_by_snowballstemmer("indicate indication indicative indicatively")
stem_by_lovins("indicate indication indicative indicatively")