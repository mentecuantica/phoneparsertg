import asyncio
import csv
import os
from telethon.sync import TelegramClient
from telethon.tl.types import User

from configparser import ConfigParser
config = ConfigParser()
config.read('config.ini')
api_id = config.get('main','api_id')
username = config.get('main','username')
api_hash = config.get('main','api_hash')

client = TelegramClient(username, api_id, api_hash)
client.start()

current_dir = os.path.abspath(os.path.dirname(__file__))
csv_dir = os.path.join(current_dir,'csv')
if not os.path.exists(csv_dir):
    os.mkdir(csv_dir)

loop = asyncio.get_event_loop()
async def main():
    url = input("Enter link to a channel or chat: ")
    channel = await client.get_entity(url)
    await dump_all_participants(channel,url)


async def dump_all_participants(channel,url):
    """Writes a csv-file with info about all with phones participants"""

    all_phone_participants = []

    #to override 10000 limit, we use client.get_participants(aggressive=True)
    participants = await client.get_participants(channel,None,aggressive=True)
    print(f"All participants: {len(participants)}")
    for participant in participants:
        participant:User
        if participant.phone is not None:
            all_phone_participants.append(participant)
    print(f"All phone participants: {len(all_phone_participants)}")

    filename = url+'.csv'
    full_file_name = os.path.join(csv_dir,filename)
    with open(full_file_name,mode="w",encoding='utf-8',newline='') as csv_file:
        fieldnames = ['phone','first_name', 'last_name', 'username']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for participant in all_phone_participants:
            participant:User
            writer.writerow({'phone':participant.phone,'first_name':participant.first_name,'last_name':participant.last_name,
                             'username':participant.username})


loop.run_until_complete(main())