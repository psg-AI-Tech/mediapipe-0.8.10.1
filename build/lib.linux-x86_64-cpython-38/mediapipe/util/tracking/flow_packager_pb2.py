# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/util/tracking/flow_packager.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.util.tracking import motion_models_pb2 as mediapipe_dot_util_dot_tracking_dot_motion__models__pb2
from mediapipe.util.tracking import region_flow_pb2 as mediapipe_dot_util_dot_tracking_dot_region__flow__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/util/tracking/flow_packager.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n+mediapipe/util/tracking/flow_packager.proto\x12\tmediapipe\x1a+mediapipe/util/tracking/motion_models.proto\x1a)mediapipe/util/tracking/region_flow.proto\"\xb1\x05\n\x0cTrackingData\x12\x16\n\x0b\x66rame_flags\x18\x01 \x01(\x05:\x01\x30\x12\x14\n\x0c\x64omain_width\x18\x02 \x01(\x05\x12\x15\n\rdomain_height\x18\x03 \x01(\x05\x12\x17\n\x0c\x66rame_aspect\x18\x06 \x01(\x02:\x01\x31\x12/\n\x10\x62\x61\x63kground_model\x18\x04 \x01(\x0b\x32\x15.mediapipe.Homography\x12\x37\n\x0bmotion_data\x18\x05 \x01(\x0b\x32\".mediapipe.TrackingData.MotionData\x12\x1c\n\x14global_feature_count\x18\x07 \x01(\r\x12 \n\x18\x61verage_motion_magnitude\x18\x08 \x01(\x02\x1a\xeb\x01\n\nMotionData\x12\x14\n\x0cnum_elements\x18\x01 \x01(\x05\x12\x17\n\x0bvector_data\x18\x02 \x03(\x02\x42\x02\x10\x01\x12\x14\n\x08track_id\x18\x03 \x03(\x05\x42\x02\x10\x01\x12\x17\n\x0brow_indices\x18\x04 \x03(\x05\x42\x02\x10\x01\x12\x16\n\ncol_starts\x18\x05 \x03(\x05\x42\x02\x10\x01\x12?\n\x13\x66\x65\x61ture_descriptors\x18\x06 \x03(\x0b\x32\".mediapipe.BinaryFeatureDescriptor\x12&\n\x1e\x61\x63tively_discarded_tracked_ids\x18\x07 \x03(\x05\"\xaa\x01\n\nFrameFlags\x12\x19\n\x15\x46LAG_PROFILE_BASELINE\x10\x00\x12\x15\n\x11\x46LAG_PROFILE_HIGH\x10\x01\x12\x1e\n\x1a\x46LAG_HIGH_FIDELITY_VECTORS\x10\x02\x12\x1c\n\x18\x46LAG_BACKGROUND_UNSTABLE\x10\x04\x12\x13\n\x0f\x46LAG_DUPLICATED\x10\x08\x12\x17\n\x13\x46LAG_CHUNK_BOUNDARY\x10\x10\"\xfb\x01\n\x11TrackingDataChunk\x12/\n\x04item\x18\x01 \x03(\x0b\x32!.mediapipe.TrackingDataChunk.Item\x12\x19\n\nlast_chunk\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0b\x66irst_chunk\x18\x03 \x01(\x08:\x05\x66\x61lse\x1a~\n\x04Item\x12.\n\rtracking_data\x18\x01 \x01(\x0b\x32\x17.mediapipe.TrackingData\x12\x11\n\tframe_idx\x18\x02 \x01(\x05\x12\x16\n\x0etimestamp_usec\x18\x03 \x01(\x03\x12\x1b\n\x13prev_timestamp_usec\x18\x04 \x01(\x03\"\"\n\x12\x42inaryTrackingData\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\"\x8a\x01\n\x08MetaData\x12\x12\n\nnum_frames\x18\x02 \x01(\x07\x12\x36\n\rtrack_offsets\x18\x03 \x03(\x0b\x32\x1f.mediapipe.MetaData.TrackOffset\x1a\x32\n\x0bTrackOffset\x12\x0c\n\x04msec\x18\x01 \x01(\x07\x12\x15\n\rstream_offset\x18\x02 \x01(\x07\"S\n\x11TrackingContainer\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x12\n\x07version\x18\x02 \x01(\x07:\x01\x31\x12\x0c\n\x04size\x18\x03 \x01(\x07\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"\xad\x01\n\x17TrackingContainerFormat\x12/\n\tmeta_data\x18\x01 \x01(\x0b\x32\x1c.mediapipe.TrackingContainer\x12\x30\n\ntrack_data\x18\x02 \x03(\x0b\x32\x1c.mediapipe.TrackingContainer\x12/\n\tterm_data\x18\x03 \x01(\x0b\x32\x1c.mediapipe.TrackingContainer\"s\n\x16TrackingContainerProto\x12&\n\tmeta_data\x18\x01 \x01(\x0b\x32\x13.mediapipe.MetaData\x12\x31\n\ntrack_data\x18\x02 \x03(\x0b\x32\x1d.mediapipe.BinaryTrackingData\"\xc1\x02\n\x13\x46lowPackagerOptions\x12\x19\n\x0c\x64omain_width\x18\x01 \x01(\x05:\x03\x32\x35\x36\x12\x1a\n\rdomain_height\x18\x02 \x01(\x05:\x03\x31\x39\x32\x12*\n\x1c\x62inary_tracking_data_support\x18\x06 \x01(\x08:\x04true\x12\x1f\n\x10use_high_profile\x18\x03 \x01(\x08:\x05\x66\x61lse\x12(\n\x1ahigh_fidelity_16bit_encode\x18\x04 \x01(\x08:\x04true\x12)\n\x1chigh_profile_reuse_threshold\x18\x05 \x01(\x02:\x03\x30.5\"Q\n\x13HighProfileEncoding\x12\x11\n\x0c\x41\x44VANCE_FLAG\x10\x80\x01\x12\x17\n\x13\x44OUBLE_INDEX_ENCODE\x10@\x12\x0e\n\nINDEX_MASK\x10?')
  ,
  dependencies=[mediapipe_dot_util_dot_tracking_dot_motion__models__pb2.DESCRIPTOR,mediapipe_dot_util_dot_tracking_dot_region__flow__pb2.DESCRIPTOR,])



_TRACKINGDATA_FRAMEFLAGS = _descriptor.EnumDescriptor(
  name='FrameFlags',
  full_name='mediapipe.TrackingData.FrameFlags',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FLAG_PROFILE_BASELINE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAG_PROFILE_HIGH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAG_HIGH_FIDELITY_VECTORS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAG_BACKGROUND_UNSTABLE', index=3, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAG_DUPLICATED', index=4, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLAG_CHUNK_BOUNDARY', index=5, number=16,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=666,
  serialized_end=836,
)
_sym_db.RegisterEnumDescriptor(_TRACKINGDATA_FRAMEFLAGS)

_FLOWPACKAGEROPTIONS_HIGHPROFILEENCODING = _descriptor.EnumDescriptor(
  name='HighProfileEncoding',
  full_name='mediapipe.FlowPackagerOptions.HighProfileEncoding',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ADVANCE_FLAG', index=0, number=128,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE_INDEX_ENCODE', index=1, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INDEX_MASK', index=2, number=63,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1888,
  serialized_end=1969,
)
_sym_db.RegisterEnumDescriptor(_FLOWPACKAGEROPTIONS_HIGHPROFILEENCODING)


_TRACKINGDATA_MOTIONDATA = _descriptor.Descriptor(
  name='MotionData',
  full_name='mediapipe.TrackingData.MotionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_elements', full_name='mediapipe.TrackingData.MotionData.num_elements', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vector_data', full_name='mediapipe.TrackingData.MotionData.vector_data', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='track_id', full_name='mediapipe.TrackingData.MotionData.track_id', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='row_indices', full_name='mediapipe.TrackingData.MotionData.row_indices', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='col_starts', full_name='mediapipe.TrackingData.MotionData.col_starts', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature_descriptors', full_name='mediapipe.TrackingData.MotionData.feature_descriptors', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actively_discarded_tracked_ids', full_name='mediapipe.TrackingData.MotionData.actively_discarded_tracked_ids', index=6,
      number=7, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=428,
  serialized_end=663,
)

_TRACKINGDATA = _descriptor.Descriptor(
  name='TrackingData',
  full_name='mediapipe.TrackingData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame_flags', full_name='mediapipe.TrackingData.frame_flags', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_width', full_name='mediapipe.TrackingData.domain_width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_height', full_name='mediapipe.TrackingData.domain_height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_aspect', full_name='mediapipe.TrackingData.frame_aspect', index=3,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='background_model', full_name='mediapipe.TrackingData.background_model', index=4,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='motion_data', full_name='mediapipe.TrackingData.motion_data', index=5,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_feature_count', full_name='mediapipe.TrackingData.global_feature_count', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average_motion_magnitude', full_name='mediapipe.TrackingData.average_motion_magnitude', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRACKINGDATA_MOTIONDATA, ],
  enum_types=[
    _TRACKINGDATA_FRAMEFLAGS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=147,
  serialized_end=836,
)


_TRACKINGDATACHUNK_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='mediapipe.TrackingDataChunk.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tracking_data', full_name='mediapipe.TrackingDataChunk.Item.tracking_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_idx', full_name='mediapipe.TrackingDataChunk.Item.frame_idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp_usec', full_name='mediapipe.TrackingDataChunk.Item.timestamp_usec', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prev_timestamp_usec', full_name='mediapipe.TrackingDataChunk.Item.prev_timestamp_usec', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=964,
  serialized_end=1090,
)

_TRACKINGDATACHUNK = _descriptor.Descriptor(
  name='TrackingDataChunk',
  full_name='mediapipe.TrackingDataChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='mediapipe.TrackingDataChunk.item', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_chunk', full_name='mediapipe.TrackingDataChunk.last_chunk', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_chunk', full_name='mediapipe.TrackingDataChunk.first_chunk', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRACKINGDATACHUNK_ITEM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=839,
  serialized_end=1090,
)


_BINARYTRACKINGDATA = _descriptor.Descriptor(
  name='BinaryTrackingData',
  full_name='mediapipe.BinaryTrackingData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='mediapipe.BinaryTrackingData.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=1092,
  serialized_end=1126,
)


_METADATA_TRACKOFFSET = _descriptor.Descriptor(
  name='TrackOffset',
  full_name='mediapipe.MetaData.TrackOffset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msec', full_name='mediapipe.MetaData.TrackOffset.msec', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream_offset', full_name='mediapipe.MetaData.TrackOffset.stream_offset', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1217,
  serialized_end=1267,
)

_METADATA = _descriptor.Descriptor(
  name='MetaData',
  full_name='mediapipe.MetaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_frames', full_name='mediapipe.MetaData.num_frames', index=0,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='track_offsets', full_name='mediapipe.MetaData.track_offsets', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_METADATA_TRACKOFFSET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1129,
  serialized_end=1267,
)


_TRACKINGCONTAINER = _descriptor.Descriptor(
  name='TrackingContainer',
  full_name='mediapipe.TrackingContainer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='mediapipe.TrackingContainer.header', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='mediapipe.TrackingContainer.version', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='size', full_name='mediapipe.TrackingContainer.size', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='mediapipe.TrackingContainer.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=1269,
  serialized_end=1352,
)


_TRACKINGCONTAINERFORMAT = _descriptor.Descriptor(
  name='TrackingContainerFormat',
  full_name='mediapipe.TrackingContainerFormat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_data', full_name='mediapipe.TrackingContainerFormat.meta_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='track_data', full_name='mediapipe.TrackingContainerFormat.track_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='term_data', full_name='mediapipe.TrackingContainerFormat.term_data', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1355,
  serialized_end=1528,
)


_TRACKINGCONTAINERPROTO = _descriptor.Descriptor(
  name='TrackingContainerProto',
  full_name='mediapipe.TrackingContainerProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_data', full_name='mediapipe.TrackingContainerProto.meta_data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='track_data', full_name='mediapipe.TrackingContainerProto.track_data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1530,
  serialized_end=1645,
)


_FLOWPACKAGEROPTIONS = _descriptor.Descriptor(
  name='FlowPackagerOptions',
  full_name='mediapipe.FlowPackagerOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_width', full_name='mediapipe.FlowPackagerOptions.domain_width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=256,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='domain_height', full_name='mediapipe.FlowPackagerOptions.domain_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=192,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binary_tracking_data_support', full_name='mediapipe.FlowPackagerOptions.binary_tracking_data_support', index=2,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_high_profile', full_name='mediapipe.FlowPackagerOptions.use_high_profile', index=3,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high_fidelity_16bit_encode', full_name='mediapipe.FlowPackagerOptions.high_fidelity_16bit_encode', index=4,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high_profile_reuse_threshold', full_name='mediapipe.FlowPackagerOptions.high_profile_reuse_threshold', index=5,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.5),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FLOWPACKAGEROPTIONS_HIGHPROFILEENCODING,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1648,
  serialized_end=1969,
)

_TRACKINGDATA_MOTIONDATA.fields_by_name['feature_descriptors'].message_type = mediapipe_dot_util_dot_tracking_dot_region__flow__pb2._BINARYFEATUREDESCRIPTOR
_TRACKINGDATA_MOTIONDATA.containing_type = _TRACKINGDATA
_TRACKINGDATA.fields_by_name['background_model'].message_type = mediapipe_dot_util_dot_tracking_dot_motion__models__pb2._HOMOGRAPHY
_TRACKINGDATA.fields_by_name['motion_data'].message_type = _TRACKINGDATA_MOTIONDATA
_TRACKINGDATA_FRAMEFLAGS.containing_type = _TRACKINGDATA
_TRACKINGDATACHUNK_ITEM.fields_by_name['tracking_data'].message_type = _TRACKINGDATA
_TRACKINGDATACHUNK_ITEM.containing_type = _TRACKINGDATACHUNK
_TRACKINGDATACHUNK.fields_by_name['item'].message_type = _TRACKINGDATACHUNK_ITEM
_METADATA_TRACKOFFSET.containing_type = _METADATA
_METADATA.fields_by_name['track_offsets'].message_type = _METADATA_TRACKOFFSET
_TRACKINGCONTAINERFORMAT.fields_by_name['meta_data'].message_type = _TRACKINGCONTAINER
_TRACKINGCONTAINERFORMAT.fields_by_name['track_data'].message_type = _TRACKINGCONTAINER
_TRACKINGCONTAINERFORMAT.fields_by_name['term_data'].message_type = _TRACKINGCONTAINER
_TRACKINGCONTAINERPROTO.fields_by_name['meta_data'].message_type = _METADATA
_TRACKINGCONTAINERPROTO.fields_by_name['track_data'].message_type = _BINARYTRACKINGDATA
_FLOWPACKAGEROPTIONS_HIGHPROFILEENCODING.containing_type = _FLOWPACKAGEROPTIONS
DESCRIPTOR.message_types_by_name['TrackingData'] = _TRACKINGDATA
DESCRIPTOR.message_types_by_name['TrackingDataChunk'] = _TRACKINGDATACHUNK
DESCRIPTOR.message_types_by_name['BinaryTrackingData'] = _BINARYTRACKINGDATA
DESCRIPTOR.message_types_by_name['MetaData'] = _METADATA
DESCRIPTOR.message_types_by_name['TrackingContainer'] = _TRACKINGCONTAINER
DESCRIPTOR.message_types_by_name['TrackingContainerFormat'] = _TRACKINGCONTAINERFORMAT
DESCRIPTOR.message_types_by_name['TrackingContainerProto'] = _TRACKINGCONTAINERPROTO
DESCRIPTOR.message_types_by_name['FlowPackagerOptions'] = _FLOWPACKAGEROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrackingData = _reflection.GeneratedProtocolMessageType('TrackingData', (_message.Message,), dict(

  MotionData = _reflection.GeneratedProtocolMessageType('MotionData', (_message.Message,), dict(
    DESCRIPTOR = _TRACKINGDATA_MOTIONDATA,
    __module__ = 'mediapipe.util.tracking.flow_packager_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.TrackingData.MotionData)
    ))
  ,
  DESCRIPTOR = _TRACKINGDATA,
  __module__ = 'mediapipe.util.tracking.flow_packager_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TrackingData)
  ))
_sym_db.RegisterMessage(TrackingData)
_sym_db.RegisterMessage(TrackingData.MotionData)

TrackingDataChunk = _reflection.GeneratedProtocolMessageType('TrackingDataChunk', (_message.Message,), dict(

  Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
    DESCRIPTOR = _TRACKINGDATACHUNK_ITEM,
    __module__ = 'mediapipe.util.tracking.flow_packager_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.TrackingDataChunk.Item)
    ))
  ,
  DESCRIPTOR = _TRACKINGDATACHUNK,
  __module__ = 'mediapipe.util.tracking.flow_packager_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TrackingDataChunk)
  ))
