
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
        


    def _validate_sex(self, sex: str) -> str:


    def _validate_sex(self, sex: str) -> str:


    def _validate_sex(self, sex: str) -> str:


    def _validate_phoneNumber(self, phoneNumber: str) -> str:
