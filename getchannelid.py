from telethon import TelegramClient
import os

# Use your own values from my.telegram.org
id = os.environ['api_id']
hash = os.environ['api_hash']
  # Use your own values from my.telegram.org
api_id = id
api_hash = hash
client = TelegramClient('anon', api_id, api_hash)

#id=1001737335720
async def main():
  async for dialog in client.iter_dialogs():
    print(dialog.name, " ",dialog.id)
    #await client.forward_messages(-1001727182067,10,-1001737335720)
  

with client:
  client.loop.run_until_complete(main())


