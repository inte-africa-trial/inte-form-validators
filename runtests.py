#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_constants.constants import IGNORE
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname, join


app_name = 'inte_form_validators'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    BASE_DIR=base_dir,
    APP_NAME=app_name,
    SITE_ID=100,
    COUNTRY="uganda",
    ETC_DIR=os.path.join(base_dir, app_name, "tests", "etc"),
    EDC_BOOTSTRAP=3,
    EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
    EMAIL_CONTACTS={
        "data_request": "someone@example.com",
        "data_manager": "someone@example.com",
    },
    ADVERSE_EVENT_ADMIN_SITE="inte_ae_admin",
    ADVERSE_EVENT_APP_LABEL="inte_ae",
    EMAIL_ENABLED=True,
    HOLIDAY_FILE=join(base_dir, app_name, "tests", "holidays.csv"),
    SUBJECT_CONSENT_MODEL=f"inte_consent.subjectconsent",
    SUBJECT_VISIT_MODEL=f"inte_subject.subjectvisit",
    SUBJECT_REQUISITION_MODEL=f"inte_subject.subjectrequisition",
    LIVE_SYSTEM=False,
    EDC_NAVBAR_VERIFY_ON_LOAD=IGNORE,
    RANDOMIZATION_LIST_PATH=join(base_dir, app_name, "tests"),
    EDC_RANDOMIZATION_REGISTER_DEFAULT_RANDOMIZER=False,
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "django_celery_beat",
        "django_celery_results",
        "edc_auth.apps.AppConfig",
        "edc_action_item.apps.AppConfig",
        "edc_adverse_event.apps.AppConfig",
        "edc_appointment.apps.AppConfig",
        "edc_dashboard.apps.AppConfig",
        "edc_data_manager.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_prn.apps.AppConfig",
        "edc_randomization.apps.AppConfig",
        "edc_reference.apps.AppConfig",
        "edc_identifier.apps.AppConfig",
        "edc_export.apps.AppConfig",
        "edc_navbar.apps.AppConfig",
        "edc_facility.apps.AppConfig",
        "edc_locator.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_pharmacy.apps.AppConfig",
        "edc_protocol.apps.AppConfig",
        "edc_metadata.apps.AppConfig",
        "edc_metadata_rules.apps.AppConfig",
        "edc_model_admin.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_offstudy.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "edc_visit_tracking.apps.AppConfig",
        "inte_auth.apps.AppConfig",
        "inte_labs.apps.AppConfig",
        "inte_lists.apps.AppConfig",
        "inte_ae.apps.AppConfig",
        "inte_prn.apps.AppConfig",
        "inte_screening.apps.AppConfig",
        "inte_visit_schedule.apps.AppConfig",
        "inte_reference.apps.AppConfig",
        "inte_subject.apps.AppConfig",
        "inte_consent.apps.AppConfig",
        "inte_form_validators.apps.AppConfig",
    ],
    use_test_urls=True,
    add_dashboard_middleware=True,
    add_lab_dashboard_middleware=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split('=')[1] for t in sys.argv if t.startswith('--tag')]
    failures = DiscoverRunner(failfast=False, tags=tags).run_tests(
        [f'{app_name}.tests'])
    sys.exit(bool(failures))


if __name__ == "__main__":
    logging.basicConfig()
    main()
