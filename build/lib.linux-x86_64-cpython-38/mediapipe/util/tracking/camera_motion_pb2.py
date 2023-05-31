# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/util/tracking/camera_motion.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.util.tracking import motion_models_pb2 as mediapipe_dot_util_dot_tracking_dot_motion__models__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/util/tracking/camera_motion.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n+mediapipe/util/tracking/camera_motion.proto\x12\tmediapipe\x1a+mediapipe/util/tracking/motion_models.proto\"\x86\x0b\n\x0c\x43\x61meraMotion\x12\x30\n\x0btranslation\x18\x01 \x01(\x0b\x32\x1b.mediapipe.TranslationModel\x12.\n\nsimilarity\x18\x02 \x01(\x0b\x32\x1a.mediapipe.SimilarityModel\x12;\n\x11linear_similarity\x18\x03 \x01(\x0b\x32 .mediapipe.LinearSimilarityModel\x12&\n\x06\x61\x66\x66ine\x18\x04 \x01(\x0b\x32\x16.mediapipe.AffineModel\x12)\n\nhomography\x18\x05 \x01(\x0b\x32\x15.mediapipe.Homography\x12\x38\n\x12mixture_homography\x18\x08 \x01(\x0b\x32\x1c.mediapipe.MixtureHomography\x12\x13\n\x0b\x66rame_width\x18\x1f \x01(\x02\x12\x14\n\x0c\x66rame_height\x18  \x01(\x02\x12\x41\n\x1bmixture_homography_spectrum\x18\x17 \x03(\x0b\x32\x1c.mediapipe.MixtureHomography\x12\x19\n\x11mixture_row_sigma\x18\n \x01(\x02\x12\x1c\n\x11\x61verage_magnitude\x18\x18 \x01(\x02:\x01\x30\x12\x1f\n\x14translation_variance\x18\x19 \x01(\x02:\x01\x30\x12\"\n\x17similarity_inlier_ratio\x18\x1d \x01(\x02:\x01\x30\x12)\n\x1esimilarity_strict_inlier_ratio\x18\x1e \x01(\x02:\x01\x30\x12 \n\x18\x61verage_homography_error\x18\x0b \x01(\x02\x12\"\n\x1ahomography_inlier_coverage\x18\x0c \x01(\x02\x12)\n!homography_strict_inlier_coverage\x18\x16 \x01(\x02\x12\x1f\n\x17mixture_inlier_coverage\x18\r \x03(\x02\x12\x1d\n\x15rolling_shutter_guess\x18\x0e \x01(\x02\x12(\n\x1crolling_shutter_motion_index\x18\x10 \x01(\x05:\x02-1\x12\x17\n\x0foverlay_indices\x18\x11 \x03(\x05\x12\x1a\n\x0eoverlay_domain\x18\x12 \x01(\x05:\x02\x31\x30\x12\x31\n\x04type\x18\x06 \x01(\x0e\x32\x1c.mediapipe.CameraMotion.Type:\x05VALID\x12<\n\x0foverridden_type\x18\x0f \x01(\x0e\x32\x1c.mediapipe.CameraMotion.Type:\x05VALID\x12\x10\n\x05\x66lags\x18\x13 \x01(\x05:\x01\x30\x12\x12\n\nblur_score\x18\x14 \x01(\x02\x12\x14\n\tbluriness\x18\x15 \x01(\x02:\x01\x30\x12#\n\x1b\x66rac_long_features_rejected\x18\x1a \x01(\x02\x12\x19\n\x0etimestamp_usec\x18\x1b \x01(\x03:\x01\x30\x12\x16\n\x0bmatch_frame\x18\x1c \x01(\x05:\x01\x30\"R\n\x04Type\x12\t\n\x05VALID\x10\x00\x12\x12\n\x0eUNSTABLE_HOMOG\x10\x01\x12\x10\n\x0cUNSTABLE_SIM\x10\x02\x12\x0c\n\x08UNSTABLE\x10\x03\x12\x0b\n\x07INVALID\x10\x04\"\xc3\x01\n\x05\x46lags\x12\x16\n\x12\x46LAG_SHOT_BOUNDARY\x10\x01\x12\x15\n\x11\x46LAG_BLURRY_FRAME\x10\x02\x12\x16\n\x12\x46LAG_MAJOR_OVERLAY\x10\x04\x12\x14\n\x10\x46LAG_SHARP_FRAME\x10\x08\x12\x1c\n\x18\x46LAG_SINGULAR_ESTIMATION\x10\x10\x12\x12\n\x0e\x46LAG_SHOT_FADE\x10 \x12\x13\n\x0f\x46LAG_DUPLICATED\x10@\x12\x16\n\x11\x46LAG_CENTER_FRAME\x10\x80\x01*\x04\x08\t\x10\n')
  ,
  dependencies=[mediapipe_dot_util_dot_tracking_dot_motion__models__pb2.DESCRIPTOR,])



_CAMERAMOTION_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='mediapipe.CameraMotion.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSTABLE_HOMOG', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSTABLE_SIM', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSTABLE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1232,
  serialized_end=1314,
)
_sym_db.RegisterEnumDescriptor(_CAMERAMOTION_TYPE)

_CAMERAMOTION_FLAGS = _descriptor.EnumDescriptor(
  name='Flags',
  full_name='mediapipe.CameraMotion.Flags',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FLAG_SHOT_BOUNDARY', index=0, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAG_BLURRY_FRAME', index=1, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAG_MAJOR_OVERLAY', index=2, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAG_SHARP_FRAME', index=3, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAG_SINGULAR_ESTIMATION', index=4, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAG_SHOT_FADE', index=5, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAG_DUPLICATED', index=6, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAG_CENTER_FRAME', index=7, number=128,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1317,
  serialized_end=1512,
)
_sym_db.RegisterEnumDescriptor(_CAMERAMOTION_FLAGS)


