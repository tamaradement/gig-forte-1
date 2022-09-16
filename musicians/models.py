from django.db import models
from accounts.models import CustomUser
from django.conf import settings


class CallList(models.Model):
    bandleader = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="bandleader")
    musicians = models.ManyToManyField(CustomUser, blank=True, related_name="musicians")

    def __str__(self):
        return self.bandleader.username
    
    def add_musician(self, account):
        # Add musician to call list.
        if not account in self.musicians.all():
            self.musicians.add(account)
    
    def remove_musician(self, account):
        # Remove musician from call list.
        if account in self.musicians.all():
            self.musicians.remove(account)
    
    def terminate_relationship(self, removee):
        # Initiate terminating the playing relationship.
        remover_call_list = self # Call list of person terminating the relationship.

        # Remove removee from remover's call list.
        remover_call_list.remove_musician(removee)
    
    def is_associate(self, musician):
        # Is there a professional relationship?
        if musician in self.musicians.all():
            return True
        
        return False