_sym_db.RegisterMessage(TrackingDataChunk)
_sym_db.RegisterMessage(TrackingDataChunk.Item)

BinaryTrackingData = _reflection.GeneratedProtocolMessageType('BinaryTrackingData', (_message.Message,), dict(
  DESCRIPTOR = _BINARYTRACKINGDATA,
  __module__ = 'mediapipe.util.tracking.flow_packager_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.BinaryTrackingData)
  ))
_sym_db.RegisterMessage(BinaryTrackingData)

MetaData = _reflection.GeneratedProtocolMessageType('MetaData', (_message.Message,), dict(

  TrackOffset = _reflection.GeneratedProtocolMessageType('TrackOffset', (_message.Message,), dict(
    DESCRIPTOR = _METADATA_TRACKOFFSET,
    __module__ = 'mediapipe.util.tracking.flow_packager_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.MetaData.TrackOffset)
    ))
  ,
  DESCRIPTOR = _METADATA,
  __module__ = 'mediapipe.util.tracking.flow_packager_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.MetaData)
  ))
_sym_db.RegisterMessage(MetaData)
_sym_db.RegisterMessage(MetaData.TrackOffset)

TrackingContainer = _reflection.GeneratedProtocolMessageType('TrackingContainer', (_message.Message,), dict(
  DESCRIPTOR = _TRACKINGCONTAINER,
  __module__ = 'mediapipe.util.tracking.flow_packager_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TrackingContainer)
  ))