_CAMERAMOTION = _descriptor.Descriptor(
  name='CameraMotion',
  full_name='mediapipe.CameraMotion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='translation', full_name='mediapipe.CameraMotion.translation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='similarity', full_name='mediapipe.CameraMotion.similarity', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='linear_similarity', full_name='mediapipe.CameraMotion.linear_similarity', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='affine', full_name='mediapipe.CameraMotion.affine', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homography', full_name='mediapipe.CameraMotion.homography', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mixture_homography', full_name='mediapipe.CameraMotion.mixture_homography', index=5,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_width', full_name='mediapipe.CameraMotion.frame_width', index=6,
      number=31, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_height', full_name='mediapipe.CameraMotion.frame_height', index=7,
      number=32, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mixture_homography_spectrum', full_name='mediapipe.CameraMotion.mixture_homography_spectrum', index=8,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mixture_row_sigma', full_name='mediapipe.CameraMotion.mixture_row_sigma', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average_magnitude', full_name='mediapipe.CameraMotion.average_magnitude', index=10,
      number=24, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='translation_variance', full_name='mediapipe.CameraMotion.translation_variance', index=11,
      number=25, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='similarity_inlier_ratio', full_name='mediapipe.CameraMotion.similarity_inlier_ratio', index=12,
      number=29, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='similarity_strict_inlier_ratio', full_name='mediapipe.CameraMotion.similarity_strict_inlier_ratio', index=13,
      number=30, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average_homography_error', full_name='mediapipe.CameraMotion.average_homography_error', index=14,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homography_inlier_coverage', full_name='mediapipe.CameraMotion.homography_inlier_coverage', index=15,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='homography_strict_inlier_coverage', full_name='mediapipe.CameraMotion.homography_strict_inlier_coverage', index=16,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mixture_inlier_coverage', full_name='mediapipe.CameraMotion.mixture_inlier_coverage', index=17,
      number=13, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rolling_shutter_guess', full_name='mediapipe.CameraMotion.rolling_shutter_guess', index=18,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rolling_shutter_motion_index', full_name='mediapipe.CameraMotion.rolling_shutter_motion_index', index=19,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overlay_indices', full_name='mediapipe.CameraMotion.overlay_indices', index=20,
      number=17, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overlay_domain', full_name='mediapipe.CameraMotion.overlay_domain', index=21,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='mediapipe.CameraMotion.type', index=22,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overridden_type', full_name='mediapipe.CameraMotion.overridden_type', index=23,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='flags', full_name='mediapipe.CameraMotion.flags', index=24,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blur_score', full_name='mediapipe.CameraMotion.blur_score', index=25,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bluriness', full_name='mediapipe.CameraMotion.bluriness', index=26,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frac_long_features_rejected', full_name='mediapipe.CameraMotion.frac_long_features_rejected', index=27,
      number=26, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_usec', full_name='mediapipe.CameraMotion.timestamp_usec', index=28,
      number=27, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='match_frame', full_name='mediapipe.CameraMotion.match_frame', index=29,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CAMERAMOTION_TYPE,
    _CAMERAMOTION_FLAGS,
  ],
  serialized_options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(9, 10), ],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=1518,
)

_CAMERAMOTION.fields_by_name['translation'].message_type = mediapipe_dot_util_dot_tracking_dot_motion__models__pb2._TRANSLATIONMODEL
_CAMERAMOTION.fields_by_name['similarity'].message_type = mediapipe_dot_util_dot_tracking_dot_motion__models__pb2._SIMILARITYMODEL
_CAMERAMOTION.fields_by_name['linear_similarity'].message_type = mediapipe_dot_util_dot_tracking_dot_motion__models__pb2._LINEARSIMILARITYMODEL
_CAMERAMOTION.fields_by_name['affine'].message_type = mediapipe_dot_util_dot_tracking_dot_motion__models__pb2._AFFINEMODEL
_CAMERAMOTION.fields_by_name['homography'].message_type = mediapipe_dot_util_dot_tracking_dot_motion__models__pb2._HOMOGRAPHY
_CAMERAMOTION.fields_by_name['mixture_homography'].message_type = mediapipe_dot_util_dot_tracking_dot_motion__models__pb2._MIXTUREHOMOGRAPHY
_CAMERAMOTION.fields_by_name['mixture_homography_spectrum'].message_type = mediapipe_dot_util_dot_tracking_dot_motion__models__pb2._MIXTUREHOMOGRAPHY
_CAMERAMOTION.fields_by_name['type'].enum_type = _CAMERAMOTION_TYPE
_CAMERAMOTION.fields_by_name['overridden_type'].enum_type = _CAMERAMOTION_TYPE
_CAMERAMOTION_TYPE.containing_type = _CAMERAMOTION
_CAMERAMOTION_FLAGS.containing_type = _CAMERAMOTION
DESCRIPTOR.message_types_by_name['CameraMotion'] = _CAMERAMOTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CameraMotion = _reflection.GeneratedProtocolMessageType('CameraMotion', (_message.Message,), dict(
  DESCRIPTOR = _CAMERAMOTION,
  __module__ = 'mediapipe.util.tracking.camera_motion_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.CameraMotion)
  ))
_sym_db.RegisterMessage(CameraMotion)


# @@protoc_insertion_point(module_scope)
