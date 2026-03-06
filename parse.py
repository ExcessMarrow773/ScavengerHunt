from Server.db import dbHandler

from dateutil import parser

import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ScavengerHunt.settings")
django.setup()

from django.utils import timezone

from app.models import request
from django.contrib.auth import get_user_model

User = get_user_model()

db = dbHandler(name='./Server/db.sqlite3')

requests = db.get_requests()

# print(requests)
for i in requests:
	print(i['device'])
	try:
		strtime = i['timestamp']
		timestamp = parser.parse(strtime)
		print(strtime)
		print(timestamp)
		print(timezone.make_aware(timestamp, timezone.get_default_timezone()))
		thing = request.objects.create(
			device=i["device"],
			message=i['message'],
			created_on=timezone.make_aware(timestamp, timezone.get_default_timezone())
		)

	except KeyError as e:
		print('No timestamp')
		thing = request.objects.create(
			device=i["device"],
			message=i['message']
		)
	print(thing)
	thing.save()

