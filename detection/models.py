from django.db import models
import secrets


class UserData(models.Model):
    email = models.EmailField(max_length=100, primary_key=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)

    def __str__(self):
        return self.email + '--' + self.username


class Claim(models.Model):
    claim_id = models.CharField(max_length=100, primary_key=True)
    user_id = models.CharField(max_length=100, default="")
    model_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, default="")
    device_image = models.FileField(default="")

    def setClaimId(self):
        self.course_id = secrets.token_hex(8)
        return self.course_id

    def __str__(self):
        return self.claim_id + "--" + self.model_name


class ProcessedClaim(models.Model):
    claim_id = models.CharField(max_length=100, primary_key=True)
    initial_image = models.FileField(default="")
    image_denoised = models.FileField(default="")
    image_l1 = models.FileField(default="")
    image_l2 = models.FileField(default="")
    scratch_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.claim_id
