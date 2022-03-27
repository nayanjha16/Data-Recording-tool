from django.db import models
from django.contrib.auth.models import User


class users(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    ]
    LANG_CHOICES = [
        ('Hindi', 'Hindi'),
        ('Bengali', 'Bengali'),
        ('Marathi', 'Marathi'),
        ('Telugu', 'Telugu'),
        ('Tamil', 'Tamil'),
        ('Gujarati', 'Gujarati'),
        ('Urdu', 'Urdu'),
        ('Bhojpuri', 'Bhojpuri'),
        ('Kannada', 'Kannada'),
        ('Malayalam', 'Malayalam'),
        ('Odia', 'Odia'),
        ('Punjabi', 'Punjabi'),
        ('Rajasthani', 'Rajasthani'),
        ('Chhattisgarhi', 'Chhattisgarhi'),
        ('Assamese', 'Assamese'),
        ('Maithili', 'Maithili'),
        ('Magadhi/Magahi', 'Magadhi'),
        ('Haryanvi', 'Haryanvi'),
        ('Khortha/Khotta', 'Khortha'),
        ('Marwari', 'Marwari'),
        ('Santali', 'Santali'),
        ('Kashmiri', 'Kashmiri'),
        ('Bundeli/Bundel khandi', 'Bundeli'),
        ('Malvi', 'Malvi'),
        ('Sadan/Sadri', 'Sadan'),
        ('Mewari', 'Mewari'),
        ('Awadhi', 'Awadhi'),
        ('Wagdi', 'Wagdi'),
        ('Lamani/Lambadi', 'Lamani'),
        ('Pahari[c]', 'Pahari'),
        ('Bhili/Bhilodi', 'Bhili'),
        ('Hara/Harauti', 'Hara'),
        ('Nepali', 'Nepali'),
        ('Gondi', 'Gondi'),
        ('Bagheli/Baghel Khandi', 'Bagheli'),
        ('Sambalpuri', 'Sambalpuri'),
        ('Dogri', 'Dogri'),
        ('Garhwali', 'Garhwali'),
        ('Nimadi', 'Nimadi'),
        ('Surjapuri', 'Surjapuri'),
        ('Konkani', 'Konkani'),
        ('Kumaoni', 'Kumaoni'),
        ('Kurukh/Oraon', 'Kurukh'),
        ('Tulu', 'Tulu'),
        ('Manipuri', 'Manipuri'),
        ('Surgujia', 'Surgujia'),
        ('Sindhi', 'Sindhi'),
        ('Bagri', 'Bagri'),
        ('Ahirani', 'Ahirani'),
        ('Banjari', 'Banjari'),
        ('Brajbhasha', 'Brajbhasha'),
        ('Dhundhari', 'Dhundhari'),
        ('Bodo/Boro', 'Bodo'),
        ('Ho', 'Ho'),
        ('Gojri/Gujjari/Gujar', 'Gojri'),
        ('Mundari', 'Mundari'),
        ('Garo', 'Garo'),
        ('Kangri', 'Kangri'),
        ('Khasi', 'Khasi'),
        ('Kachchhi', 'Kachchhi')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10)
    contact = models.CharField(max_length=10)
    lang_fluent_in = models.CharField(# choices=LANG_CHOICES,
                                      max_length=50)
    disability = models.CharField(max_length=150)

    def __str__(self):
        return self.f_name + " " + self.l_name
