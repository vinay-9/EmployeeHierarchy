from models.dbconn import Session
from models.log import Log
import logConfig


class StoreLog:
    def __init__(self, *args):
        pass

    def log(self, object):
        session = Session()
        try:
            log = Log(
                userid=object.get("userid"),
                path=object.get("path"),
                method=object.get("method"),
                browser=object.get("browser"),
                browser_version=object.get("browser_version"),
                os=object.get("os"),
                ip_address=object.get("ip_address"),
                params=object.get("params"),
                body=object.get("body"),
                status=object.get("status"),
                duration=object.get("duration"),
            )

            session.add(log)
            session.commit()
        except Exception as e:
            logConfig.logError("Error while inserting the LogData to DB => " + str(e))
        finally:
            session.close()
