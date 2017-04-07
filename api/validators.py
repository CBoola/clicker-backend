from django.core.exceptions import ValidationError


def validate_type(type):

    def func(value):
        if not isinstance(value, type):
            raise ValidationError(str(value) + ": is not a " + str(type))

    return func


def validate_schema(schema):

    def func(value):
        try:
            from jsonschema import validate
            validate(value, schema)

        except Exception as ex:
            raise ValidationError(str(ex))

    return func



def validate_existence(queryset):

    available = list(queryset.values_list("system_id", flat=True))
    print(available)

    def func(array):
        if not isinstance(array, list):
            raise ValidationError(str(array) + ": is not an array!")

        for item in array:
            print(item)

            if item["system_id"] not in available:
                raise ValidationError(str(item["system_id"]) + ": does not exist")

    return func
