from databases import Database

from app.settings import settings

database = Database(str(settings.db_url))
