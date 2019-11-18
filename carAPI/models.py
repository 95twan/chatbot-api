from django.db import models


class Maker(models.Model):
    id = models.BigAutoField(primary_key=True)
    no = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'maker'


class Car(models.Model):
    id = models.BigAutoField(primary_key=True)
    maker = models.ForeignKey(Maker, models.DO_NOTHING)
    model_no = models.IntegerField()
    model = models.CharField(max_length=40)
    level_no = models.IntegerField()
    level = models.CharField(max_length=40)
    class_no = models.IntegerField()
    class_field = models.CharField(db_column='class', max_length=40, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    year = models.IntegerField()
    price = models.IntegerField()
    fuel = models.CharField(max_length=30, blank=True, null=True)
    grand_clearance = models.IntegerField()
    driving_system = models.CharField(max_length=3, blank=True, null=True)
    break_front = models.CharField(max_length=50, blank=True, null=True)
    break_rear = models.CharField(max_length=50, blank=True, null=True)
    weight = models.IntegerField()
    max_speed = models.IntegerField(blank=True, null=True)
    fuel_capacity = models.IntegerField()
    fuel_efficiency_highway = models.FloatField()
    fuel_efficiency_combined = models.FloatField()
    fuel_efficiency_city = models.FloatField()
    max_torque = models.CharField(max_length=15, blank=True, null=True)
    guarantee_basic = models.CharField(max_length=30, blank=True, null=True)
    guarantee_power = models.CharField(max_length=30, blank=True, null=True)
    transmission = models.CharField(max_length=30, blank=True, null=True)
    wheel_front = models.CharField(max_length=5, blank=True, null=True)
    wheel_rear = models.CharField(max_length=5, blank=True, null=True)
    engine_type = models.CharField(max_length=100, blank=True, null=True)
    tire_front = models.IntegerField(blank=True, null=True)
    tire_rear = models.IntegerField(blank=True, null=True)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    displacement = models.IntegerField()
    suspension_front = models.CharField(max_length=30, blank=True, null=True)
    suspension_rear = models.CharField(max_length=30, blank=True, null=True)
    seating_capacity = models.IntegerField()
    steering = models.CharField(max_length=40, blank=True, null=True)
    cylinder_number = models.IntegerField()
    max_output = models.CharField(max_length=12, blank=True, null=True)
    load_capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'car'


class Color(models.Model):
    id = models.BigAutoField(primary_key=True)
    color = models.CharField(max_length=30)
    rgb = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'color'


class CarColor(models.Model):
    id = models.BigAutoField(primary_key=True)
    car = models.ForeignKey(Car, models.DO_NOTHING)
    color = models.ForeignKey(Color, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'car_color'
