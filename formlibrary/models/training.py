#!/usr/bin/python3
# -*- coding: utf-8 -*-

from django.db import models
from .service import Service
from workflow.models import Contact


class Training(Service):
    """
    Suject to future changes: https://github.com/hikaya-io/activity/issues/421
    ? Should we edit/update the already existing TrainingAttendance, or implement from scratch?
    """
    trainer = models.ForeignKey(
        Contact, null=True, blank=True, on_delete=models.SET_NULL)
    duration = models.IntegerField(help_text="Number of days? Sessions?")

    @property
    def total_individual_supported(self):
        # TODO Check all individuals, and households and their individuals
        return 0

    # @property
    # def attendance(self):
    #     """
    #     ? Return list of Individuals and their attendance as a percentage relative to `training_duration`.
    #     TODO This is related to cases, which keeps track of attendance
    #     """
    #     return {}