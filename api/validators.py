from django.core.exceptions import ValidationError


def validate_schema(schema):

    def func(value):
        try:
            from jsonschema import validate
            validate(value, schema)

        except Exception as ex:
            raise ValidationError(str(ex))

    return func



def validate_existence(available):

    available = list(available)

    def func(array):
        if not isinstance(array, list):
            raise ValidationError(str(array) + ": is not an array!")

        for item in array:
            if item["system_id"] not in available:
                raise ValidationError(str(item["system_id"]) + ": does not exist")

    return func
