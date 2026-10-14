import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
import httpx

# Твої дані з сайту DuckDNS
# DUCKDNS_DOMAIN = "testthisdnsm"  # Наприклад: "myschoolpranks" (без .duckdns.org)
# DUCKDNS_TOKEN = "de989104-8955-4533-83ce-8c554128c5c4"

# async def update_duckdns():
#     """Функція для оновлення IP в DuckDNS"""
#     url = f"https://www.duckdns.org/update?domains={DUCKDNS_DOMAIN}&token={DUCKDNS_TOKEN}"
#     async with httpx.AsyncClient() as client:
#         try:
#             response = await client.get(url)
#             print(f"[DuckDNS] Статус оновлення: {response.text}")
#         except Exception as e:
#             print(f"[DuckDNS] Помилка мережі: {e}")


# async def periodic_duckdns_update():
#     """Фоновий цикл оновлення IP кожні 5 хвилин"""
#     while True:
#         await update_duckdns()
#         await asyncio.sleep(60)  # 300 секунд = 5 хвилин

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     """Керування життєвим циклом додатку (старт і зупинка)"""
#     # Запускаємо фонову задачу при старті сервера
#     task = asyncio.create_task(periodic_duckdns_update())
#     yield
#     # Тут можна додати зупинку задачі, якщо знадобиться

app = FastAPI()

@app.get("/")
def home():
    return {
        "status": "active",
        "address": f"http://duckdns.org",
    }

# Ендпоінт, до якого будуть звертатися комп'ютери за командою
@app.get("/get-command")
def get_command():
    # Тут ти можеш повертати потрібну команду ("prank", "none" тощо)
    return {"command": "prank"}