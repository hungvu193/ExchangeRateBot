from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime as dt

import requests

END_POINT = "https://api.exchangeratesapi.io/"


def _create_api_path(curreny: Any, time: Any) -> Text:
    timePath = ""
    currencyPath = ""
    if time is None:
        timePath = "latest"
    else:
        timePath = time

    if curreny is None:
        currencyPath = "?base=EUR"
    elif len(curreny) == 1:
        currencyPath = "?base={}".format(curreny[0])
    elif len(curreny) == 2:
        currencyPath = "?symbols={},{}".format(curreny[0], curreny[1])
    fullPath = END_POINT + timePath + currencyPath
    print(fullPath)
    return fullPath


# return time with format YYYY-mm-dd
def _create_api_time(time: Text) -> Text:
    time_object = dt.strptime(time, "%Y-%m-%dT%H:%M:%S.%f%z")
    return time_object.strftime("%Y-%m-%d")


class ActionSearchExchange(Action):
    def name(self) -> Text:
        return "action_search_exchange"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        path = ""
        extractTime = ""
        # search for exachange and response here
        listCurrency = tracker.get_slot('currency')
        times = tracker.get_slot('time')
        print(listCurrency)
        print(times)
        dispatcher.utter_message(
            text="Đang tìm kiếm thông tin, vui lòng đợi trong giây lát")
        if listCurrency is None:
            print("None")

        if times is None:
            extractTime = None
        elif "from" in times or "to" in times:
            extractTime = _create_api_time(times['from'])
        else:
            extractTime = _create_api_time(times)
        path = _create_api_path(listCurrency, extractTime)
        results = requests.get(path).json()
        if extractTime is None:
            dispatcher.utter_message(
                text="Tỷ giá ngoại tệ hôm nay: {}".format(results))
        else:
            dispatcher.utter_message(text="Tỷ giá ngoại tệ ngày {}: {}".format(
                extractTime, results))

        return []


class ActionSubmitLockCard(Action):
    def name(self) -> Text:
        return "action_submit_lock_card"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Đã xong")

        return []