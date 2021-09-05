from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime
from dotenv import load_dotenv

load_dotenv()


today = datetime.date.today()
tommorrow = today + datetime.timedelta(days=1)
six_month_from_today = today + datetime.timedelta(days=6*30)

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
data_manager.get_sheet_data()

for data_row in data_manager.sheet_data:
    flight_search = FlightSearch()

    # update iata code
    if data_row["iataCode"] == "":
        data_row["iataCode"] = flight_search.get_iata_code(
            city=data_row["city"])
        new_data = {
            "city": data_row["city"],
            "iataCode": data_row["iataCode"],
            "lowestPrice": data_row["lowestPrice"],
        }
        data_manager.update_row(id=data_row["id"], data=new_data)

    flight_data = flight_search.get_flight_data(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=data_row["iataCode"],
        from_time=tommorrow,
        to_time=six_month_from_today
    )

    # send sms
    if flight_data.price < data_row["lowestPrice"]:
        notification_manager = NotificationManager()
        notification_manager.send_sms(flight_data)

# pprint(data_manager.sheet_data)
