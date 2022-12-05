from rest_framework import permissions

class UpdateOwnBankAccount(permissions.BasePermission):
    """Allow user to allow their own bank account"""
    def has_object_permission(self, request, view, obj):
        """Check the user is tring to update their own status. The user is the only
        one who can see his bank account"""
        return obj.user_profile.id == request.user.id