"Cabify HTML Parser"


class CabifyParser:
    def __init__(self, html_body):
        self.html_body = html_body

    def _get_mail_values(self):
        trs = self.html_body.find_all("tr")

        mail_values = []
        for tr in trs:
            tds = tr.find_all("td")
            for td in tds:
                trs2 = td.find_all("tr")
                for tr2 in trs2:
                    text = tr2.text.strip()
                    mail_values.append(text)

        return mail_values

    def get_base_price(self):
        mail_values = self._get_mail_values()
        for value in mail_values:
            if "base" in value:
                base_price = value.split("$")[1].replace(".", "").replace(",", ".")
                return float(base_price)

    def get_processing_fee(self):
        mail_values = self._get_mail_values()
        for value in mail_values:
            if "Procesamiento" in value:
                processing_fee = value.split("$")[1].replace(".", "").replace(",", ".")
                return float(processing_fee)

    def get_high_demand_fee(self):
        mail_values = self._get_mail_values()
        for value in mail_values:
            if "demanda" in value:
                high_demand_fee = value.split("$")[1].replace(".", "").replace(",", ".")
                return float(high_demand_fee)

    def get_total_price(self):
        mail_values = self._get_mail_values()
        for value in mail_values:
            if "Total" in value:
                total_price = value.split("$")[1].replace(".", "").replace(",", ".")
                return float(total_price)

    def get_trip_duration_in_seconds(self):
        mail_values = self._get_mail_values()
        for value in mail_values:
            if "Duración" in value:
                trip_duration = value.split("\n\n\n")[1]
                minutes = int(trip_duration.split(" min")[0])
                # seconds = int(trip_duration.split(" min ")[1].split(" s")[0])
                seconds = trip_duration.split(" min ")
                if len(seconds) == 1:
                    seconds = 0
                else:
                    seconds = int(seconds[1].split(" s")[0])
                return minutes * 60 + seconds
