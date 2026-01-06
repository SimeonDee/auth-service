import enum


class UserRoles(str, enum.Enum):
    """Defines the allowed values for user roles."""

    PLATFORM_ADMIN = "platform_admin"
    SCHOOL_ADMIN = "school_admin"
    TEACHER = "teacher"
    ACCOUNTANT = "accountant"
    PARENT = "parent"
    STUDENT = "student"
    GUEST = "guest"
    SUPER_USER = "super_user"
