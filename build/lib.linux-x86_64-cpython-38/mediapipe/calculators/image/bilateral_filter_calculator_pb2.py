# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/image/bilateral_filter_calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/image/bilateral_filter_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n=mediapipe/calculators/image/bilateral_filter_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xa7\x01\n BilateralFilterCalculatorOptions\x12\x13\n\x0bsigma_color\x18\x01 \x01(\x02\x12\x13\n\x0bsigma_space\x18\x02 \x01(\x02\x32Y\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xc1\xef\xf4y \x01(\x0b\x32+.mediapipe.BilateralFilterCalculatorOptions')
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_BILATERALFILTERCALCULATOROPTIONS = _descriptor.Descriptor(
  name='BilateralFilterCalculatorOptions',
  full_name='mediapipe.BilateralFilterCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sigma_color', full_name='mediapipe.BilateralFilterCalculatorOptions.sigma_color', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sigma_space', full_name='mediapipe.BilateralFilterCalculatorOptions.sigma_space', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.BilateralFilterCalculatorOptions.ext', index=0,
      number=255670209, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=282,
)

DESCRIPTOR.message_types_by_name['BilateralFilterCalculatorOptions'] = _BILATERALFILTERCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BilateralFilterCalculatorOptions = _reflection.GeneratedProtocolMessageType('BilateralFilterCalculatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _BILATERALFILTERCALCULATOROPTIONS,
  __module__ = 'mediapipe.calculators.image.bilateral_filter_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.BilateralFilterCalculatorOptions)
  ))
_sym_db.RegisterMessage(BilateralFilterCalculatorOptions)

_BILATERALFILTERCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _BILATERALFILTERCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_BILATERALFILTERCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)