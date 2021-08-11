import requests

f=open('btc.txt')  
f1=open('out.txt','w')
i=0
for line in f.readlines():
 r = requests.get("http://blockchain.info/q/pubkeyaddr/"+line.strip())
 pub=str(r.content)
 pub=pub.replace("b'","")
 pub=pub.replace("'","")
 if pub!='Maximum concurrent requests for this endpoint reached. Please try again shortly.':
  print(pub)
  f1.write(line.strip()+';'+pub+'\n')  
 else:
  r = requests.get("http://blockchain.info/q/pubkeyaddr/"+line.strip())
  pub=str(r.content)
  pub=pub.replace("b'","")
  pub=pub.replace("'","") 
  f1.write(line.strip()+';'+pub+'\n')
 #f1.write(line.strip()+';'+str(balance)+';'+r.content+'\n')

f.close()
f1.close()
sleep(1)
