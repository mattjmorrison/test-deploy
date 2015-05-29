from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print 'STATIC_URL = {}'.format(settings.STATIC_URL)
        print 'AWS_ACCESS_KEY_ID = {}'.format(settings.AWS_ACCESS_KEY_ID)
        print 'AWS_SECRET_ACCESS_KEY = {}'.format(settings.AWS_SECRET_ACCESS_KEY)
        print 'AWS_STORAGE_BUCKET_NAME = {}'.format(settings.AWS_STORAGE_BUCKET_NAME)
