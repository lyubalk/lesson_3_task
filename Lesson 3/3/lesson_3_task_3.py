from address import Address
from mailing import Mailing

address_from = Address("101000", "Москва", "ул.Донская", "д.8", "кв.1")
address_to = Address("187015", "Санкт-Петербург", "ул.Белы Куна", "д.10", "кв.2")
mailing = Mailing(address_from, address_to, 234, "V668867798CN")
print(f"Отправление: Track: {mailing.track},",
      f"\nИз: {mailing.from_address.index}, {mailing.from_address.city},"
      f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.flat}",
      f"\nВ: {mailing.to_address.index}, {mailing.to_address.city},"
      f"{mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.flat}"
      f"\nСтоимость: {mailing.cost} рублей.")

