from django.db import models


class Kilometers(models.Model):
    estimated_diameter_min = models.FloatField
    estimated_diameter_max = models.FloatField


class Meters(models.Model):
    estimated_diameter_min = models.FloatField
    estimated_diameter_max = models.FloatField


class Miles(models.Model):
    estimated_diameter_min = models.FloatField
    estimated_diameter_max = models.FloatField


class Feet(models.Model):
    estimated_diameter_min = models.FloatField
    estimated_diameter_max = models.FloatField


class EstimatedDiameter(models.Model):
    kilometers = Kilometers
    meter = Meters
    miles = Miles
    feet = Feet


class RelativeVelocity(models.Model):
    kilometers_per_second = models.CharField(max_length=20)
    kilometers_per_hour = models.CharField(max_length=20)
    miles_per_hour = models.CharField(max_length=20)


class MissDistance(models.Model):
    astronomical = models.CharField(max_length=20)
    lunar = models.CharField(max_length=20)
    kilometers = models.CharField(max_length=20)
    miles = models.CharField(max_length=20)


class CloseApproachData(models.Model):
    close_approach_date = models.CharField(max_length=20)
    close_approach_date_full = models.CharField(max_length=20)
    epoch_date_close_approach = models.IntegerField
    relative_velocity = RelativeVelocity
    miss_distance = MissDistance
    orbiting_body = models.CharField(max_length=20)


class OrbitalClass(models.Model):
    orbit_class_type = [
        'IEO', 'ATE', 'APO', 'AMO', 'MCA',
        'IMB', 'MBA', 'OMB', 'TJN', 'CEN', 'TNO',
        'PAA', 'HYA', 'HYP', 'PAR', 'COM', 'JFC',
        'HTC', 'ETC', 'CTC', 'JFc'
    ]
    orbit_class_description = models.CharField(max_length=20)
    orbit_class_range = models.CharField(max_length=20)


class OrbitalData(models.Model):
    orbit_id = models.CharField(max_length=20)
    orbit_determination_date = models.CharField(max_length=20)
    first_observation_date = models.CharField(max_length=20)
    last_observation_date = models.CharField(max_length=20)
    data_arc_in_days = models.IntegerField
    observations_used = models.IntegerField
    orbit_uncertainty = models.CharField(max_length=20)
    minimum_orbit_intersection = models.CharField(max_length=20)
    jupiter_tisserand_invariant = models.CharField(max_length=20)
    epoch_osculation = models.CharField(max_length=20)
    eccentricity = models.CharField(max_length=20)
    semi_major_axis = models.CharField(max_length=20)
    inclination = models.CharField(max_length=20)
    ascending_node_longitude = models.CharField(max_length=20)
    orbital_period = models.CharField(max_length=20)
    perihelion_distance = models.CharField(max_length=20)
    perihelion_argument = models.CharField(max_length=20)
    aphelion_distance = models.CharField(max_length=20)
    perihelion_time = models.CharField(max_length=20)
    mean_anomaly = models.CharField(max_length=20)
    mean_motion = models.CharField(max_length=20)
    equinox = models.CharField(max_length=20)
    orbit_class = OrbitalClass


class NearObject(models.Model):
    link = models.CharField(max_length=500)
    ast_id = models.CharField(max_length=10)
    neo_reference_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    nasa_jpl_url = models.CharField(max_length=100)
    absolute_magnitude_h = models.IntegerField()
    estimated_diameter = EstimatedDiameter
    is_potentially_hazardous_asteroid = models.BooleanField
    close_approach_data = CloseApproachData
    orbital_data = OrbitalData
    is_sentry_object = models.BooleanField
    sentry_data = models.CharField(max_length=500)


class Base(models.Model):
    links = models.CharField(max_length=500)
    element_count = models.IntegerField()
    near_earth_objets = NearObject