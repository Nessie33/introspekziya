import inspect
import types


def introspection_info(obj):
    obj_type = type(obj).__name__
    atributes = dir(obj)
    methods = [attr for attr in atributes if callable(getattr(obj, attr)) and not attr.startswith('__')]
    module = getattr(obj, '__module__', 'builtins' if obj_type in dir(__builtins__) else 'main')
    info = {
        'type': obj_type,
        'atributes': atributes,
        'methods': methods,
        'module': module
    }
    return info


number_info = introspection_info(42)
print(number_info)

string_info = introspection_info('Hello!')
print(string_info)