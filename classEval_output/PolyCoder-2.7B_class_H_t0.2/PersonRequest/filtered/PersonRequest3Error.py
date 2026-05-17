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
        Return a string representation of the PersonRequest.
        :return: str, the string representation of the PersonRequest
        """
        return "PersonRequest(name={0}, sex={1}, phoneNumber={2})".format(self.name, self.sex, self.phoneNumber)


    def __repr__(self):
        """
        Return a representation of the PersonRequest.
        :return: str, the string representation of the PersonRequest
        """
        return "PersonRequest(name={0}, sex={1}, phoneNumber={2})".format(self.name, self.sex, self.phoneNumber)


    def __eq__(self, other):
        """
        Compare two PersonRequest objects.
        :param other: PersonRequest object to compare to
        :return: bool, True if both PersonRequest objects are equal, False otherwise
        """
        if not isinstance(other, PersonRequest):
            return False

        return self.name == other.name and self.sex == other.sex and self.phoneNumber == other.phoneNumber


    def __ne__(self, other):
        """
        Compare two PersonRequest objects.
        :param other: PersonRequest object to compare to
        :return: bool, True if both PersonRequest objects are not equal, False otherwise
        """
        return not self.__eq__(other)


    def __hash__(self):
        """
        Return a hash value for the PersonRequest.
        :return: int, a hash value for the PersonRequest
        """
        return hash(self.name) ^ hash(self.sex) ^ hash(self.phoneNumber)


    def __str__(self):
        """
        Return a string representation of the PersonRequest.
        :return: str, the string representation of the PersonRequest
        """
        return "PersonRequest(name={0}, sex={1}, phoneNumber={2})".format(self.name, self.sex, self.phoneNumber)


    def __repr__(self):
        """
        Return a representation of the PersonRequest.
        :return: str, the string representation of the PersonRequest
        """
        return "PersonRequest(name={0}, sex={1}, phoneNumber={2})".format(self.name, self.sex, self.phoneNumber)


    def __getstate__(self):
        """
        Return a representation of the PersonRequest.
        :return: dict, the dictionary representation of the PersonRequest
        """
        return {'name': self.name,'sex': self.sex, 'phoneNumber': self.phoneNumber}


    def __setstate__(self, state):
        """
        Set the PersonRequest state from a dictionary representation.
        :param state: dict, the dictionary representation of the PersonRequest
        """
        self.name = state['name']
        self.sex = state['sex']
        self.phoneNumber = state['phoneNumber']


    def __getnewargs__(self):
        """
        Return a new PersonRequest object with all attributes of the PersonRequest as defined by the parameters of the object.
        :return: PersonRequest, a new PersonRequest object with all attributes of the PersonRequest as defined by the parameters of the object
        """
        return PersonRequest(self.name, self.sex, self.phoneNumber)


    def __setnewargs__(self, newargs):
        """
        Set the PersonRequest state from a new PersonRequest object.
        :param newargs: PersonRequest, a new PersonRequest object with all attributes of the PersonRequest as defined by the parameters of the object
        """
        self.name = newargs.name
        self.sex = newargs.sex
        self.phoneNumber = newargs.phoneNumber


    def __deepcopy__(self, memo):
        """
        Deep copy the PersonRequest object.
        :param memo: PersonRequest, the PersonRequest object to deep copy
        :return: PersonRequest, a deep copy of the PersonRequest object
        """
        return PersonRequest(self.name, self.sex, self.phoneNumber)


    def __str__(self):
        """
        Return a string representation of the PersonRequest.
        :return: str, the string representation of the