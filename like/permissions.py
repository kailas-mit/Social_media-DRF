from rest_framework import permissions

class hasSelfVotedOrReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.liked_by == request.user or obj.diss_liked_by== request.user
   