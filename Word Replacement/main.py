def replaceX():
    string="On am we offices expense thought. Its hence ten smile age means. Seven chief sight far point any. Of so high into easy. Dashwoods eagerness oh extensive as discourse sportsman frankness. Husbands see disposed surprise likewise humoured yet pleasure. Fifteen no inquiry cordial so resolve garrets as. Impression was estimating surrounded solicitude indulgence son shy."
    word_to_replace=input("provide the word u want to replace")
    if (word_to_replace not in string):
        print("the word u want to replace is does not exist in the text     :  ")
        replaceX()
    else:
        word_replacement=input("provide the word u  want to replace with    :   ")
       
        print(f"\nyour new string is \n{ string.replace(word_to_replace,word_replacement)}")
if(__name__ == "__main__"):
    replaceX()