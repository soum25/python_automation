import pytz
from datetime import date, datetime
import time
my_tz = {}


print("bonjour", end="")
while True:
    abidjan_tz = pytz.timezone("Africa/Abidjan")
    paris_tz = pytz.timezone("Europe/Paris")

    time_abidjan = datetime.now(abidjan_tz)
    time_paris = datetime.now(paris_tz)

    hour_abidjan = time_abidjan.strftime("%H:%M:%S")
    hour_paris = time_paris.strftime("%H:%M:%S")

    if __name__ == '__main__':
        print(f"Heure Abidjan = {hour_abidjan} <==> Heure Paris = {hour_paris}", end="", flush=True)
        time.sleep(1)
        print("\r", end="", flush=True)
