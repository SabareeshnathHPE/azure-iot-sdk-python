# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BulkEnrollmentOperation(Model):
    """Bulk operation.

    :param mode: Operation mode. Possible values include: 'create', 'update',
     'updateIfMatchETag', 'delete'
    :type mode: str or ~serviceswagger.models.enum
    :param enrollments: Enrollment items
    :type enrollments: list[~serviceswagger.models.IndividualEnrollment]
    """

    _validation = {
        'mode': {'required': True},
        'enrollments': {'required': True},
    }

    _attribute_map = {
        'mode': {'key': 'mode', 'type': 'str'},
        'enrollments': {'key': 'enrollments', 'type': '[IndividualEnrollment]'},
    }

    def __init__(self, mode, enrollments):
        self.mode = mode
        self.enrollments = enrollments
