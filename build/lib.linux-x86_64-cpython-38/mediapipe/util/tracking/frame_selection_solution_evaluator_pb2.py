# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/util/tracking/frame_selection_solution_evaluator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/util/tracking/frame_selection_solution_evaluator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n@mediapipe/util/tracking/frame_selection_solution_evaluator.proto\x12\tmediapipe\"4\n&FrameSelectionSolutionEvaluatorOptions*\n\x08\xa0\x9c\x01\x10\x80\x80\x80\x80\x02\"\x9e\x01\n#FrameSelectionSolutionEvaluatorType\x12\x33\n\nclass_name\x18\x01 \x01(\t:\x1f\x46rameSelectionSolutionEvaluator\x12\x42\n\x07options\x18\x02 \x01(\x0b\x32\x31.mediapipe.FrameSelectionSolutionEvaluatorOptions')
)




_FRAMESELECTIONSOLUTIONEVALUATOROPTIONS = _descriptor.Descriptor(
  name='FrameSelectionSolutionEvaluatorOptions',
  full_name='mediapipe.FrameSelectionSolutionEvaluatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(20000, 536870912), ],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=131,
)


_FRAMESELECTIONSOLUTIONEVALUATORTYPE = _descriptor.Descriptor(
  name='FrameSelectionSolutionEvaluatorType',
  full_name='mediapipe.FrameSelectionSolutionEvaluatorType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='class_name', full_name='mediapipe.FrameSelectionSolutionEvaluatorType.class_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("FrameSelectionSolutionEvaluator").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='mediapipe.FrameSelectionSolutionEvaluatorType.options', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
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
  serialized_start=134,
  serialized_end=292,
)

_FRAMESELECTIONSOLUTIONEVALUATORTYPE.fields_by_name['options'].message_type = _FRAMESELECTIONSOLUTIONEVALUATOROPTIONS
DESCRIPTOR.message_types_by_name['FrameSelectionSolutionEvaluatorOptions'] = _FRAMESELECTIONSOLUTIONEVALUATOROPTIONS
DESCRIPTOR.message_types_by_name['FrameSelectionSolutionEvaluatorType'] = _FRAMESELECTIONSOLUTIONEVALUATORTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FrameSelectionSolutionEvaluatorOptions = _reflection.GeneratedProtocolMessageType('FrameSelectionSolutionEvaluatorOptions', (_message.Message,), dict(
  DESCRIPTOR = _FRAMESELECTIONSOLUTIONEVALUATOROPTIONS,
  __module__ = 'mediapipe.util.tracking.frame_selection_solution_evaluator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.FrameSelectionSolutionEvaluatorOptions)
  ))
_sym_db.RegisterMessage(FrameSelectionSolutionEvaluatorOptions)

FrameSelectionSolutionEvaluatorType = _reflection.GeneratedProtocolMessageType('FrameSelectionSolutionEvaluatorType', (_message.Message,), dict(
  DESCRIPTOR = _FRAMESELECTIONSOLUTIONEVALUATORTYPE,
  __module__ = 'mediapipe.util.tracking.frame_selection_solution_evaluator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.FrameSelectionSolutionEvaluatorType)
  ))
_sym_db.RegisterMessage(FrameSelectionSolutionEvaluatorType)


# @@protoc_insertion_point(module_scope)
