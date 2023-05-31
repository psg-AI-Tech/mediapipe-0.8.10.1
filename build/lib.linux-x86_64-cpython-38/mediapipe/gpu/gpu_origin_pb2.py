# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/gpu/gpu_origin.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/gpu/gpu_origin.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x1emediapipe/gpu/gpu_origin.proto\x12\tmediapipe\"@\n\tGpuOrigin\"3\n\x04Mode\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x10\n\x0c\x43ONVENTIONAL\x10\x01\x12\x0c\n\x08TOP_LEFT\x10\x02')
)



_GPUORIGIN_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='mediapipe.GpuOrigin.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONVENTIONAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOP_LEFT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=58,
  serialized_end=109,
)
_sym_db.RegisterEnumDescriptor(_GPUORIGIN_MODE)


_GPUORIGIN = _descriptor.Descriptor(
  name='GpuOrigin',
  full_name='mediapipe.GpuOrigin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GPUORIGIN_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=109,
)

_GPUORIGIN_MODE.containing_type = _GPUORIGIN
DESCRIPTOR.message_types_by_name['GpuOrigin'] = _GPUORIGIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GpuOrigin = _reflection.GeneratedProtocolMessageType('GpuOrigin', (_message.Message,), dict(
  DESCRIPTOR = _GPUORIGIN,
  __module__ = 'mediapipe.gpu.gpu_origin_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.GpuOrigin)
  ))
_sym_db.RegisterMessage(GpuOrigin)


# @@protoc_insertion_point(module_scope)
