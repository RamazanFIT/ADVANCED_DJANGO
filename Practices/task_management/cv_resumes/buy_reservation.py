import asyncio
import aiohttp
import random

BASE_URL_RESERVATION = "https://avatariya.test.nidgecloud.com/api/transactions/reservation/"
BASE_URL_SIMULATE_SCAN = "http://194.67.82.131/api/kaspi-pay/simulate-scan-qr/"
BASE_URL_SIMULATE_CONFIRM = "http://194.67.82.131/api/kaspi-pay/simulate-confirm-payment/"

HEADERS_RESERVATION = {
    "Authorization": "Token 299d3e320834b7261dc80616a52224506bcf56c3",
    "Content-Type": "application/json"
}

HEADERS_SIMULATE = {
    "Authorization": "Token 48cfbcd124536f1f27f2fc438beae23483ace8e2",
    "Content-Type": "application/json"
}

async def make_purchase(session, index):
    try:
        # Шаг 1: Резервация товара
        reservation_data = {
            "provider_type": "KASPI",
            "card_id": None,
            "reservation_data": {
                "park": 15,
                "room": None,
                "style": 3,
                "kid": 5,
                "reservation_products": [
                {
                    "product": 348,
                    "amount": 1,
                    "price": 35000.0,
                    "child_products": [
                    {
                        "product": 391,
                        "additional_service": 1
                    }
                    ]
                }
                ],
                "amount_kids": 1,
                "amount_adults": 0,
                "reservation_date": "2025-02-05",
                "start_time": "16:00",
                "end_time": "18:59"
            }
        }


        async with session.post(BASE_URL_RESERVATION, headers=HEADERS_RESERVATION, json=reservation_data) as resp:
            response_data = await resp.json()
            qr_payment_id = response_data.get("payment_id")
            if not qr_payment_id:
                print(f"[{index}] Ошибка резервации: {response_data}")
                return
            print(f"[{index}] Резервирование успешно: QR ID {qr_payment_id}")

        # Шаг 2: Симуляция сканирования QR-кода
        scan_payload = {"qr_payment_id": str(qr_payment_id)}
        async with session.post(BASE_URL_SIMULATE_SCAN, headers=HEADERS_SIMULATE, json=scan_payload) as resp:
            response_data = await resp.json()
            print(f"[{index}] QR сканирован: {response_data}")

        # Шаг 3: Симуляция подтверждения платежа
        confirm_payload = {"qr_payment_id": str(qr_payment_id)}
        async with session.post(BASE_URL_SIMULATE_CONFIRM, headers=HEADERS_SIMULATE, json=confirm_payload) as resp:
            response_data = await resp.json()
            print(f"[{index}] Платеж подтвержден: {response_data}")
    
    except Exception as e:
        print(f"[{index}] Ошибка: {e}")

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [make_purchase(session, i) for i in range(1, 1001)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())


