# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FooDB(models.Model):
    food_id = models.IntegerField(db_column='Id', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    food = models.TextField(db_column='Food', blank=True, null=True)  # Field name made lowercase.
    food_type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    calories = models.IntegerField(db_column='Calories', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Sheet1'

    def __str__(self):
    	return self.food


