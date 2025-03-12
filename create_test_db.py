#!/usr/bin/env python3

from dotenv import load_dotenv

# Load environment variables from '.env' file.
load_dotenv()

from lbrc_flask.database import db
from lbrc_flask.security import init_roles, init_users
from alembic.config import Config
from alembic import command
from faker import Faker
from dashboard.model import *
from lbrc_flask.pytest.faker import LbrcFlaskFakerProvider
from tests.faker import AcademicProvider, LookupProvider, ProjectProvider
from dashboard import create_app


fake = Faker("en_GB")
fake.add_provider(LbrcFlaskFakerProvider)
fake.add_provider(LookupProvider)
fake.add_provider(AcademicProvider)
fake.add_provider(ProjectProvider)

application = create_app()
application.app_context().push()
db.create_all()
init_roles([])
init_users()

alembic_cfg = Config("alembic.ini")
command.stamp(alembic_cfg, "head")

fake.create_standard_lookups()
db.session.commit()

for _ in range(20):
    fake.project().get_in_db()

db.session.close()