_sym_db.RegisterMessage(TrackingContainer)

TrackingContainerFormat = _reflection.GeneratedProtocolMessageType('TrackingContainerFormat', (_message.Message,), dict(
  DESCRIPTOR = _TRACKINGCONTAINERFORMAT,
  __module__ = 'mediapipe.util.tracking.flow_packager_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TrackingContainerFormat)
  ))
_sym_db.RegisterMessage(TrackingContainerFormat)

TrackingContainerProto = _reflection.GeneratedProtocolMessageType('TrackingContainerProto', (_message.Message,), dict(
  DESCRIPTOR = _TRACKINGCONTAINERPROTO,
  __module__ = 'mediapipe.util.tracking.flow_packager_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TrackingContainerProto)
  ))
_sym_db.RegisterMessage(TrackingContainerProto)

FlowPackagerOptions = _reflection.GeneratedProtocolMessageType('FlowPackagerOptions', (_message.Message,), dict(
  DESCRIPTOR = _FLOWPACKAGEROPTIONS,
  __module__ = 'mediapipe.util.tracking.flow_packager_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.FlowPackagerOptions)
  ))
_sym_db.RegisterMessage(FlowPackagerOptions)


_TRACKINGDATA_MOTIONDATA.fields_by_name['vector_data']._options = None
_TRACKINGDATA_MOTIONDATA.fields_by_name['track_id']._options = None
_TRACKINGDATA_MOTIONDATA.fields_by_name['row_indices']._options = None
_TRACKINGDATA_MOTIONDATA.fields_by_name['col_starts']._options = None
# @@protoc_insertion_point(module_scope)