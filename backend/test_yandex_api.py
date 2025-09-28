import requests
from datetime import datetime, timedelta

API_KEY = "45482873-c57b-4ef3-b0b2-dc6b4692f32f"
BASE_URL = "https://api.rasp.yandex.net/v3.0/search/"

# коды станций
FROM_CODE = "s9602499"   # Санкт-Петербург (Ладожский вокзал)
TO_CODE = "s9604211"     # Череповец-1


def get_week_dates(start=None, days=7):
    """Возвращает список дат на неделю вперёд в формате YYYY-MM-DD"""
    start = start or datetime.now().date()
    return [(start + timedelta(days=i)).isoformat() for i in range(days)]


def get_schedule_for_date(date):
    """Запрос расписания из СПб в Череповец на определённую дату"""
    params = {
        "apikey": API_KEY,
        "from": FROM_CODE,
        "to": TO_CODE,
        "lang": "ru_RU",
        "date": date,
        "transport_types": "train",
    }
    try:
        r = requests.get(BASE_URL, params=params, timeout=15)
        data = r.json()
        if "error" in data:
            return []
        return data.get("segments", [])
    except Exception as e:
        print(f"❌ Ошибка при запросе на {date}: {e}")
        return []


def print_schedule():
    print(f"📅 Расписание поездов Санкт-Петербург → Череповец (на 7 дней)\n")
    for date in get_week_dates():
        segments = get_schedule_for_date(date)
        print(f"== {date} ==")
        if not segments:
            print("   ❌ Нет поездов\n")
            continue
        for seg in segments:
            dep = seg["departure"].replace("T", " ")[:-3]
            arr = seg["arrival"].replace("T", " ")[:-3]
            train = seg["thread"].get("number", "—")
            title = seg["thread"].get("title", "")
            duration = seg.get("duration", 0) // 3600  # часы
            print(f"   🚆 {train} {title}")
            print(f"      Отправление: {dep}")
            print(f"      Прибытие:   {arr}")
            print(f"      В пути:     {duration} ч\n")


if __name__ == "__main__":
    print_schedule()
