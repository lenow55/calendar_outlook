from O365 import Account, MSGraphProtocol, FileSystemTokenBackend
from O365.calendar import Calendar
from jwt_encode import create_jwt_assertion
from client_conf import Settings

config = Settings()

credentials = (config.client_id, config.secret.get_secret_value())

protocol = MSGraphProtocol()
token_backend = FileSystemTokenBackend(
    token_path="tokens", token_filename="my_token.txt"
)
scopes = ["calendar"]
account = Account(
    credentials,
    protocol=protocol,
    token_backend=token_backend,
)

if account.is_authenticated:
    print("Authenticated!")
else:
    account.authenticate(scopes=scopes)
if not account.is_authenticated:
    raise Exception("Can't authenticate!")

schedule = account.schedule(resource="inovikow_test@outlook.com")
calendar = schedule.get_default_calendar()
if not isinstance(calendar, Calendar):
    raise RuntimeError()
events = calendar.get_events(include_recurring=False)

for event in events:
    print(event.to_api_data())
    print(event.start)
    print(event.end)
