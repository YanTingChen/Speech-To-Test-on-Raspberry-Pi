#coding=utf-8
import subprocess
import json
import MySQLdb

subprocess.call("arecord -D plughw:1,0 -d 4 test.wav".split())
subprocess.call("ffmpeg -i  test.wav -ar 16000 -acodec flac test.flac".split())
#sudo wget -q -U "Mozilla/5.0" --post-file s.flac --header "Content-Type: audio/x-flac; rate=16000" -O - "http://www.google.com/speech-api/v2/recognize?output=json&lang=en_us&key=AIzaSyC-IWsssM-e_MtTkSswKp8nwx5i8kqS9ws&client=chromium" > out.txt
subprocess.call("sudo wget -q -U \"Mozilla/5.0\" --post-file test.flac --header \"Content-Type: audio/x-flac; rate=16000\" -O - \"http://www.google.com/speech-api/v2/recognize?output=json&lang=zh_tw&key=AIzaSyC-IWsssM-e_MtTkSswKp8nwx5i8kqS9ws&client=chromium\" > test.txt",shell=True)
subprocess.call("sudo rm test.flac".split())
subprocess.call("sudo rm test.wav".split())
#subprocess.call("cat test.txt".split())

file = open("test.txt")
f = file.readlines()

for i in f:	
	data=i.rstrip("\n")
	data_string = json.dumps(data,separators=(',',':'))
	decoded = json.loads(data_string)
	decoded=decoded.replace('"','')
	decoded=decoded.replace('[','')
	decoded=decoded.replace(']','')
	decoded=decoded.replace('{','')
	decoded=decoded.replace('}','')
	decoded=decoded.replace(':','')
	decoded=decoded.replace('result','')
	decoded=decoded.replace('confidence','')
	decoded=decoded.replace('alternative','')
	decoded=decoded.replace('transcript','')
	decoded=decoded.replace('final','')
	decoded=decoded.replace('true','')
	decoded=decoded.replace('_index0','')
file.close()		
a=decoded.rstrip(",,")
#print a 
sStr= ','   
c=a.find(sStr)
fin=a[0:c]
#print fin

db = MySQLdb.connect(host="163.17.136.196", user="YanTing", passwd="waVH38aBpG85Jq3y", db="test")
cursor = db.cursor()

sql="insert into testdb(text) values (%s)"
try:
	cursor.execute(sql,fin)
	db.commit()
except:
	db.rollback()	
cursor.execute("SELECT * FROM testdb")
result = cursor.fetchall()
for record in result:
    print str(record[0])+' '+record[1]
db.close
subprocess.call("sudo rm test.txt".split())	