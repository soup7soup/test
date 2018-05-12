import  json ,  config
from  requests_oauthlib  import  OAuth1Session
import urllib
import random
import datetime

counter = 0

def downloader(image_url, extension):
 try: 
    global counter
    random_name = str(random.randrange(100000))
    currentDT = datetime.datetime.now()
    now = currentDT.strftime("%Y%m%d%H%M%S")
    full_file_name = str(random_name + "_T_"+ now +"."+extension)

    local_filename, headers = urllib.request.urlretrieve(image_url,full_file_name)
    print(local_filename)
    html = open(local_filename)
    html.close()
    if(local_filename is not None) :
        counter = counter +1
    print('-------------------------生成-------------------------')

 except IOError:
    print('An error occurred trying to read the file.')

 except ValueError:
    print('Non-numeric data found in the file.')

 except ImportError:
    print("NO module found")

 except EOFError:
    print('Why did you do an EOF on me?')

 except KeyboardInterrupt:
    print('You cancelled the operation.')

 except:
    print('An error occurred.')

CK  =  config . CONSUMER_KEY
CS  =  config . CONSUMER_SECRET
AT  =  config . ACCESS_TOKEN
ATS  =  config . ACCESS_TOKEN_SECRET
twitter  =  OAuth1Session ( CK ,  CS ,  AT ,  ATS )


url = "https://api.twitter.com/1.1/search/tweets.json"
print("Enterを押すと、JustinBieberの写真をダウンロードします。")
keyword = input('>> ')
keyword = "JustinBieber"
print('----------------------実行開始----------------------')

params = {'q' : keyword, 'count' : 100, 'include_entities' : 'true'}

req = twitter.get(url, params = params)

if req.status_code == 200:
    search_timeline = json.loads(req.text)
    for tweet in search_timeline['statuses']:
        if tweet['entities'].get("media",None) is not None and counter < 10:
            pic_url = tweet['entities'].get("media",None)[0].get('media_url',None)

            if pic_url.find('/'):
               file_name = pic_url.rsplit('/', 1)[1]
               extension = file_name.rsplit('.', 1)[1]

            #save image
            downloader(pic_url, extension)

else:
    print("ERROR: %d" % req.status_code)

input('\nPress ENTER to exit')
