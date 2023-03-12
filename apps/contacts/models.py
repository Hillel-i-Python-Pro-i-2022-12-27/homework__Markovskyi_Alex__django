from django.db import models


class Contact(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )

    username = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    ssn = models.CharField(max_length=20)
    company = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    mail = models.EmailField(max_length=50)
    telephone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_auto_generated = models.BooleanField(default=False)

    def __str__(self) -> str:
        return (
            f"{self.pk} - {self.username} - "
            f"{self.name} - {self.birthdate} - "
            f"{self.sex} - {self.ssn} - "
            f"{self.company} - {self.job} - "
            f"{self.mail} - {self.telephone} - "
            f"{self.address}"
        )

    __repr__ = __str__
