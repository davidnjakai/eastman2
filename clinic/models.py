# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Patients(models.Model):
    patid = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=45)
    firstname = models.CharField(max_length=45)
    middlename = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    mobilenumber = models.CharField(max_length=45, blank=True, null=True)
    mobilenumber2 = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    guarantor = models.IntegerField()
    dateofbirth = models.DateField(blank=True, null=True)
    filenumber = models.IntegerField()
    photolocation = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10)
    position = models.CharField(max_length=10, blank=True, null=True)
    dueamount = models.IntegerField()
    insuranceamount = models.IntegerField()
    balancedue = models.IntegerField()
    occupation = models.CharField(max_length=45, blank=True, null=True)
    employer_school = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.lastname
    class Meta:
        managed = False
        db_table = 'patients'
