from tkinter import CASCADE
from django.db import models
from user_auth.models import User
import signals
from django.utils.translation import gettext_lazy as _

class Connection(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE, related_name='req_sender')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE, related_name='req_receiver')
    status=models.CharField(max_length=200,default='pending')


    # class Meta:
    #     verbose_name = _(u'connection request')
    #     verbose_name_plural = _(u'conndection requests')
    #     unique_together = (('receiver', 'sender'),)


    def __str__(self):
        return f"{self.id}--{self.sender}--{self.receiver}"

    # def get_connected(self):
    #     return Connection.objects.filter(status='accept') 


#     def accept(self):
#         Connected.objects.befriend(self.from_user, self.to_user)
#         self.accepted = True
#         self.save()
#         signals.friendship_accepted.send(sender=self)





# class ConnectionManager(models.Manager):
#     def friends_of(self, user, shuffle=False):
#         qs = User.objects.filter(friendship__friends__user=user)
#         if shuffle:
#             qs = qs.order_by('?')
#         return qs

#     def are_connections(self, user1, user2):
#         return bool(Connection.objects.get(user=user1).friends.filter(
#                                                           user=user2).exists())

#     def beconnected(self, user1, user2):
#         Connection.objects.get(user=user1).connections.add(
#                                            Connected.objects.get(user=user2))
#         # Now that user1 accepted user2's friend request we should delete any
#         # request by user1 to user2 so that we don't have ambiguous data
#         Connection.objects.filter(from_user=user1,
#                                          to_user=user2).delete()

#     def unconnect(self, user1, user2):
#         # Break friendship link between users
#         Connection.objects.get(user=user1).connections.remove(
#                                            Connected.objects.get(user=user2))
#         # Delete FriendshipRequest's as well
#         Connection.objects.filter(from_user=user1,
#                                          to_user=user2).delete()
#         Connection.objects.filter(from_user=user2,
#                                          to_user=user1).delete()




 
# class Connected(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='connection')
#     connections = models.ManyToManyField('self', symmetrical=True)

#     objects = ConnectionManager()

#     class Meta:
#         verbose_name = _(u'connection')
#         verbose_name_plural = _(u'connections')


    


