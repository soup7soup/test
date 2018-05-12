import urllib.request
import re
import pprint

print("Enterを押すと、https://no1s.biz/中のURLを収集します。")
input(">>")
print('----------------------実行開始----------------------')

try:
 urls = "https://no1s.biz/"
 html_file = urllib.request.urlopen(urls)
 urlSet = {}
 html_text = html_file.readlines()
 name = None


 for line in html_text:

        new_line = str(line, 'utf-8')

        if "href" in new_line:

          match2 = re.search('>(.*?)</a>', new_line)

          if match2:
             getStr = match2.group(0)
             if re.findall("<span>(.*?)</span>", getStr): 
                name = re.findall("<span>(.*?)</span>", getStr)
             elif re.findall("title=\"(.*?)\"", getStr):
                name = re.findall("title=\"(.*?)\"", getStr)
             elif re.findall("class=\"more\"", getStr):
                name = re.findall("</span>(.*?)<a", getStr)
             elif re.findall("\">(.*?)</a>", getStr):   
                name = re.findall("\">(.*?)</a>", getStr)
             else:   
                if re.findall("class=\"", getStr) is None:
                  plain_list = re.findall(">(.*?)</a>", getStr)
                  plain_text = str(plain_list)
                  chg_text_0 = plain_text.replace("&nbsp;","")
                  chg_text_1 = chg_text_0.replace("&gt;","")
                  name = chg_text_1

             nameStr = str(name)

             if nameStr is not None:
                url = None
                if re.findall("onclick=\"(.*?)\"", getStr):
                   url = re.findall('<a href=\"(.*?) onclick', getStr)
                else:
                   url = re.findall('<a href=\"(.*?)\">', getStr) 
                urlStr = str(url)
                if len(urlStr) > 5:
                   if len(re.findall(" class=\"more", urlStr)) == 0:
                           urlSet[urlStr[2:len(urlStr)-2]] = nameStr[2:len(nameStr)-2]
                   

 for k, v in urlSet.items():
    print(k, v)
    
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
    
input('\nPress ENTER to exit')
