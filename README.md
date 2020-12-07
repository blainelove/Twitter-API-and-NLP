# **Fun with Twitter and Natural Language Processing**

Using [Tweepy](http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html) to interact with the Twitter API, these scripts provide functions to tweet status updates as well as search Twitter to conduct basic sentiment analysis using [TextBlob](https://textblob.readthedocs.io/en/dev/index.html) library for natural language processing.

## **UpdateStatus**

Updates status with text and/or media and provides error protection.

![Twitter profile page](UpdateStatusResult.png  "Twitter profile page")

## **TwitterSearch**

Takes user input for a term to search on Twitter and conducts sentiment analysis. 
This function pulls tweets with the given term then using TextBlob, analyzes the Tweets and calculates the average subjectivity and polarity of the tweets.


Polarity is float which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement. 
Subjective sentences generally refer to personal opinion, emotion or judgment whereas objective refers to factual information. Subjectivity is also a float which lies in the range of [0,1]. 
(From [AnalyticsVidhya](https://www.analyticsvidhya.com/blog/2018/02/natural-language-processing-for-beginners-using-textblob/))

The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective. (From [TextBlobDocs](https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis))

### **Example output:** 

RT @OANN: Trump legal team to probe Mich. Dominion voting machines - https://t.co/f4SmEhZUVx #OANN

RT @MollyJongFast: Democrats were worried trump would destroy the social safety net, ignore a pandemic and crush democratic norms. Trump di…

@catturd2 What lie ? Trump admitted to what he did.

@FrankLuntz And so will Trump dip Shit. Bush was not considered president at the same time we are now last 2020 election.

RT @HeadlineZooo: @parkerbutler10 Trump skipped a GOP and general election debate. Debating suggests you believe in democracy and respect v…

RT @funder: Rudy Giuliani has the Trump Virus.

RT @TotalWorld1: 【速報】Facebookザッカーバーグ氏は極左団体に4億ドルを寄付／PAとMIの民主党州務長官は極左団体に州の有権者名簿を渡していた https://t.co/oYrKJ7awbM https://t.co/UtsKXn55pi

RT @Ramnier: Jenna Ellis asegura que la orden de un Juez de Michigan para auditar 22 máquinas de Dominion Voting Systems en el Condado de A…
this 0 followers trump supporter is on my account getting read. embarrassing 😭

@JoyAnnReid @KLoeffler She was pathetic on stage with Trump at the rally.

RT @thehill: JUST IN: Loeffler sidesteps question on Trump's claims of "rigged" election during debate https://t.co/fAl57Gar53 https://t.co…

RT @Delavegalaw: Trump's final days are not Shakespearean, the stuff of great literature, or even soap opera. Trump is a falling-apart lowl…

RT @ruthbenghiat: Why is the Washington Post hosting Kudlow, who has lied to the press for years to please Trump and endangered lives w/his…



### **Average subjectivity is 0.22521367521367525**

### **Average polarity is -0.03632478632478632**