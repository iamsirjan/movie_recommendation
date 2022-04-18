from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, name and password.
        """
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),

        )
        user.set_password(password)
        user.save()
        return user


def create_superuser(self, email,  password=None):
    """
    Creates and saves a superuser with the given email and password.
    """
    user = self.create_user(
        email,

        password=password,
    )

    user.is_superuser = True
    user.is_admin = True
    user.save()
    return user
