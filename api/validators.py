from django.core.exceptions import ValidationError

from jsonschema import Draft4Validator, validators


def extend_with_default(validator_class):
    validate_properties = validator_class.VALIDATORS["properties"]

    def set_defaults(validator, properties, instance, schema):
        for property, subschema in properties.items():
            if "default" in subschema:
                instance.setdefault(property, subschema["default"])

        for error in validate_properties(validator, properties, instance, schema):
            yield error

    return validators.extend(validator_class, {"properties" : set_defaults})


def validate_type(type):

    def func(value):
        if not isinstance(value, type):
            raise ValidationError(str(value) + ": is not a " + str(type))

    return func


def validate_schema(schema):

    def func(value):
        try:
            validator = extend_with_default(Draft4Validator)(schema)
            validator.validate(value)

        except Exception as ex:
            raise ValidationError(str(ex))

    return func



def validate_existence(queryset):

    available = list(queryset.values_list("system_id", flat=True))

    def func(array):
        if not isinstance(array, list):
            raise ValidationError(str(array) + ": is not an array!")

        for item in array:
            if item["system_id"] not in available:
                raise ValidationError(str(item["system_id"]) + ": does not exist")

    return func
