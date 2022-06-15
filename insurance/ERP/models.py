from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Company_info(models.Model):
    id = models.AutoField(primary_key=True)
    C_name = models.CharField(max_length=255, null=True, blank=True)
    C_address = models.CharField(max_length=255, null=True, blank=True)
    C_Phone = models.CharField(max_length=255, null=True, blank=True)
    C_Fax = models.CharField(max_length=255, null=True, blank=True)
    C_Email = models.EmailField(max_length=255, null=True, blank=True)
    C_Web = models.CharField(max_length=255, null=True, blank=True)
    Create_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Create_date = models.DateTimeField(auto_now_add=True, blank=True)
    C_image = models.ImageField(upload_to='c_logo', null=True, blank=True)
    Page_lod_img = models.ImageField(upload_to='page_load_img', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.C_name


class BranchInformation(models.Model):
    id = models.AutoField(primary_key=True)
    Create_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Create_date = models.DateTimeField(auto_now_add=True, blank=True)
    B_name=models.CharField(max_length=255,null=True,blank=True)
    B_short_name=models.CharField(max_length=50,null=True,blank=True)
    B_address=models.CharField(max_length=255,null=True,blank=True)
    B_phone=models.CharField(max_length=50,null=True,blank=True)
    B_fax=models.CharField(max_length=50,null=True,blank=True)
    B_email=models.EmailField(max_length=100,null=True,blank=True)
    objects=models.Manager()




