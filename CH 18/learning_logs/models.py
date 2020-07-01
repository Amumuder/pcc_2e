from django.db import models

# Create your models here.


class Topic(models.Model):  # Create a class, which inherits frm Model
    """A topic the user learning about"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # is a ForeignKey instance
    # on_delete=models.CASCADE > when a topic is deleted, all entries associated with that topic should be deleted as well
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    # 18-2 Short Entries
    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        else:
            return f'{self.text}'
