from O365 import Account, MSGraphProtocol
from O365.calendar import Calendar
from jwt_encode import create_jwt_assertion


thumbprint = "2a69137b1b3125cd4b8b38d6bed136a4314a4e62"
private_key = open("./keys/server.key").read()
open_key = open("./keys/openserver.pem").read()
client_id = "89f740d2-14c1-409f-b6c8-0e68d4d9acff"
tenant_id = "f8cdef31-a31e-4b4a-93e4-5f571e91255a"

encoded_payload = create_jwt_assertion(private_key, tenant_id, thumbprint, client_id)

credentials = (client_id, encoded_payload)

protocol = MSGraphProtocol()
# protocol = MSGraphProtocol(defualt_resource='<sharedcalendar@domain.com>')
# scopes = ["user.read"]
scopes = ["https://graph.microsoft.com/Calendars.Read"]
# scopes = ["calendar"]
# scopes = protocol.get_scopes_for("basic")
# print(scopes_graph)
account = Account(
    credentials,
    # protocol=protocol,
    auth_flow_type="certificate",
    tenant_id=tenant_id,
    # scopes=scopes,
)

if account.authenticate():
    print("Authenticated!")
else:
    exit(1)

schedule = account.schedule(resource="inovikow_test@outlook.com")
calendar = schedule.get_default_calendar()
if not isinstance(calendar, Calendar):
    raise RuntimeError()
events = calendar.get_events(include_recurring=False)
# events = calendar.get_events(query=q, include_recurring=True)

for event in events:
    print(event)
