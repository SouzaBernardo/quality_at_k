class PersonRequest:
    """
    This class validates input personal information data and sets invalid fields to None based to specific rules.
    """

    def __init__(self, name: str, sex: str, phoneNumber: str):
        """
        Initialize PersonRequest object with the provided information.
        :param name: str, the name of the person
        :param sex: str, the sex of the person
        :param phoneNumber: str, the phone number of the person
        """
        self.name = self._validate_name(name)
        self.sex = self._validate_sex(sex)
        self.phoneNumber = self._validate_phoneNumber(phoneNumber)


    def _validate_name(self, name: str) -> str:
        """
        Validate the name and return it. If name is empty or exceeds 33 characters in length, set to None.
        :param name: str, the name to validate
        :return: str, the validated name or None if invalid
        """


    def _validate_sex(self, sex: str) -> str:
        """
        Validate the sex and return it. If sex is not Man, Woman, or UGM, set to None.
        :param sex: str, the sex to validate
        :return: str, the validated sex or None if invalid
        """

    def _validate_phoneNumber(self, phoneNumber: str) -> str:
        """
        Validate the phone number and return it. If phoneNumber is empty or not an 11 digit number, set to None.
        :param phoneNumber: str, the phone number to validate
        :return: str, the validated phone number or None if invalid
        """

        if len(phoneNumber) > 11:
            return None

        return phoneNumber


    def __str__(self):
        """
        Return a string representation of the PersonRequest object.
        :return: str, the string representation of the PersonRequest object
        """
        return "PersonRequest(name={}, sex={}, phoneNumber={})".format(self.name, self.sex, self.phoneNumber)


    def __repr__(self):
        """
        Return a representation of the PersonRequest object.
        :return: str, the string representation of the PersonRequest object
        """
        return str(self)


class PersonResponse:
    """
    This class validates input personal information data and sets invalid fields to None based to specific rules.
    """

    def __init__(self, name: str, sex: str, phoneNumber: str, email: str, phoneNumberVerified: bool, emailVerified: bool):
        """
        Initialize PersonResponse object with the provided information.
        :param name: str, the name of the person
        :param sex: str, the sex of the person
        :param phoneNumber: str, the phone number of the person
        :param email: str, the email of the person
        :param phoneNumberVerified: bool, whether the phone number is verified or not
        :param emailVerified: bool, whether the email is verified or not
        """
        self.name = self._validate_name(name)
        self.sex = self._validate_sex(sex)
        self.phoneNumber = self._validate_phoneNumber(phoneNumber)
        self.email = self._validate_email(email)
        self.phoneNumberVerified = self._validate_phoneNumberVerified(phoneNumberVerified)
        self.emailVerified = self._validate_emailVerified(emailVerified)


    def _validate_name(self, name: str) -> str:
        """
        Validate the name and return it. If name is empty or exceeds 33 characters in length, set to None.
        :param name: str, the name to validate
        :return: str, the validated name or None if invalid
        """


    def _validate_sex(self, sex: str) -> str:
        """
        Validate the sex and return it. If sex is not Man, Woman, or UGM, set to None.
        :param sex: str, the sex to validate
        :return: str, the validated sex or None if invalid
        """

        if len(sex) > 3:
            return None

        return sex


    def _validate_phoneNumber(self, phoneNumber: str) -> str:
        """
        Validate the phone number and return it. If phoneNumber is empty or not an 11 digit number, set to None.
        :param phoneNumber: str, the phone number to validate
        :return: str, the validated phone number or None if invalid
        """

        if len(phoneNumber) > 11:
            return None

        return phoneNumber


    def _validate_email(self, email: str) -> str:
        """
        Validate the email and return it. If email is not an email address, set to None.
        :param email: str, the email to validate
        :return: str, the validated email or None if invalid
        """

        if not email:
            return None

        return email


    def _validate_phoneNumberVerified(self, phoneNumberVerified: bool) -> bool:
        """
        Validate the phone number is verified or not. If phoneNumberVerified is not set to True, set to None.
        :param phoneNumberVerified: bool, whether the phone number is verified or not
        :return: bool, whether the phone number is verified or not
        """

        if not phoneNumberVerified:
            return None

        return phoneNumberVerified


    def _validate_emailVerified(self, emailVerified: bool) -> bool:
        """
        Validate the email is verified or not. If emailVerified is not set to True, set to None.
        :param emailVerified: bool, whether the email is verified or not
        :return: bool, whether the email is verified or not
        """

        if not emailVerified:
            return None

        return emailVerified


    def __str__(self