import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    

    #Prepare dictionary from the sentiment score file

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    #Load twitter data in dictionary
    data = []
    
    for line in tweet_file:
        data.append(json.loads(line))

    #iterate dictionary
    for value in data:
        if 'text' in value.keys():
            temp =  value['text'].encode('utf-8')
            sentVal = 0
            for item in scores:
                #print item
                #print scores[item]
                if temp.find(item) >=0 :
                    #print temp
                    #print item
                    sentVal += scores[item]
            print sentVal
    

if __name__ == '__main__':
    main()
