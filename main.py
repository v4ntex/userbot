import os
from pyrogram import Client, filters, enums
from pyrogram.types import Message
import asyncio
import logging
import sys
from sys import executable
from os import execvp
import time
from random import choice
from dotenv import load_dotenv

load_dotenv(".env")

API_ID=14645805
API_HASH="5f4481e1aad831e5abde0c49c3c4c24d"
STRING_SESSION="BQAhIHQAsaEyrbKST7PlvOpW7NjsNg1jgv2xlQ1G1aeEz9JsSAHZtfze27DkDqzpy1-QOz711kIM5vXwtNEIjOBY9rbQRBTRvQl9t1VcrmKixuZySq6cBwRJ1kEyFN415FwhOg0I2RABY-HnWZS6goQiVI3KnMe_jp3FbTG90v_qeSQy_Rlu0V4imDAeMiXlCo4MZ4J7fRF6DA3Keuy_Z0xB3I0OdSoYd3hbFMeza7aV4NyLeOgpWnN_aA8ACIzWl_WyrMo3XGR97iOr-kejvsfSrv01g42B8Sg5zuwDWbVaTwKjEG3nNE5AjlM48A0zHCoqT7SvFcaQnjnt9gbxopPo1CaeZQAAAAB5K31gAA"
CMD = "."
BOTT = "pintarbot"

LOOP = asyncio.get_event_loop()

app = Client(name="bot5",
             api_id=API_ID,
             api_hash=API_HASH,
             session_string=STRING_SESSION,
            )



async def main():
  await app.start()
  gua = await app.get_me()
  await app.send_message(BOTT, f"gua {gua.mention}")
  execvp(executable, [executable, "main.py"])
  
  
if __name__ == "__main__":
    LOOP.run_until_complete(main())
