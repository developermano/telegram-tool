import os
from telethon import TelegramClient, events
from tinydb import TinyDB, Query

from server import keepalive


keepalive()


db = TinyDB('db.json')
User = Query()

def main():
  id = os.environ['api_id']
  hash = os.environ['api_hash']
  # Use your own values from my.telegram.org
  api_id = id
  api_hash = hash
  client = TelegramClient('anon', api_id, api_hash)


  @client.on(events.NewMessage)
  async def my_event_handler(event):
      print(event)
      channelid=event.peer_id.channel_id
      for i in getdata():
        print(i,channelid)
        chatid=str(i['toid'])
        if "-100"+str(channelid)==str(i['fromid']):
          #print(chatid,event.id,str(i['fromid'])[4:])
          await client.forward_messages(int(i['toid']),event.id,int(i['fromid']))

  client.start()
  client.run_until_disconnected()





def insertdata(fromchannel,tochannel):
  global db
  db.insert({"fromid":fromchannel,"toid":tochannel})


def getdata():
  global db
  return db.all()



if __name__=="__main__":
  main()