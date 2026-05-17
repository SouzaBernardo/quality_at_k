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


    def __str__(self) -> str:
        """
        Return a string representation of the PersonRequest object.
        :return: str, the string representation of the PersonRequest object
        """
        return "PersonRequest(name={}, sex={}, phoneNumber={})".format(self.name, self.sex, self.phoneNumber)


    def __repr__(self) -> str:
        """
        Return a representation of the PersonRequest object.
        :return: str, the string representation of the PersonRequest object
        """
        return self.__str__()


    def __eq__(self, other: object) -> bool:
        """
        Check equality of PersonRequest objects.
        :param other: object, the object to compare to
        :return: bool, whether the PersonRequest objects are equal
        """
        if not isinstance(other, PersonRequest):
            return False
        return self.name == other.name and self.sex == other.sex and self.phoneNumber == other.phoneNumber


    def __ne__(self, other: object) -> bool:
        """
        Check inequality of PersonRequest objects.
        :param other: object, the object to compare to
        :return: bool, whether the PersonRequest objects are not equal
        """
        return not self.__eq__(other)


    def __hash__(self) -> int:
        """
        Return a hash of the PersonRequest object.
        :return: int, the hash of the PersonRequest object
        """
        return hash(self.name) ^ hash(self.sex) ^ hash(self.phoneNumber)


    def __len__(self) -> int:
        """
        Return the length of the PersonRequest object.
        :return: int, the length of the PersonRequest object
        """
        return len(self.name) + len(self.sex) + len(self.phoneNumber)


    def __getitem__(self, index: int) -> str:
        """
        Return the PersonRequest object at the specified index.
        :param index: int, the index of the PersonRequest object
        :return: str, the PersonRequest object at the specified index
        """
        return self.name[index]


    def __setitem__(self, index: int, value: str) -> None:
        """
        Set the PersonRequest object at the specified index.
        :param index: int, the index of the PersonRequest object
        :param value: str, the PersonRequest object to set at the specified index
        """
        self.name[index] = value


    def __iter__(self) -> Iterator[str]:
        """
        Return an iterator over the PersonRequest object.
        :return: Iterator[str], an iterator over the PersonRequest object
        """
        return iter(self.name)


    def __contains__(self, value: str) -> bool:
        """
        Check whether the PersonRequest object contains the provided value.
        :param value: str, the PersonRequest object to check for
        :return: bool, whether the PersonRequest object contains the provided value
        """
        return value in self.name


    def __str__(self) -> str:
        """
        Return a string representation of the PersonRequest object.
        :return: str, the string representation of the PersonRequest object
        """
        return "PersonRequest(name={}, sex={}, phoneNumber={})".format(self.name, self.sex, self.phoneNumber)


    def __repr__(self) -> str:
        """
        Return a representation of the PersonRequest object.
        :return: str, the string representation of the PersonRequest object
        """
        return self.__str__()


    def __eq__(self, other: object) -> bool:
        """
        Check equality of PersonRequest objects.
        :param other: object, the object to compare to
        :return: bool, whether the PersonRequest objects are equal
        """
        if not isinstance(other, PersonRequest):
            return False
        return self.name == other.name and self.sex == other.sex and self.phoneNumber == other.phoneNumber


    def __ne__(self, other: object) -> bool:
        """
        Check inequality of PersonRequest objects.